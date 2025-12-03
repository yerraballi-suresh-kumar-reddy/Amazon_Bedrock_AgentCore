from strands import Agent
from strands.tools import tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from datetime import datetime, timezone, timedelta

# -------------------------------------------------------
# Utility functions
# -------------------------------------------------------

def get_ist_time():
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

def extract_output(result):
    return result.message if hasattr(result, "message") else str(result)


# -------------------------------------------------------
# Bedrock Agent Core App
# -------------------------------------------------------
app = BedrockAgentCoreApp()


# -------------------------------------------------------
# Tool: Research Assistant
# -------------------------------------------------------
@tool
def research_assistant(query: str) -> str:
    try:
        agent = Agent(
            system_prompt=f"""
            You are a research assistant.
            Provide factual, verified information only.
            IST Time: {get_ist_time()}
            """
        )
        result = agent(query)
        return extract_output(result)

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------------------------------------
# Tool: Product Recommendation
# -------------------------------------------------------
@tool
def product_recommendation_assistant(query: str) -> str:
    try:
        agent = Agent(
            system_prompt=f"""
            You are a product recommendation expert.
            Give all prices in INR.
            IST Time: {get_ist_time()}
            """
        )
        result = agent(query)
        return extract_output(result)

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------------------------------------
# Tool: Trip Planner
# -------------------------------------------------------
@tool
def trip_planning_assistant(query: str) -> str:
    try:
        agent = Agent(
            system_prompt=f"""
            You are a travel expert.
            Provide seasonal and practical recommendations.
            IST Time: {get_ist_time()}
            """
        )
        result = agent(query)
        return extract_output(result)

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------------------------------------
# Orchestrator Agent (Main Router)
# -------------------------------------------------------
MAIN_SYSTEM_PROMPT = """
You are an orchestration agent.
Your job is to pick the correct tool based on user intent:

- Research or factual questions      → research_assistant
- Product or pricing queries         → product_recommendation_assistant
- Travel plans, trips, itineraries   → trip_planning_assistant
"""

orchestrator = Agent(
    system_prompt=MAIN_SYSTEM_PROMPT,
    tools=[
        research_assistant,
        product_recommendation_assistant,
        trip_planning_assistant
    ]
)


# -------------------------------------------------------
# Entrypoint for Amazon Bedrock Agent Core
# -------------------------------------------------------
@app.entrypoint
def invoke(payload):
    try:
        user_message = payload.get("prompt", "")
        print(f"Received request: {user_message}")

        if not user_message:
            return {"error": "Missing 'prompt' in payload"}

        result = orchestrator(user_message)
        response = extract_output(result)

        return {
            "response": response,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "model": "strands-orchestrator"
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"error": str(e)}


# -------------------------------------------------------
# Local Dev Mode
# -------------------------------------------------------
if __name__ == "__main__":
    print("Starting Bedrock Agent Core App...")
    print("Agent is ready.")
    app.run()
 
