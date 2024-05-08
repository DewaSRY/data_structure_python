""" 
"""

from unittest import TestCase
from src.data_structure import MyDoubleLinkedList


class TestMyDoubleLinkedList(TestCase):

    def setUp(self) -> None:
        self.linkedList = MyDoubleLinkedList()

    def tearDown(self) -> None:
        self.linkedList = MyDoubleLinkedList()

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
