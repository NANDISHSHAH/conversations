from fastapi import Depends

from models import Conversation
from repositories import ConversationRepository
from sqlalchemy.orm import Session
from database import get_db_connection

#shared a logic between services and repositories it can depend on the database 
def get_conversation_repository(db: Session = Depends(get_db_connection)) -> ConversationRepository:
    return ConversationRepository(db)

class ConversationService:
    conversation_repo: ConversationRepository

    def __init__(
            self,
            conversation_repo: ConversationRepository = Depends(get_conversation_repository),
    ) -> None:
        self.conversation_repo = conversation_repo

    def list(self, chat_id: int) -> list[Conversation]:
        return self.conversation_repo.list(chat_id)
