from flask import Response, request
from database.models import Conversation, Character, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class ConversationsApi(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        print(user_id)
        user = User.objects.get(id=user_id)
        query = Conversation.objects()
        conversations = Conversation.objects(user=user.id).to_json()
        return Response(conversations, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        user_id = get_jwt_identity()
        character_id = str(body["character"])
        character = Character.objects.get(id=character_id)
        user = User.objects.get(id=user_id)
        conversation =  Conversation()
        conversation.character = character
        conversation.user = user
        conversation.save()
        id = conversation.id
        return {'id': str(id)}, 200
        
class ConversationApi(Resource):
    @jwt_required
    def put(self, id):
        users_id = get_jwt_identity()
        conversation = Conversation.objects.get(id=id)
        body = request.get_json()
        Conversation.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        conversation = Conversation.objects.get(id=id)
        conversation.delete()
        return '', 200

    def get(self, id):
        conversations = Conversation.objects.get(id=id).to_json()
        return Response(conversations, mimetype="application/json", status=200)