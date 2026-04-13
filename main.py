from graph import graph
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# 🔥 Load .env file
load_dotenv()

# 🔥 Get API key from env
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY not found in environment variables")

# 🔥 Your test salesman ID
USER_ID = "iPr3xaUi9DXQruUtefalaDVkAJH2"

# 🔥 Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

def main():

    config = {
        "configurable": {
            "thread_id": USER_ID
        }
    }

    print("🤖 Sales AI Chatbot (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        response = graph.invoke({
            "input": query,
            "user_id": USER_ID,
            "llm": llm
        }, config=config)

        print("Bot:", response["response"])
        print("-" * 50)

if __name__ == "__main__":
    main()