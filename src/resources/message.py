from flask import Response, request
from database.models import Message, Conversation, User, Character, Knowledge
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import random

class MessagesApi(Resource):

    def get(self, conversation_id):
        conversation = Conversation.objects.get(id=conversation_id)
        query = Message.objects()
        print("Id: "+conversation_id)
        messages = Message.objects(conversation=conversation.id).to_json()
        return Response(messages, mimetype="application/json", status=200)

    @jwt_required
    def post(self, conversation_id):
        body = request.get_json()
        user_id = get_jwt_identity()
        conversation = Conversation.objects.get(id=conversation_id)
        user = User.objects.get(id=user_id)
        message =  Message(**body)
        message.conversation = conversation
        message.save()
        id = message.id
        return {'id': str(id)}, 200
        
class MessageApi(Resource):
    @jwt_required
    def put(self, id):
        users_id = get_jwt_identity()
        message = Message.objects.get(id=id)
        body = request.get_json()
        Message.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        message = Message.objects.get(id=id)
        message.delete()
        return '', 200

    def get(self, id):
        messages = Message.objects.get(id=id).to_json()
        return Response(messages, mimetype="application/json", status=200)

class RamdomMessageCharacter(Resource):
    
    def post(self, conversation_id):
        conversation = Conversation.objects.get(id=conversation_id)
        query = Message.objects()
        character = Character.objects.get(id=conversation.character.id)

        query = Knowledge.objects()

        knowledges = Knowledge.objects(character=conversation.character.id)

        ramdom_message = []

        for i in range(0,random.randint(1, 10)):
            ramdom_message.append(knowledges[random.randrange(len(knowledges))].content+' ')

        message =  Message()
        message.content = ''.join(ramdom_message).strip()
        message.conversation = conversation
        message.sender_character = True
        message.save()
        return Response(message.to_json(), mimetype="application/json", status=200)