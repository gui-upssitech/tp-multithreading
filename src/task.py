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
