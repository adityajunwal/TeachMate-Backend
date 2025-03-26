from fastapi import APIRouter, HTTPException
from routes.ChatApp.processPrompt import Conversation

chatRouter = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

chatManager = Conversation()
chatManager.generate_response("remember that there are 4 students, Abhishek, Pankaj, Aditya, Anjali and all are set to be absent for now")

@chatRouter.get("/")
def respond(prompt: str):

    response = chatManager.generate_response(prompt)

    if response :
        return {"message" : response}
    else:
        raise HTTPException(status_code=400, detail="Bad Request")
