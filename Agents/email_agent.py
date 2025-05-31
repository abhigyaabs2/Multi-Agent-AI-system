from memory.redis_memory import RedisMemory
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def extract_sender(self, email_text):
        import re
        match = re.search(r"From: (.+)", email_text)
        return match.group(1).strip() if match else "unknown"

    def extract_urgency(self, email_text):
        if "urgent" in email_text.lower():
            return "High"
        return "Normal"

    def extract_intent(self, email_text):
        email_text = email_text.lower()
        if "invoice" in email_text:
            return "Invoice"
        elif "complaint" in email_text:
            return "Complaint"
        elif "rfq" in email_text:
            return "RFQ"
        elif "regulation" in email_text:
            return "Regulation"
        else:
            return "Other"


    def process(self, email_text, thread_id):
        sender = self.extract_sender(email_text)
        urgency = self.extract_urgency(email_text)
        intent = self.extract_intent(email_text)

        crm_format = {
            "sender": sender,
            "urgency": urgency,
            "intent": intent,
            "content": email_text
        }

       
        self.memory.log_event(thread_id, crm_format)

        return crm_format
