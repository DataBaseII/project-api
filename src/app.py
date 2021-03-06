from flask import Flask, request, Response
from flask_pymongo import PyMongo
from services.user_service import *
from services.movie_service import *
from services.category_service import *
from utils.constants import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = DB_URI
mongo = PyMongo(app)

# USERS
# POST -> Crear
@app.route(USERS_PATH, methods=["POST"])
def create_users():
    response = save_user(mongo, request)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# GET -> Obtener
@app.route(USERS_PATH, methods=["GET"])
def get_users():
    response = get_all_users(mongo)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# GET -> Obtener by ID
@app.route(USERS_PATH + ID, methods=["GET"])
def get_user(id):
    response = get_user_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# DELETE -> Eliminar by ID
@app.route(USERS_PATH + ID, methods=["DELETE"])
def delete_user(id):
    response = delete_user_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# PUT -> Actualizar by ID
@app.route(USERS_PATH + ID, methods=["PUT"])
def update_user(id):
    response = update_user_by_id(mongo, request, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# MOVIES
@app.route(MOVIES_PATH, methods=["POST"])
def create_movie():
    response = save_movie(mongo, request)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH, methods=["GET"])
def get_movies():
    response = get_all_movies(mongo)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH + ID, methods=["GET"])
def get_movie(id):
    response = get_movie_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH + ID, methods=["DELETE"])
def delete_movie(id):
    response = delete_movie_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(MOVIES_PATH + ID, methods=["PUT"])
def update_movie(id):
    response = update_movie_by_id(mongo, request, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# CATEGORIES
@app.route(CATEGORIES_PATH, methods=["POST"])
def create_category():
    response = save_category(mongo, request)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(CATEGORIES_PATH, methods=["GET"])
def get_categories():
    response = get_all_categories(mongo)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(CATEGORIES_PATH + ID, methods=["GET"])
def get_category(id):
    response = get_category_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(CATEGORIES_PATH + ID, methods=["DELETE"])
def delete_category(id):
    response = delete_category_by_id(mongo, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route(CATEGORIES_PATH + ID, methods=["PUT"])
def update_category(id):
    response = update_category_by_id(mongo, request, id)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
