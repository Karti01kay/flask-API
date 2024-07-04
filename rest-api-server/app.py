import os
from flask import Flask, Response, request, jsonify, make_response
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

load_dotenv()

app = Flask(__name__)
mongo_db_url = os.environ.get("MONGO_DB_CONN_STRING")

client = MongoClient(mongo_db_url)
db = client['users_db']

@app.get("/api/users")
def get_users():
    user_id = request.args.get('user_id')
    filter = {} if user_id is None else {"user_id": user_id}
    users = list(db.users.find(filter))

    response = Response(
        response=dumps(users), status=200,  mimetype="application/json")
    return response

@app.post("/api/users")
def add_user():
    _json = request.json
    db.users.insert_one(_json)

    resp = jsonify({"message": "User added successfully"})
    resp.status_code = 200
    return resp


@app.delete("/api/users/<id>")
def delete_user(id):
    db.users.delete_one({'_id': ObjectId(id)})

    resp = jsonify({"message": "User deleted successfully"})
    resp.status_code = 200
    return resp 

@app.put("/api/users/<id>")
def update_user(id):
    _json = request.json
    db.users.update_one({'_id': ObjectId(id)}, {"$set": _json})

    resp = jsonify({"message": "User updated successfully"})
    resp.status_code = 200
    return resp

@app.errorhandler(400)
def handle_400_error(error):
    return make_response(jsonify({"errorCode": error.code, 
                                  "errorDescription": "Bad request!",
                                  "errorDetailedDescription": error.description,
                                  "errorName": error.name}), 400)

@app.errorhandler(404)
def handle_404_error(error):
        return make_response(jsonify({"errorCode": error.code, 
                                  "errorDescription": "Resource not found!",
                                  "errorDetailedDescription": error.description,
                                  "errorName": error.name}), 404)

@app.errorhandler(500)
def handle_500_error(error):
        return make_response(jsonify({"errorCode": error.code, 
                                  "errorDescription": "Internal Server Error",
                                  "errorDetailedDescription": error.description,
                                  "errorName": error.name}), 500)