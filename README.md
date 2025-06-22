
# 🧠 Multi-Agent Customer Support Ticket Resolution System

This project simulates a team of AI agents working together to process and respond to a customer support request. Built using [CrewAI](https://github.com/joaomdmoura/crewAI), the system models a real-world customer support workflow with distinct roles, message passing, and clear outputs.

## 📌 Objective
Automate the process of responding to customer queries using multiple AI agents that collaborate in a step-by-step pipeline.

## 👥 Agent Roles

| Agent | Role |
|-------|------|
| **Collector Agent** | Receives the customer query and structures it for processing |
| **Classifier Agent** | Tags the issue (Billing, Technical, or General) |
| **Responder Agent** | Drafts a professional reply using the classified data |
| **Reviewer Agent** | Reviews and polishes the message for clarity and tone |

## 🔄 Workflow
Customer Message → Collector → Classifier → Responder → Reviewer → Final Response

## 🛠️ How to Run

### ✅ Requirements
- Python 3.8+
- OpenAI API Key
- Install dependencies:
```bash
pip install crewai openai
```

### ▶️ Run the Agent Workflow
```bash
python main.py
```

## 📁 Project Structure
customer_support_agents/
├── main.py
├── agents/
│   ├── collector_agent.py
│   ├── classifier_agent.py
│   ├── responder_agent.py
│   └── reviewer_agent.py
├── utils/
│   └── tools.py
├── logs/
│   └── run_log.txt
├── diagram.png
└── README.md

## 📈 Enhancements Ideas
- Add SentimentAgent for escalation
- Plug into a real support platform or ticketing UI
- Add retrieval-augmented generation for KB responses
- Log agent decisions in real-time using AgentOps
