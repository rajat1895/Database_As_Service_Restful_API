"""
Registration of user - 0 tokens
Each user gets 10 tokens
Store a sentence on our database for 1 token
Retrieve his stored sentence on our database for 1 token
"""
import certifi
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)
db_url = ""
client = MongoClient(db_url, tlsCAFile=certifi.where())
db = client.mydb
users = db["Users"]


class Register(Resource):
    def post(self):
        # Step1 get posted data by the user
        postedData = request.get_json()

        # Get the data
        username = postedData["username"]
        password = postedData["password"]  # 123xyz

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # store username and password into the database
        # users.insert({
        #    "Username": username,
        #    "Password": hashed_pw,
        #    "Sentence": "",
        #    "Tokens": 6
        #  })

        users.insert_one({"Username": username, "Password": hashed_pw, "Sentence": "", "Tokens": 6})

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)


def verifyPw(username, password):
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False


def countTokens(username):
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens


class Store(Resource):
    def post(self):
        # Step 1 get the posted data
        postedData = request.get_json()

        # Step 2 is to read the data
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        # Step 3 verify the username password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)

        # Step 4 Verify user has enough tokens
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # Step 5 store the sentence, take one token away and return 200OK
        users.update_one({
            "Username": username},
            {
                "$set": {
                    "Sentence": sentence,
                    "Tokens": num_tokens - 1
                }
            })

        retJson = {
            "status": 200,
            "msg": "Sentence saved successfully"
        }
        return jsonify(retJson)


class Get(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        # step 3 verify the username pw match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)
        sentence = users.find({
            "Username": username
        })[0]["Sentence"]

        retJson = {
            "status": 200,
            "sentence": sentence
        }

        return jsonify(retJson)

        # MAKE THE USER PAY!
        users.update_one({
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens - 1
            }
        })


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
