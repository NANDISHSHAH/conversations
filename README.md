# Conversations
### Instructions to run
```commandline
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ fastapi dev
```
An endpoint to retrieve the conversation history
from the chat_id `http://localhost:8000/conversations/{chat_id}`

Example request:
```commandline
curl http://localhost:8000/conversations/2
```
to get the conversation history of chat_id 2
