
from crewai import Crew, Task

# Import the individual agents
from agents.collector_agent import CollectorAgent
from agents.classifier_agent import ClassifierAgent
from agents.responder_agent import ResponderAgent
from agents.reviewer_agent import ReviewerAgent

# Simulated customer input
customer_message = "Hi, I was charged twice for my last order. Please fix this issue."

# 1. Task: Collector gathers and structures the query
collect_task = Task(
    agent=CollectorAgent,
    description=f"Receive this customer query and prepare it for classification: '{customer_message}'",
    expected_output="A clear summary of the issue extracted from the customer's message."
)

# 2. Task: Classifier categorizes the issue
classify_task = Task(
    agent=ClassifierAgent,
    description="Classify the issue into one of the following categories: Billing, Technical, or General "
                "based on the structured input.",
    expected_output="Category of the ticket and a short reason why it was classified that way.",
    context=[collect_task]
)

# 3. Task: Responder drafts a reply using classification
respond_task = Task(
    agent=ResponderAgent,
    description="Generate a support reply addressing the customer’s issue using the classified category.",
    expected_output="A helpful and professional draft response for the customer.",
    context=[classify_task]
)

# 4. Task: Reviewer improves tone and grammar
review_task = Task(
    agent=ReviewerAgent,
    description="Review and refine the draft response to ensure clarity, politeness, and professionalism.",
    expected_output="The final polished message to be sent to the customer.",
    context=[respond_task]
)

# Define the Crew that links all agents and tasks
crew = Crew(
    agents=[CollectorAgent, ClassifierAgent, ResponderAgent, ReviewerAgent],
    tasks=[collect_task, classify_task, respond_task, review_task],
    verbose=True  # Enable detailed logging in console
)

# Execute the multi-agent workflow using kickoff() instead of run()
result = crew.kickoff()

# Final output
print("\nFinal Reviewed Response to Customer:\n", result)
