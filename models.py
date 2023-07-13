from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from flask_bcrypt import Bcrypt
import re
from datetime import datetime

from extensions import db

bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = "users"

    US_STATE_CODES = {
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
    }

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(254), unique=True, nullable=False)
    password = db.Column(db.String(254))
    city = db.Column(db.String(120))
    state = db.Column(db.String(2))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    last_login = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    aquariums = db.relationship("Aquarium", backref="owner", lazy="dynamic")
    shared_aquariums = db.relationship("UserAquarium", back_populates="user")
    posts = db.relationship("Post", backref="user", lazy="dynamic")
    comments = db.relationship("Comment", backref="user", lazy="dynamic")

    @validates("email")
    def validate_email(self, key, email):
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise AssertionError("Provided email is not a valid email.")
        return email

    @validates("state")
    def validate_state(self, key, state):
        if state.upper() not in self.US_STATE_CODES:
            raise AssertionError("Provided state is not a valid US state code.")
        return state.upper()

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "city": self.city,
            "state": self.state,
            "created_at": self.created_at,
            "last_login": self.last_login,
            "aquariums": [aquarium.to_dict() for aquarium in self.aquariums],
            "shared_aquariums": [
                {
                    "id": shared_aquarium.id,
                    "user_id": shared_aquarium.user_id,
                    "aquarium": shared_aquarium.aquarium.to_dict(),
                }
                for shared_aquarium in self.shared_aquariums
            ],
        }

    def __repr__(self):
        return f"<User {self.id} {self.email}>"


class Aquarium(db.Model):
    __tablename__ = "aquariums"

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    brand = db.Column(db.String(120))
    model = db.Column(db.String(120))
    volume = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    shared_users = db.relationship("UserAquarium", back_populates="aquarium")
    water_parameters = db.relationship("WaterParameter", backref="aquarium")

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "brand": self.brand,
            "model": self.model,
            "volume": self.volume,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "water_parameters": [
                water_parameter.to_dict() for water_parameter in self.water_parameters
            ],
        }

    def __repr__(self):
        return f"<Aquarium {self.id} {self.brand} {self.model} {self.volume}>"


class UserAquarium(db.Model):
    __tablename__ = "user_aquariums"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    aquarium_id = db.Column(db.Integer, db.ForeignKey("aquariums.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    __table_args__ = (
        db.UniqueConstraint("user_id", "aquarium_id", name="uq_user_aquarium"),
    )

    user = db.relationship("User", back_populates="shared_aquariums")
    aquarium = db.relationship("Aquarium", back_populates="shared_users")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "aquarium_id": self.aquarium_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "aquarium": self.aquarium.to_dict(),
        }

    def __repr__(self):
        return f"<UserAquarium {self.id} {self.user_id} {self.aquarium_id}>"


class WaterParameter(db.Model):
    __tablename__ = "water_parameters"

    id = db.Column(db.Integer, primary_key=True)
    aquarium_id = db.Column(db.Integer, db.ForeignKey("aquariums.id"))
    date_recorded = db.Column(db.Date, nullable=False, default=datetime.utcnow().date)
    salinity = db.Column(db.Float)
    ph = db.Column(db.Float)
    ammonia = db.Column(db.Float)
    nitrate = db.Column(db.Float)
    phosphate = db.Column(db.Float)
    calcium = db.Column(db.Float)
    magnesium = db.Column(db.Float)
    alkalinity = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "aquarium_id": self.aquarium_id,
            "date_recorded": self.date_recorded.strftime("%Y-%m-%d"),
            "salinity": self.salinity,
            "ph": self.ph,
            "ammonia": self.ammonia,
            "nitrate": self.nitrate,
            "phosphate": self.phosphate,
            "calcium": self.calcium,
            "magnesium": self.magnesium,
            "alkalinity": self.alkalinity,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __repr__(self):
        return f"<Parameters {self.id} {self.aquarium_id} {self.salinity} {self.ph} {self.ammonia} {self.nitrate} {self.phosphate} {self.calcium} {self.magnesium} {self.alkalinity}>"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    comments = db.relationship("Comment", backref="post")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "comments": [comment.to_dict() for comment in self.comments],
            "user": self.user.to_dict(),
        }

    def __repr__(self):
        return f"<Post {self.id} {self.user_id} {self.title}>"


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.to_dict(),
        }

    def __repr__(self):
        return f"<Comment {self.id} {self.user_id} {self.post_id}>"
