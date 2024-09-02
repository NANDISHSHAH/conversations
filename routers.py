from fastapi import FastAPI

app = FastAPI()

@app.get("/conversations")
async def index():
    return {"Hello": "World"}
