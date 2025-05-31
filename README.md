#Multi-Agent AI Document Classifier
#Overview
This project is a multi-agent AI system designed to classify incoming documents (PDF, JSON, Email) based on format and intent, and route them to appropriate agents. It uses LLM-based classification and aims to support context tracking via Redis.

#Features Implemented
Input Format Classification: Detects whether input is a PDF, JSON, or Email.

Intent Classification: Uses OpenAI's GPT model to classify intent into:

Invoice

RFQ

Complaint

Regulation

Other

Routing Logic: Based on format and intent, routes input to relevant agents:

PDF Agent

JSON Agent

Email Agent

Basic Pipeline Testing: Successfully tested classification and routing pipeline.

#Planned Features (Pending Due to Time Constraints)
Context Memory (Redis): Intended to store thread-based memory using Redis.

Email Agent Details: Extraction of sender, urgency, intent, and CRM-compatible formatting.

JSON Schema Validation & anomaly detection.


#Requirements
Python 3.9+

openai, PyPDF2, redis, jsonschema, etc.

OpenAI API key

Redis 

