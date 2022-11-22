import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

server = Flask(__name__)
server.config['MONGO_URI'] = "mongodb://localhost:27017/videos"

mongo = PyMongo(server)

# Store big data in GridFS (videos)
fs = gridfs.GridFS(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

@server.route('/login', methods=['POST'])
def login():
    token, err = access.login(request)

    if not err:
        return token, 200
    else:
        return err

@server.route('/upload', methods=['POST'])
def upload():
    access, err = validate.token(request)

    access = json.loads(access)

    if access["admin"]:
        if len(request.files) > 1 or len(request.files) < 1:
            return "exactly 1 file required", 400
        
        for _, f in request.files.items():
            err = util.upload(f, fs, channel, access)

            if err:
                return err, 400

        return "success", 200
    else:
        return "unauthorized", 401

@server.route('/download', methods=['GET'])
def download():
    pass

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080)