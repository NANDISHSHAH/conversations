from database import BaseModel


class ConversationPostRequestSchema(BaseModel):
    chat_id: int
    message_text: str


class ConversationSchema(ConversationPostRequestSchema):
    message_counter: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
