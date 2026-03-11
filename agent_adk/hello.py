from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {
        "status": "success",
        "city": city,
        "time": "10:30 AM"
    }

# Create agent
root_agent = Agent(
    model="gemini-1.5-flash",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant that tells the current time in cities. "
        "Use the 'get_current_time' tool for this purpose."
    ),
    tools=[get_current_time],
)

# ✅ Create session service
session_service = InMemorySessionService()

# ✅ Create runner with session service
runner = Runner(session_service=session_service)

# ✅ Run agent
response = runner.run(
    agent=root_agent,
    input="What is the current time in Delhi?"
)

print(response)