from fastapi import Depends, FastAPI

from schema import ConversationSchema
from services import ConversationService

app = FastAPI()


@app.get('/conversations/{chat_id}', response_model=list[ConversationSchema])
async def get_list(
    chat_id: int,
    conversation_service: ConversationService = Depends(),
) -> list[ConversationSchema]:
    return [
        conversation.normalize()
        for conversation in conversation_service.list(chat_id)
    ]
