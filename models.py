from sqlalchemy import (
    Column,
    Integer,
    String,
)

from database import Base


class Conversation(Base):
    __tablename__ = 'conversations'

    chat_id = Column(Integer, primary_key=True, index=True)
    message_counter = Column(Integer, primary_key=True)
    message_text = Column(String)

    def normalize(self):
        return {
            'chat_id': self.chat_id,
            'message_counter': self.message_counter,
            'message_text': self.message_text,
        }
