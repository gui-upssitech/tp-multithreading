import json
from time import perf_counter

import numpy as np


class Task:
    def __init__(self, identifier: str, size: int = 10):
        """Initializes a task with a random matrix A and vector B"""

        self.identifier = identifier
        self.size = size

        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)
        self.x = np.zeros((size, size))

        self.time = 0

    def work(self):
        """Time intensive function that finds X where A = X * B"""

        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = perf_counter() - start

    def to_json(self) -> str:
        return json.dumps(
            {
                "identifier": self.identifier,
                "size": self.size,
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "x": self.x.tolist(),
                "time": self.time,
            }
        )

    @classmethod
    def from_json(cls, json_str: str) -> "Task":
        obj = json.loads(json_str)
        task = Task("x")

        task.identifier = obj["identifier"]
        task.size = obj["size"]
        task.a = np.array(obj["a"])
        task.b = np.array(obj["b"])
        task.x = np.array(obj["x"])
        task.time = obj["time"]

        return task

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Task):
            return False

        task: Task = __value
        return (
            self.identifier == task.identifier
            and self.size == task.size
            and np.array_equal(self.a, task.a)
            and np.array_equal(self.b, task.b)
            and np.array_equal(self.x, task.x)
            and self.time == task.time
        )
