# graph.py
from langgraph.graph import StateGraph
from agents.summary_agent import summary_agent
from agents.followup_agent import followup_agent
from agents.general_agent import general_agent
from supervisor import supervisor_node
from langgraph.checkpoint import MemorySaver

builder = StateGraph(dict)

builder.add_node("supervisor", supervisor_node)
builder.add_node("summary_agent", summary_agent)
builder.add_node("followup_agent", followup_agent)
builder.add_node("general_agent", general_agent)

builder.set_entry_point("supervisor")

builder.add_conditional_edges(
    "supervisor",
    lambda x: x["agent"],
    {
        "summary_agent": "summary_agent",
        "followup_agent": "followup_agent",
        "general_agent": "general_agent"
    }
)

checkpointer = MemorySaver()

graph = builder.compile(checkpointer=checkpointer)