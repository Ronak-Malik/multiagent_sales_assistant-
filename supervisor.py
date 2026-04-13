from pydantic import BaseModel
from enum import Enum

class AgentEnum(str, Enum):
    SUMMARY = "summary_agent"
    FOLLOWUP = "followup_agent"
    GENERAL = "general_agent"

class TimeEnum(str, Enum):
    TODAY = "today"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

class Router(BaseModel):
    agent: AgentEnum
    time_range: TimeEnum

def supervisor_node(state):
    query = state["input"]
    llm = state["llm"]

    router_llm = llm.with_structured_output(Router)

    prompt = f"""
You are an intelligent routing system for a sales assistant AI.

Analyze the user query and decide:

1. Which agent should handle it:
   - summary_agent → performance, reports, stats
   - followup_agent → meetings, reminders, followups
   - general_agent → anything else

2. Extract time range:
   - today
   - weekly
   - monthly
   - default to weekly if not specified

User Query:
{query}

Respond ONLY in structured format.
"""

    try:
        decision = router_llm.invoke(prompt)
        print(f"🧠 ROUTER DECISION → {decision}")

        return {
            **state,  # 🔥 VERY IMPORTANT (preserve state)
            "agent": decision.agent.value,
            "time_range": decision.time_range.value
        }

    except Exception as e:
        print("⚠️ Router fallback triggered:", e)

        # 🔥 Safe fallback (production safety)
        return {
            **state,
            "agent": "general_agent",
            "time_range": "weekly"
        }