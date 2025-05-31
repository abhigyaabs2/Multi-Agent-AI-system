import openai
import re

def classify_email_intent_urgency(text):
    prompt = f"""
    Analyze this email and provide:
    - intent (e.g., RFQ, Complaint, Invoice, Regulation)
    - urgency (Low, Medium, High)
    
    Email:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}]
    )

    output = response['choices'][0]['message']['content']
    intent_match = re.search(r"intent:\s*(.*)", output, re.IGNORECASE)
    urgency_match = re.search(r"urgency:\s*(.*)", output, re.IGNORECASE)

    return (
        intent_match.group(1).strip() if intent_match else "Unknown",
        urgency_match.group(1).strip() if urgency_match else "Unknown"
    )
