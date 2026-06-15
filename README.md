# 🤖 Multi-Agent Sales Assistant AI

An intelligent multi-agent AI system designed to assist sales representatives in managing customer interactions, visit tracking, follow-ups, and activity summaries within a sales management platform.

This project was integrated into a sales tracking application used by field sales representatives to automate note analysis, generate visit summaries, and provide intelligent follow-up recommendations using a collaborative AI agent architecture.

---

# 🚀 Features

### 🤖 Multi-Agent Architecture

The system uses specialized AI agents that collaborate to handle different sales-related tasks.

* General Agent for handling user queries.
* Follow-Up Agent for generating actionable next steps.
* Summary Agent for creating concise visit summaries.
* Supervisor Agent for intelligent task routing.

### 📋 Sales Visit Intelligence

* Analyze salesperson notes.
* Extract key discussion points.
* Generate structured meeting summaries.
* Identify customer requirements and concerns.

### 📞 Automated Follow-Up Suggestions

* Recommend next actions after customer visits.
* Generate follow-up reminders.
* Improve sales workflow efficiency.

### 🧠 Intelligent Agent Routing

* Queries are automatically routed to the most suitable agent.
* Supervisor coordinates agent collaboration.
* Optimized multi-agent decision-making workflow.

### ⚡ Redis Caching

* Response caching using Redis.
* Reduced LLM response latency.
* Improved scalability and performance.
* Lower AI inference costs.

### 🔄 Real-Time Processing

* Fast API responses.
* Efficient workflow execution.
* Optimized agent communication.

---

# 🏗️ Architecture

```text
Salesperson Input
       │
       ▼
  Supervisor Agent
       │
 ┌─────┼─────┐
 │     │     │
 ▼     ▼     ▼
General Follow-Up Summary
Agent    Agent    Agent
 │        │        │
 └─────┬──┴──┬─────┘
       ▼
 Redis Cache
       ▼
 Final Response
```

---

# 🧩 AI Agents

## 1. General Agent

Responsible for:

* Answering user questions.
* Understanding sales context.
* Providing customer-related insights.

## 2. Follow-Up Agent

Responsible for:

* Creating follow-up recommendations.
* Identifying pending actions.
* Suggesting next customer engagement steps.

## 3. Summary Agent

Responsible for:

* Summarizing sales visit notes.
* Extracting key information.
* Generating concise reports.

## 4. Supervisor Agent

Responsible for:

* Agent orchestration.
* Query classification.
* Workflow coordination.
* Multi-agent routing.

---

# ⚙️ Tech Stack

## Backend

* Python
* FastAPI

## AI Stack

* LangGraph
* LangChain
* LLM Integration
* Agent-Based Workflows

## Performance Layer

* Redis
* Response Caching

## Database

* SQL Database Integration

---

# 🔍 Workflow

### Step 1

Sales representative submits visit notes or asks a question.

### Step 2

Supervisor Agent analyzes the request.

### Step 3

Request is routed to the appropriate specialized agent.

### Step 4

Agent processes the information.

### Step 5

Redis checks for cached responses.

### Step 6

Final response is returned to the application.

---

# 🎯 Key Engineering Highlights

* Multi-Agent AI Architecture.
* Agent Orchestration and Routing.
* Redis-Based Response Caching.
* Production-Ready Backend Design.
* Modular Agent Development.
* Scalable Workflow Architecture.
* Intelligent Task Delegation.
* Enterprise Sales Automation.

---

# 💼 Business Impact

The AI assistant helps sales teams by:

* Reducing manual note processing.
* Automating meeting summaries.
* Improving follow-up consistency.
* Enhancing customer engagement.
* Increasing salesperson productivity.
* Delivering actionable sales insights.

---

# 📂 Project Structure

```text
agents/
├── general_agent.py
├── followup_agent.py
└── summary_agent.py

cache.py
db.py
graph.py
main.py
supervisor.py
test_redis.py
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/Ronak-Malik/multiagent-sales-assistant.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

```env
OPENAI_API_KEY=
REDIS_URL=
DATABASE_URL=
```

## Run Application

```bash
python main.py
```

---



⭐ If you found this project useful, consider giving it a star on GitHub.
