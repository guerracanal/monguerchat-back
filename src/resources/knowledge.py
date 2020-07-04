from flask import Response, request
from database.models import Knowledge, Character
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class KnowledgesApi(Resource):
    def get(self, character_id, topic_id):
        query = Knowledge.objects()
        knowledges = Knowledge.objects(character=character_id).to_json()
        return Response(knowledges, mimetype="application/json", status=200)

    def post(self, character_id, topic_id):
        body = request.get_json()

        if isinstance(body["content"], list):
            content = body["content"]
            for x in range(0,len(content)):
                print(content[x])
                knowledge =  Knowledge()
                character = Character.objects.get(id=character_id)
                # topic = Character.objects.get(id=topic_id)
                knowledge.character = character
                knowledge.content = content[x]
                # knowledge.topic = topic
                knowledge.save()
                knowledge.id
            return {'content': str(content)}, 200

        else:
            knowledge =  Knowledge(**body)
            knowledge.save()
            id = knowledge.id
            return {'id': str(id)}, 200
        
class KnowledgeApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        print(body)
        Knowledge.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        knowledge = Knowledge.objects.get(id=id)
        knowledge.delete()
        return '', 200

    def get(self, id):
        knowledges = Knowledge.objects.get(id=id).to_json()
        return Response(knowledges, mimetype="application/json", status=200)