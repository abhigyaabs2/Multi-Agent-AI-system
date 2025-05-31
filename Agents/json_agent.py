import json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, raw_json, thread_id):
        try:
            data = json.loads(raw_json)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}

     
        required_fields = ["id", "type", "amount"]
        missing_fields = [f for f in required_fields if f not in data]

        anomaly_flag = len(missing_fields) > 0

        
        reformatted = {
            "invoice_id": data.get("id"),
            "invoice_type": data.get("type"),
            "total_amount": data.get("amount"),
        }

      
        self.memory.log_event(thread_id, {
            "processed_data": reformatted,
            "missing_fields": missing_fields,
            "anomaly": anomaly_flag
        })

        return {"status": "processed", "missing_fields": missing_fields, "reformatted": reformatted}
