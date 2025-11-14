import google.cloud.aiplatform as aiplatform
from google import genai
from google.genai import types
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path
import warnings
import os
import logging
import base64
#import fitz

env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

warnings.filterwarnings("ignore")
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
logger = logging.getLogger(__name__)



def extract_patientinfo(patientsinfo_file: str,Patientid: str) -> str:
    """
    Extracts all information related to a specific patient by patient id from patientsinfo pdf
    using the Gemini model.

    Args:
        patientsinfo_file: The full text of the patients info pdf doc
        Patient ID: The ID associated with patient

    Returns:
        Relevant information about the patient asked in user query or a message indicating it's not found.
    """
    client = genai.Client(
        vertexai=True,
        project=GOOGLE_CLOUD_PROJECT,
        location=GOOGLE_CLOUD_LOCATION,
    )

    
    # with open(policy_file_path, 'rb') as pdf_file:
    #     pdf_bytes = pdf_file.read()

    

    # Define the text part of the prompt
    prompt_text = types.Part.from_text(text=f"""
    You are an AI assistant specialized in analyzing patientsinfo by fetching relevant details from the patientsinfo pdf document path(/home/madhu_712/medagent/subagents/data/patientsinfo.pdf).
    Given the following patientsinfo text, extract relevant details present in the file regarding patient info,medical history,consultation, diagnosis 
    and surgical interventions.

    If "{Patientid}"is not explicitly mentioned or no information
    is found regarding it, state "No specific information found for {Patientid}.
    
    patientsinfo-file text: {patientsinfo_file}""")

    model = "gemini-2.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                prompt_text
            ]
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        top_p = 0.95,
        max_output_tokens = 65535,
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
    )

    summary_output = ""
    # Stream the content generation
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
    ):
        summary_output += chunk.text
    return summary_output

DATA_EXTRACTOR_INSTRUCTION = """
    You are a information extractor agent that helps with extracting 
    details about patient from user request. You will have below information to extract from /home/madhu_712/medagent/subagents/data/patientsinfo.pdf  document.
    1) patient name 
    2) patient id
    3) consultation details
    4) diagnosis info
    5) surgical procedures
    6) medical history
    """


from google.genai import types
from google.adk import Agent




data_retriver_agent = Agent(
   model='gemini-2.5-flash',
   name="data_retriver",
   description="""Agent that reviews the patients info from the pdf doc and retrives the specific content about patient mentioned in the query.""",
   instruction= DATA_EXTRACTOR_INSTRUCTION,
   generate_content_config=types.GenerateContentConfig(temperature=0.0),
   tools=[extract_patientinfo],
   
)
