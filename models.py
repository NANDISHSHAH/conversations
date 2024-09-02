from database import Base


class Conversation(Base):
    __tablename__ = 'conversations'

    chat_id = Column(Integer, primary_key=True, index=True)
    message_counter = Column(Integer, primary_key=True)
    message_text = Column(String)
