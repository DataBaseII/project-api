from flask import jsonify, Response
from bson.objectid import ObjectId
from bson import json_util
from utils.constants import *
from utils.helpers import *

# Post Category
def save_category(mongo, request):
    name = get_field(request, "name")
    if name:
        body = {"name": name}
        _id = mongo.db.genres.insert_one({**body})
        response = jsonify({"_id": str(_id.inserted_id), **body})
        response.status_code = CREATED_CODE
        return response
    else:
        return error(request)


# Get All Categories
def get_all_categories(mongo):
    categories = mongo.db.genres.find()
    response = json_util.dumps(categories)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Get Category by ID
def get_category_by_id(mongo, id):
    category = mongo.db.genres.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(category)
    response = remove_oid(response)
    return Response(response, mimetype="application/json")


# Delete Category by ID
def delete_category_by_id(mongo, id):
    categoryDeleted = mongo.db.genres.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "Category " + id + " Deleted Successfully"})
    response.status_code = 200
    return response


# Update Category by ID
def update_category_by_id(mongo, request, id):
    name = get_field(request, "name")
    body = {
        "name": name,
    }
    _id = mongo.db.genres.update_one({"_id": ObjectId(id)}, {"$set": {**body}})
    if _id.modified_count == 1:
        response = jsonify({"_id": id, **body})
        response.status_code = OK
        return response
    else:
        return error(request)
