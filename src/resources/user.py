from flask import Response, request
from database.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class UsersApi(Resource):
    def get(self):
        query = User.objects()
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        user =  User(**body, added_by=user)
        user.save()
        user.update(push__movies=user)
        user.save()
        id = user.id
        return {'id': str(id)}, 200
        
class UserApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        User.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        user = User.objects.get(id=id, added_by=user_id)
        user.delete()
        return '', 200

    def get(self, id):
        users = User.objects.get(id=id).to_json()
        return Response(users, mimetype="application/json", status=200)