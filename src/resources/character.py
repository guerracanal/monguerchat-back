from flask import Response, request
from database.models import Character
from database.models import Chatbot
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from bson.objectid import ObjectId

class CharactersApi(Resource):
    def get(self):
        query = Character.objects()
        characters = Character.objects().to_json()
        return Response(characters, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        chatbot_id = str(body["chatbot"])
        print(chatbot_id)
        chatbot = Chatbot.objects.get(id=chatbot_id)
        character =  Character(**body)
        character.chatbot = chatbot
        character.save()
        id = character.id
        return {'id': str(id)}, 200
        
class CharacterApi(Resource):
    @jwt_required
    def put(self, id):
        users_id = get_jwt_identity()
        character = Character.objects.get(id=id, added_by=users_id)
        body = request.get_json()
        Character.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        character = Character.objects.get(id=id)
        character.delete()
        return '', 200

    def get(self, id):
        characters = Character.objects.get(id=id).to_json()
        return Response(characters, mimetype="application/json", status=200)