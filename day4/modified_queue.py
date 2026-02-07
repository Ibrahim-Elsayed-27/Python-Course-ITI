from queue import queue
from custom_queue_exception import QueueOutOfRangeException
import json
class modified_queue(queue):
    all_ques = {}
    def __init__(self,id, max_size):
        super().__init__()
        self.max_size = max_size
        modified_queue.all_ques[id] = self
        

    def enqueue(self, item):
        if self.size() == self.max_size:
            raise QueueOutOfRangeException("Queue has reached its maximum size")
        super().enqueue(item)
    def is_full(self):
        return self.size() == self.max_size

    def get_items(self):
        return self.items
    
    @classmethod
    def save(cls):
        data = {}
        for id, queue_instance in cls.all_ques.items():
            data[id] = {
                'max_size': queue_instance.max_size,
                'items': queue_instance.get_items()
            }
        with open('queues_data.json', 'w') as f:
            json.dump(data, f)

    @classmethod
    def load(cls):
        try:
            with open('queues_data.json', 'r') as f:
                data = json.load(f)
                for id, queue_data in data.items():
                    queue_instance = cls(id, queue_data['max_size'])
                    for item in queue_data['items']:
                        queue_instance.enqueue(item)
        except FileNotFoundError:
            pass