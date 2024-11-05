from services import ConversationService
from mock_repo import MockConversationRepository

def test_list_conversations():
    conversation_service = ConversationService(MockConversationRepository(2)) 
    conversations = [conversation.normalize() for conversation in conversation_service.list(chat_id=2)]
    assert len(conversations) == 1
    assert conversations[0]['chat_id'] == 2
    assert conversations[0]['message_counter'] == 1
    assert conversations[0]['message_text'] == "Hello"