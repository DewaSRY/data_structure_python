""" 
"""

from unittest import TestCase
from src.data_structure import MyStack


class TestMyStack(TestCase):
    def setUp(self) -> None:
        self.stack = MyStack()

    def test_push(self):
        for n in range(5):
            self.stack.push(n)
        for n in range(5):
            assert self.stack.at(n) == n

    def test_pop(self):
        for n in range(5):
            self.stack.push(n)
        for n in range(5):
            assert self.stack.pop() == 4 - n
