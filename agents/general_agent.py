# agents/general_agent.py
def general_agent(state):
    query = state["input"]

    return {
        "response": f"General response: {query}\nIf needed contact your manager."
    }