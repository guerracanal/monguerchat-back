from flask import Response, request
from database.models import Topic
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

class TopicsApi(Resource):
    def get(self):
        query = Topic.objects()
        topics = Topic.objects().to_json()
        return Response(topics, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        topic =  Topic(**body)
        topic.save()
        id = topic.id
        return {'id': str(id)}, 200
        
class TopicApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        print(body)
        Topic.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        topic = Topic.objects.get(id=id)
        topic.delete()
        return '', 200

    def get(self, id):
        topics = Topic.objects.get(id=id).to_json()
        return Response(topics, mimetype="application/json", status=200)