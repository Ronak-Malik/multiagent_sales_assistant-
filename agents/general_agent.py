def general_agent(state):
    query = state["input"]
    llm = state["llm"]

    prompt = f"""
You are a professional AI assistant for a sales application.

Rules:
1. ONLY answer sales-related questions (clients, meetings, deals, performance).
2. If the question is NOT related to sales:
   → Respond politely that you can only assist with sales-related queries.
3. If the query involves manager, escalation, complaint, or authority:
   → Respond: "Please contact your manager for this request."

User Query:
{query}

Respond professionally.
"""

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }