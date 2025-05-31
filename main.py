import os
from Agents.classifier_agent import ClassifierAgent
from memory.redis_memory import RedisMemory

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_pipeline():
    memory = RedisMemory()
    classifier = ClassifierAgent(memory)

    # --- Email Test ---
    email_path = "sample_inputs/sample_email.txt"
    email_content = load_file(email_path)
    print("Testing Email:")
    print(classifier.route(email_content, thread_id="thread-email"))

    # --- JSON Test ---
    json_path = "sample_inputs/sample_data.json"
    json_content = load_file(json_path)
    print("\nTesting JSON:")
    print(classifier.route(json_content, thread_id="thread-json"))

    # --- PDF Test ---
    pdf_path = "sample_inputs/sample_invoice.pdf"
    print("\nTesting PDF:")
    print(classifier.route(pdf_path, thread_id="thread-pdf"))

if __name__ == "__main__":
    test_pipeline()
