import os
import json
from memory.redis_memory import RedisMemory
from Agents.json_agent import JSONAgent
from Agents.email_agent import EmailAgent
from openai import OpenAI
from Utils.pdf_utils import extract_text_from_pdf
from dotenv import load_dotenv



load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

print("Your OpenAI API Key:", api_key)  


from openai import OpenAI
client = OpenAI(api_key=api_key)

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.json_agent = JSONAgent(memory)
        self.email_agent = EmailAgent(memory)

    def classify_format(self, raw_input):
        if raw_input.strip().startswith("{"):
            return "JSON"
        elif raw_input.strip().endswith(".pdf"):
            return "PDF"
        else:
            return "Email"

    def classify_intent(self, text):
    
        text_lower = text.lower()
        if "invoice" in text_lower:
            return "Invoice"
        elif "rfq" in text_lower:
            return "RFQ"
        elif "complaint" in text_lower:
            return "Complaint"
        elif "regulation" in text_lower:
            return "Regulation"
        else:
            return "Other"


    def route(self, raw_input, thread_id):
        format_type = self.classify_format(raw_input)

        if format_type == "PDF":
            content_text = extract_text_from_pdf(raw_input)
        else:
            content_text = raw_input

        intent = self.classify_intent(content_text)

        self.memory.log_event(thread_id, {"format": format_type, "intent": intent})

        if format_type == "JSON":
            result = self.json_agent.process(content_text, thread_id)
        elif format_type == "Email":
            result = self.email_agent.process(content_text, thread_id)
        elif format_type == "PDF":
            result = {"pdf_content": content_text}
        else:
            result = {"message": "Unknown format"}

        return result
