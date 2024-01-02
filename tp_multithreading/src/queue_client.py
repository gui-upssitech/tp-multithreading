import multiprocessing as mp

from queue_manager import QueueManager
from task import Task


class QueueClient:
    def __init__(self):
        self.qm = QueueManager("localhost", 50000, b"abc123")
        self.qm.connect()

        self.qm.register("get_task_queue")
        self.qm.register("get_result_queue")

        self.task_queue: mp.Queue = self.qm.get_task_queue()
        self.result_queue: mp.Queue = self.qm.get_result_queue()

    def get_task(self, queue: mp.Queue) -> Task | None:
        item = queue.get()
        return item if isinstance(item, Task) else None


if __name__ == "__main__":
    qc = QueueClient()
    print(qc.task_queue)
