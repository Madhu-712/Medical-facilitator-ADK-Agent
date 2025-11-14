from google.adk.agents.llm_agent import Agent

from google.genai import types
from google.adk.tools.agent_tool import AgentTool

from .subagents.data_retriver_agent import data_retriver_agent
from .subagents.medical_facilitator_agent import medical_facilitator_agent
from .prompt import PROMPT
from .tools import store_pdf

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction= PROMPT,
    generate_content_config=types.GenerateContentConfig(temperature=0.2),

   tools=[
        AgentTool(agent=data_retriver_agent),
        AgentTool(agent=medical_facilitator_agent),
        store_pdf,
        
    ],
)
