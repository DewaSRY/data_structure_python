""" 
"""

from unittest import TestCase
from src.data_structure import LinkedList


class TestLinkedList(TestCase):

    def setUp(self) -> None:
        self.linkedList = LinkedList()

    def tearDown(self) -> None:
        self.linkedList = LinkedList()

    def test_append_one(self):
        linkedList = LinkedList()
        for n in range(10):
            linkedList.append(n)

        assert linkedList.at(0) == 0
        assert linkedList.at(1) == 1
        assert linkedList.at(2) == 2
        assert linkedList.at(3) == 3
        assert linkedList.at(4) == 4

        for n in range(10):
            linkedList.at(n) == n

    def test_append(self):
        self.linkedList.append(1)
        self.linkedList.append(2)

        assert (self.linkedList.at(0)) == 1
        assert (self.linkedList.at(1)) == 2

    def test_insert(self):
        self.linkedList.append(1)
        self.linkedList.append(3)
        self.linkedList.insert(value=2, index=1)
        assert (self.linkedList.at(0)) == 1
        assert (self.linkedList.at(1)) == 2
        assert (self.linkedList.at(2)) == 3

    def test_delete(self):
        self.linkedList.append(1)
        self.linkedList.append(2)
        self.linkedList.append(3)
        self.linkedList.delete(1)
        assert (self.linkedList.at(0)) == 1
        assert (self.linkedList.at(1)) == 3
