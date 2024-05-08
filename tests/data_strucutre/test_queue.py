""" 
"""

from unittest import TestCase
from src.data_structure import MyQueue


class TestMyQueue(TestCase):
    def setUp(self) -> None:
        self.queue = MyQueue()

    def test_queue(self):
        for n in range(5):
            self.queue.enqueue(n)
        for n in range(5):
            assert self.queue.at(n) == n

    def test_dequeue(self):
        for n in range(5):
            self.queue.enqueue(n)
        for n in range(5):
            assert self.queue.dequeue() == n
