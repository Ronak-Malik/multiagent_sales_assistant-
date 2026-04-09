from fastapi import FastAPI
from graph import graph
from langchain_groq import ChatGroq 

app = FastAPI()

llm = ChatGroq(model="llama-3.1-8b-instant") 

@app.post("/chat")
def chat(user_id: str, message: str):

    config = {
        "configurable": {
            "thread_id": user_id
        }
    }

    response = graph.invoke({
        "input": message,
        "user_id": user_id,
        "llm": llm
    }, config=config)

    return {"response": response["response"]}