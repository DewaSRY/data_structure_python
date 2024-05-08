"""_summary_
"""

# from typing import
from .linear_data import LinearData, LinearNode


class MyStack(LinearData):

    def push(self, value: int):
        newNode = LinearNode(value=value)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.setNextNode(newNode)
            self.head = newNode

        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            tempNode = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return tempNode.value
        else:
            temp = self.head
            prev_index = self.size - 1
            self.head = self._getNode(index=prev_index)
            self.size -= 1
            return temp.value

    def peek(self) -> int:
        return self.head.value
