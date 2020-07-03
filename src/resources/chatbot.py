from flask import Response, request
from database.models import Chatbot
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class ChatbotsApi(Resource):
    def get(self):
        query = Chatbot.objects()
        chatbots = Chatbot.objects().to_json()
        return Response(chatbots, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        chatbot =  Chatbot(**body)
        chatbot.save()
        id = chatbot.id
        return {'id': str(id)}, 200
        
class ChatbotApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        print(body)
        Chatbot.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        chatbot = Chatbot.objects.get(id=id)
        chatbot.delete()
        return '', 200

    def get(self, id):
        chatbots = Chatbot.objects.get(id=id).to_json()
        return Response(chatbots, mimetype="application/json", status=200)