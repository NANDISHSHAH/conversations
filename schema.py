from pydantic import BaseModel


class ConversationSchema(BaseModel):
    chat_id: int
    message_counter: int
    message_text: str
