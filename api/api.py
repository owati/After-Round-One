from flask import Blueprint, request, jsonify
import uuid
import json
from models.game import Game
from redis_code.main import redis_connection
import redis


api_bp = Blueprint("api_bp", __name__)
connection : redis.Redis  = redis_connection()


@api_bp.post("/create")
def create_game():
    print(request.headers)
    creator = request.headers.get('token') if request.headers.get('token') else str(uuid.uuid4()) 
    body = request.get_json()
    try:
        num = body["num"]
        if num < 1 or num > 4:
            num = 4
        _id , data = Game(str(uuid.uuid4()), {
            "_id" : creator,
            "name" : body["name"]
        }, max_players=num).serialize()
        print("data")
        if connection.set(_id, json.dumps(data)):
            print("data")
            return jsonify({
                "message" : "The game was created successfully",
                "data" : {
                    "id" : _id,
                    "num" : num,
                    "token" : creator
                }
            }), 201
        else:
            return jsonify({
                "message" : "The game was not created"
            }), 400
    except Exception as e:
        if e == KeyError:
            return jsonify({
                "message" : "The schema of the data is not correct"
            }), 422
        return jsonify({
            "message" : "An error occured in the server"
        }), 500
        


@api_bp.delete("/<int:id>")
def delete_game(id):
    if connection.delete(id) == 1:
        return jsonify({
            "message" : "The game was deleted successfully"
        }), 200
    return jsonify({
        "message" : "The game delete was not successful"
    }), 400
