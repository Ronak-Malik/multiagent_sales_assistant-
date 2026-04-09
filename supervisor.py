# supervisor.py
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

    llm = state["llm"].with_structured_output(Router)

    prompt = f"""
    Route this query:

    Query: {query}

    Rules:
    - Summary → performance, report
    - Followup → meetings, reminders
    - General → other

    Extract time:
    today / weekly / monthly
    """

    decision = llm.invoke(prompt)

    return {
        "agent": decision.agent.value,
        "time_range": decision.time_range.value
    }