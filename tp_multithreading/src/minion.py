from queue_client import QueueClient
from task import Task


class Minion(QueueClient):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            task: Task = self.get_task(self.task_queue)
            if task is None:
                continue

            print(f"Received #{task.identifier}")
            task.work()
            print(f"Finished #{task.identifier} in {task.time} seconds")

            self.result_queue.put(task)


if __name__ == "__main__":
    minion = Minion()
    minion.run()
