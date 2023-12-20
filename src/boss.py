import threading
import time

import numpy as np

from queue_client import QueueClient
from task import Task


class Boss(QueueClient):
    def __init__(self, url: str, port: int, authkey: str, task_size: int = 10):
        super().__init__(url, port, authkey)
        self.task_size = task_size

    def read_result_queue(self):
        while True:
            task = self.get_task(self.result_queue)
            if task is None:
                continue

            res = np.linalg.norm(task.a @ task.x - task.b) < 1e-6
            print(f"Result for #{task.identifier}: {'valid' if res else 'invalid'}")

    def run(self):
        i = 1

        read_thread = threading.Thread(target=self.read_result_queue, daemon=True)
        read_thread.start()

        while True:
            task = Task(f"Task {i}", self.task_size)

            self.task_queue.put(task)
            i += 1
            time.sleep(0.5)


if __name__ == "__main__":
    import sys

    task_size = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    boss = Boss("localhost", 50000, b"abc123")
    boss.run()
