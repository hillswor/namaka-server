from random import choice as random_choice, uniform
from faker import Faker
import ipdb

from extensions import db
from app import app
from models import User, Aquarium, WaterParameter, Post, UserAquarium, Comment

fake = Faker()

valid_us_state_codes = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]


aquarium_brands = [
    "Red Sea",
    "Innovative Marine",
    "Waterbox",
    "Coralife",
    "Fluval",
    "JBJ",
    "Marineland",
    "Aqueon",
    "Deep Blue",
    "SC Aquarium",
]

aquarium_models = [
    "Reefer",
    "Fusion",
    "Marine",
    "BioCube",
    "Evo",
    "Rimless",
    "Contour",
    "Cube",
    "Peninsula",
    "Concept",
    "Signature",
    "Clear-For-Life",
    "Edge",
    "Ascent",
    "Frameless",
    "Artisan",
    "Rimless",
    "Pro",
    "Standard",
]

aquarium_volumes = [
    10,
    20,
    30,
    40,
    50,
    60,
    75,
    90,
    100,
    120,
    150,
    180,
    200,
    220,
    240,
    300,
    360,
    400,
    500,
    600,
    700,
    800,
    900,
    1000,
]


def clear_data():
    db.session.query(UserAquarium).delete()
    db.session.query(WaterParameter).delete()
    db.session.query(Aquarium).delete()
    db.session.query(Comment).delete()
    db.session.query(Post).delete()
    db.session.query(User).delete()
    db.session.commit()


def seed_users():
    for i in range(30):
        password = "password"
        user = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=password,
            city=fake.city(),
            state=random_choice(valid_us_state_codes),
        )
        user.set_password(password)
        db.session.add(user)
    db.session.commit()


def seed_aquariums():
    users = User.query.all()
    for i in range(60):
        owner_id = random_choice(users).id
        brand = random_choice(aquarium_brands)
        model = random_choice(aquarium_models)
        volume = random_choice(aquarium_volumes)
        aquarium = Aquarium(owner_id=owner_id, brand=brand, model=model, volume=volume)
        db.session.add(aquarium)
    db.session.commit()


def seed_water_parameters():
    aquariums = Aquarium.query.all()
    for i in range(1000):
        new_water_parameters = WaterParameter(
            aquarium_id=random_choice(aquariums).id,
            date_recorded=fake.date_between(
                start_date="-1y", end_date="today"
            ).strftime("%Y-%m-%d"),
            salinity=round(uniform(1.01, 1.04), 3),
            ph=round(uniform(7.0, 9.0), 1),
            ammonia=round(uniform(0, 0.50), 2),
            nitrate=round(uniform(0, 5), 2),
            phosphate=round(uniform(0, 0.06), 3),
            calcium=round(uniform(300, 900), 1),
            magnesium=round(uniform(1100, 2000), 1),
            alkalinity=round(uniform(6, 20), 1),
        )

        db.session.add(new_water_parameters)
    db.session.commit()


def seed_posts():
    users = User.query.all()
    for i in range(10):
        new_post = Post(
            user_id=random_choice(users).id,
            title=fake.sentence(nb_words=6, variable_nb_words=True),
            content=fake.text(max_nb_chars=500),
        )
        db.session.add(new_post)
    db.session.commit()


def seed_comments():
    users = User.query.all()
    posts = Post.query.all()
    for i in range(25):
        new_comment = Comment(
            user_id=random_choice(users).id,
            post_id=random_choice(posts).id,
            content=fake.text(max_nb_chars=300),
        )
        db.session.add(new_comment)
    db.session.commit()


def seed_user_aquariums():
    users = User.query.all()
    aquariums = Aquarium.query.all()
    for i in range(10):
        new_user_aquarium = UserAquarium(
            user_id=random_choice(users).id,
            aquarium_id=random_choice(aquariums).id,
        )
        db.session.add(new_user_aquarium)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        clear_data()
        seed_users()
        seed_aquariums()
        seed_water_parameters()
        seed_posts()
        seed_comments()
        seed_user_aquariums()
