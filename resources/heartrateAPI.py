from flask import Flask, jsonify, request
from flask import Response, request
from database.models import User
from flask_restful import Resource
from flask_jwt_extended import jwt_required

app = Flask(__name__)

heart = [{'heart_id': 0, 'date': 'November 2022', 'heart_rate': 85}]

class HeartRateAPI(Resource):

    def get(self):
        return jsonify(heart)
    

    @jwt_required()
    def post(self):
        heartrate = request.get_json()
        heartrate['heart_id'] = len(heart)
        heart.append(heartrate)
        return {'id': len(heart)}

class HeartAPI(Resource):
    def get(self, id):
        heartrate = [heartrate for heartrate in heart if heartrate['heart_id'] == id]
        return jsonify(heartrate)

    @jwt_required()
    def put(self, id):
        heartrate = [heartrate for heartrate in heart if heartrate['heart_id'] == id]
        for key, value in enumerate(heart):
            if value[heart_id] == id:
                heart[key] = request.get_json
        return 'Heart information successfully updated.', 200      

    @jwt_required()
    def delete(self, id):
        heartrate = [heartrate for heartrate in heart if heartrate['heart_id'] == id]
        heart.remove(heartrate[0])
        return 'Heart information successfully deleted.', 200

if __name__ == '__main__':
    app.run()


    