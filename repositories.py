from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_connection
from models import Conversation


class ConversationRepository:
    db: Session

    def __init__(
            self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(self, chat_id: int) -> list[Conversation]:
        """Get the history of a conversation with a user from
        the chat_id."""
        query = self.db.query(Conversation).filter(
            Conversation.chat_id == chat_id)
        return query.all()

