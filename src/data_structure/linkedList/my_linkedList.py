"""_summary_
"""

from typing import Self, Union


class LinkedListNode:
    value: int
    next_node: Union[Self, None] = None

    def __init__(self, value: int) -> None:
        self.value = value


class LinkedList:
    tail: Union[LinkedListNode, None] = None
    head: Union[LinkedListNode, None] = None
    size = 0

    def append(self, value: int):
        newNode = LinkedListNode(value=value)

        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.head.next_node = newNode
            self.head = newNode
        self.size += 1

    def insert(self, value: int, index: int):
        if index == 0:
            newNode = LinkedListNode(value=value)
            newNode.next_node = self.tail
            self.tail = newNode
        elif index == self.size:
            self.append(value=value)
        else:
            newNode = LinkedListNode(value=value)
            backNode = self._get_node(index=index - 1)
            currentNode = self._get_node(index=index)
            newNode.next_node = currentNode
            backNode.next_node = newNode
        self.size += 1

    def delete(self, index: int):
        try:
            self._check_index(index=index)
        except Exception as s:
            raise s
        if index == 0:
            self.tail = self.tail.next_node
        if index == self.size - 1:
            back_node = self._get_node(index=index - 1)
            back_node.next_node = None
        else:
            back_node = self._get_node(index=index - 1)
            next_node = self._get_node(index=index + 1)
            back_node.next_node = next_node
        self.size -= 1

    def at(self, index: int) -> int:
        try:
            self._check_index(index=index)
            return self._get_node(index=index).value
        except Exception as e:
            raise e

    def _get_node(self, index: int) -> LinkedListNode:
        currentNode = self.tail
        while index != 0:
            currentNode = currentNode.next_node
            index -= 1
        return currentNode

    def _check_index(self, index: int):
        if index < 0 and index > self.size - 1:
            raise Exception(f"index out of bond")
