from models import Conversation
class MockConversationRepository:


    def __init__(
            self,
            chat_id: int,
    ) -> None:
        pass
    def list(self,chat_id:int) -> list[Conversation]:
        return [Conversation(chat_id=2, message_counter=1, message_text="Hello")]
       