from .auth import SignupApi, LoginApi
from .user import UsersApi, UserApi
from .character import CharactersApi, CharacterApi
from .chatbot import ChatbotsApi, ChatbotApi
from .conversation import ConversationsApi, ConversationApi
from .message import MessagesApi, MessageApi, RamdomMessageCharacter
from .topic import TopicsApi, TopicApi
from .knowledge import KnowledgesApi, KnowledgeApi



def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/user/<id>')

    api.add_resource(CharactersApi, '/api/characters')
    api.add_resource(CharacterApi, '/api/character/<id>')

    api.add_resource(ChatbotsApi, '/api/chatbots')
    api.add_resource(ChatbotApi, '/api/chatbot/<id>')

    api.add_resource(ConversationsApi, '/api/conversations')
    api.add_resource(ConversationApi, '/api/conversation/<id>')

    api.add_resource(MessagesApi, '/api/messages/<conversation_id>')
    api.add_resource(MessageApi, '/api/message/<id>')
    api.add_resource(RamdomMessageCharacter, '/api/random_message/<conversation_id>')

    api.add_resource(TopicsApi, '/api/topics')
    api.add_resource(TopicApi, '/api/topic/<id>')

    api.add_resource(KnowledgesApi, '/api/knowledges/<character_id>/<topic_id>')
    api.add_resource(KnowledgeApi, '/api/knowledge/<id>')