from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

# class Movie(db.Document):
#     name = db.StringField(required=True, unique=True)
#     casts = db.ListField(db.StringField(), required=True)
#     genres = db.ListField(db.StringField(), required=True)
#     added_by = db.ReferenceField('User')

# User.register_delete_rule(Movie, 'added_by', db.CASCADE)

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    username = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Character(db.Document):
    name = db.StringField(required=True, unique=True)
    avatar = db.URLField(required=True)
    chatbot = db.ReferenceField('Chatbot')

class Conversation(db.Document):
    user = db.ReferenceField('User')
    character = db.ReferenceField('Character')

class Message(db.Document):
    content = db.StringField(required=True)
    time = db.DateTimeField(default=datetime.datetime.utcnow, required=True)
    conversation = db.ReferenceField('Conversation', required=True)
    sender_character = db.BooleanField(required=True)

class Chatbot(db.Document):
    name = db.StringField(required=True, unique=True)
    description = db.StringField()
    version = db.StringField()

class Topic(db.Document):
    name = db.StringField(required=True, unique=True)
    triggers = db.ListField(db.StringField(), required=True)

# class Trigger(db.Document):
#     pattern
    
class Knowledge(db.Document):
    character = db.ReferenceField('Character')
    content = db.StringField(required=True)
    topic = db.ReferenceField('Topic')

class Search(db.Document):
    name = db.StringField(required=True, unique=True)
    url_api = db.URLField(required=True)
