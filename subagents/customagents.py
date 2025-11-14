from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.agents.llm_agent import Agent



# Create an agent with google search tool as a search specialist
google_search_agent = Agent(
    model='gemini-2.5-flash',
    name='googlewiki_search_agent',
    instruction='Use google search or wiki to answer user questions about real-time, logistical information related to health care providers, hospitals and doctors info',
    tools=[google_search],
)
