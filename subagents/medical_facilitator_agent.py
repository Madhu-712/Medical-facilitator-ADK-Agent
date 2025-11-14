from google.genai import types
from google.adk import Agent
import os
from serpapi import GoogleSearch
from .customagents import google_search_agent
from google.adk.tools.agent_tool import AgentTool


def serpapi(query: str) -> dict:
    """
    Performs a Google search using SerpApi and returns the structured JSON results.

    Args:
        query (str): The search query string.

    Returns:
        dict: A dictionary containing the structured search results.
              Returns an empty dictionary if the API key is missing or search fails.
    """
    api_key = os.getenv("SERPAPI_API_KEY")

    if not api_key:
        print("Error: SERPAPI_API_KEY environment variable not set.")
        return {}

    try:
        params = {
            "engine": "google",
            "q": query,
            "api_key": api_key,
            "hl": "en",
            "gl": "us"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


FACILITATOR_INSTRUCTION = """
Act like a medical facilitator agent having following responsibilities and give comprehensive suggestions to 
all user query.

Key roles and responsibilities-
1.Patient advocacy: They act as a patient's trusted guide and advocate throughout their treatment journey.
2.Logistics coordination: They arrange and manage travel logistics, including flights, accommodation, and local transportation.
3.Medical liaison: They help patients connect with the right specialists and coordinate appointments.
4.Administrative support: They handle the transfer of medical records, liaise with doctors and hospital staff, and sometimes manage payments.
5.Personalized support: They can assist with language interpretation and post-treatment care arrangements.
6.Package creation: They may create comprehensive packages that include medical, travel, and lodging expenses. 


How you should work-
1.Bridge between patient and provider: They serve as a vital link between an international patient and a healthcare provider in another country.
2.Concierge for traveling patients: Their role is often compared to that of a concierge for patients traveling abroad for medical treatment.
3.Network and partnerships: They work with a network of hospitals, doctors, and other service providers to create packages and manage the patient's care.
4.Service-based model: Some facilitators work on a service fee model, transparently showing the costs of services to the client. 

 """


medical_facilitator_agent = Agent(
   model='gemini-2.5-flash',
   name="med_facilitator_agent",
   description="""Agent that provide confidential one-on-one assistance in connecting patients with their healthcare providers.
   Facilitators are qualified to work in a wide range of settings, including hospitals, doctors' offices, insurance company call centers, and more.""",
   instruction= FACILITATOR_INSTRUCTION,
   generate_content_config=types.GenerateContentConfig(temperature=0.2),
  
   tools=[serpapi,
    AgentTool(agent=google_search_agent)]
   
)
