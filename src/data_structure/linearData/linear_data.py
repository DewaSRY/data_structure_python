from typing import Union, Self
from dataclasses import dataclass


@dataclass
class LinearNode:
    value: int
    next_node: Union[None, Self] = None

    def __init__(self, value: int) -> None:
        self.value = value

    def setNextNode(self, nextNode: Self):
        self.next_node = nextNode


class LinearData:
    head: Union[None, LinearNode] = None
    tail: Union[None, LinearNode] = None
    size = -1

    def at(self, index: int) -> int:
        try:
            return self._getNode(index=index).value
        except Exception as e:
            raise e

    def _getNode(self, index: int) -> LinearNode:
        if self._check_index(index=index):
            raise Exception(f"index out of bonds")
        current_node: LinearNode = self.tail
        while index != 0:
            current_node = current_node.next_node
            index -= 1
        return current_node

    def _check_index(self, index: int) -> bool:
        return index < 0 and index > (self.size)
