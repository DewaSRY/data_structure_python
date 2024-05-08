""" 

"""

from src.data_structure import MyTree
from unittest import TestCase
from dataclasses import dataclass, field


@dataclass
class ValueWrapper:
    value: int


class TestMyTree(TestCase):

    def setUp(self) -> None:
        self.tree = MyTree()

    def test_insert(self):
        num_list = [2, 1, 3]

        for n in num_list:
            self.tree.insert(value=n)

        current_root = self.tree.root
        assert current_root.value == 2
        assert current_root.left_node.value == 1
        assert current_root.right_node.value == 3

    def test_lookup(self):
        num_list = [2, 1, 3]

        for n in num_list:
            self.tree.insert(value=n)
        assert self.tree.lookup(value=1) == True
        assert self.tree.lookup(value=2) == True
        assert self.tree.lookup(value=3) == True

    def test_delete(self):
        num_list = [2, 1, 3]

        for n in num_list:
            self.tree.insert(value=n)
        self.tree.delete(1)
        assert self.tree.lookup(value=1) == False
        assert self.tree.lookup(value=2) == True
        assert self.tree.lookup(value=3) == True
