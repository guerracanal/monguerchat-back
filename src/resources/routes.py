from .auth import SignupApi, LoginApi
from .user import UsersApi, UserApi
from .character import CharactersApi, CharacterApi
from .chatbot import ChatbotsApi, ChatbotApi


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/user/<id>')

    api.add_resource(CharactersApi, '/api/characters')
    api.add_resource(CharacterApi, '/api/character/<id>')

    api.add_resource(ChatbotsApi, '/api/chatbots')
    api.add_resource(ChatbotApi, '/api/chatbot/<id>')