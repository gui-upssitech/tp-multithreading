import unittest

from tp_multithreading.src.task import Task


class TestTask(unittest.TestCase):
    def test_json(self):
        task_a = Task("Task 1", 50)
        task_a.work()

        task_a_json = task_a.to_json()

        task_b = Task.from_json(task_a_json)
        print(task_a == task_b)

        self.assertEqual(task_a, task_b)


if __name__ == "__main__":
    unittest.main()
