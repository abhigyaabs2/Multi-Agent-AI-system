import redis
import json
from datetime import datetime

class RedisMemory:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def log_event(self, thread_id, data):
        """
        Log a memory entry for a given thread or conversation.
        Appends to a list so all steps can be traced.
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            **data
        }

        existing = self.client.get(thread_id)
        if existing:
            history = json.loads(existing)
        else:
            history = []

        history.append(log_entry)
        self.client.set(thread_id, json.dumps(history, indent=2))

    def get_history(self, thread_id):
        """
        Fetch full memory log for a thread.
        """
        data = self.client.get(thread_id)
        if data:
            return json.loads(data)
        return []

    def clear_memory(self, thread_id=None):
        """
        Clear memory for a specific thread or all.
        """
        if thread_id:
            self.client.delete(thread_id)
        else:
            self.client.flushdb()
