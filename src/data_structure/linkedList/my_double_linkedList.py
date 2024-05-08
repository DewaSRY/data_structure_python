""" 

"""

from typing import Self, Union
from .my_linkedList import LinkedListNode, LinkedList


class DoubleNode(LinkedListNode):
    prev_node: Union[Self, None] = None

    def __init__(self, value: int) -> None:
        super().__init__(value=value)


class MyDoubleLinkedList(LinkedList):
    head: Union[None, DoubleNode] = None
    tail: Union[None, DoubleNode] = None
    size = 0

    def append(self, value: int):
        newNode = DoubleNode(value=value)
        if self.size == 0:
            self.tail = newNode
            self.head = newNode
        else:
            newNode.prev_node = self.head
            self.head.next_node = newNode
            self.head = newNode
        self.size += 1

    def insert(self, value: int, index: int):
        if index == 0:
            newNode = DoubleNode(value=value)
            newNode.next_node = self.tail
            self.tail = newNode
        elif index == self.size:
            self.append(value=value)
        else:
            newNode = DoubleNode(value=value)
            backNode = self._get_node(index=index - 1)
            frondPointer = backNode.next_node
            newNode.prev_node = backNode
            backNode.next_node = newNode
            newNode.next_node = frondPointer

        self.size += 1
