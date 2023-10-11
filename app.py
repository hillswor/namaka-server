from flask import Flask, request, session, make_response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_bcrypt import check_password_hash
from dotenv import load_dotenv
from flask_session import Session
from datetime import date
import os


from models import User, Aquarium, WaterParameter, Post, Comment, UserAquarium
from extensions import db, migrate

load_dotenv()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.json.compact = False
    app.secret_key = os.getenv("SECRET_KEY")

    Session(app)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()
api = Api(app)


class HomePage(Resource):
    def get(self):
        return "Welcome to the Namaka API"


api.add_resource(HomePage, "/")


class UserResource(Resource):
    def post(self):
        data = request.get_json()
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        email = data.get("email")
        password = data.get("password")
        city = data.get("city")
        state = data.get("state")

        new_user = User(
            first_name=first_name.title(),
            last_name=last_name.title(),
            email=email.lower(),
            password=password,
            city=city.title(),
            state=state.upper(),
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id

        return make_response(jsonify(new_user.to_dict()), 201)


api.add_resource(UserResource, "/users")


class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        try:
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                session.modified = True  # Mark the session as modified
                session.save()  # Save the session data
                return make_response(jsonify(user.to_dict()), 200)
            else:
                return make_response(jsonify({"error": "Invalid credentials"}), 401)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)


api.add_resource(Login, "/login")


class Logout(Resource):
    def delete(self):
        session.clear()
        return make_response(jsonify({"message": "Logged out"}), 200)


api.add_resource(Logout, "/logout")


class CheckSession(Resource):
    def get(self):
        if session.get("user_id"):
            user = db.session.get(User, session.get("user_id"))
            return make_response(jsonify(user.to_dict()), 200)
        return make_response(jsonify({"message": "No user logged in."}), 401)


api.add_resource(CheckSession, "/check-session")

# Aquarium routes


class AquariumResource(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        owner_id = data.get("owner_id")
        brand = data.get("brand")
        model = data.get("model")
        volume = data.get("volume")

        new_aquarium = Aquarium(
            owner_id=owner_id, brand=brand, model=model, volume=volume
        )

        db.session.add(new_aquarium)
        db.session.commit()
        return make_response(jsonify(new_aquarium.to_dict()), 201)


api.add_resource(AquariumResource, "/aquariums")


class AquariumByIdResource(Resource):
    def patch(self, id):
        data = request.get_json()
        aquarium = Aquarium.query.get(id)
        aquarium.brand = data.get("brand")
        aquarium.model = data.get("model")
        aquarium.volume = data.get("volume")
        db.session.commit()
        return make_response(jsonify(aquarium.to_dict()), 200)

    def delete(self, id):
        userAquariums = UserAquarium.query.filter_by(aquarium_id=id).all()
        aquarium = Aquarium.query.get(id)

        if userAquariums:
            for userAquarium in userAquariums:
                db.session.delete(userAquarium)

        db.session.delete(aquarium)
        db.session.commit()

        return make_response(jsonify({"message": "Aquarium deleted"}), 200)


api.add_resource(AquariumByIdResource, "/aquariums/<int:id>")


class WaterParameterResource(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        aquarium_id = data.get("aquarium_id")
        date_recorded = date.today().strftime("%Y-%m-%d")
        salinity = data.get("salinity")
        ph = data.get("ph")
        ammonia = data.get("ammonia")
        nitrate = data.get("nitrate")
        phosphate = data.get("phosphate")
        calcium = data.get("calcium")
        magnesium = data.get("magnesium")
        alkalinity = data.get("alkalinity")

        new_water_parameter = WaterParameter(
            aquarium_id=aquarium_id,
            date_recorded=date_recorded,
            salinity=salinity,
            ph=ph,
            ammonia=ammonia,
            nitrate=nitrate,
            phosphate=phosphate,
            calcium=calcium,
            magnesium=magnesium,
            alkalinity=alkalinity,
        )

        db.session.add(new_water_parameter)
        db.session.commit()
        return make_response(jsonify(new_water_parameter.to_dict()), 201)


api.add_resource(WaterParameterResource, "/water-parameters")


class PostResource(Resource):
    def get(self):
        posts = Post.query.all()
        return make_response(jsonify([post.to_dict() for post in posts]), 200)


api.add_resource(PostResource, "/posts")


class CommentsResource(Resource):
    def post(self):
        new_comment = Comment(
            user_id=request.json.get("user_id"),
            post_id=request.json.get("post_id"),
            content=request.json.get("content"),
        )
        db.session.add(new_comment)
        db.session.commit()
        return make_response(jsonify(new_comment.to_dict()), 201)


api.add_resource(CommentsResource, "/comments")
