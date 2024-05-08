""" 

"""

from .linear_data import LinearData, LinearNode


class MyQueue(LinearData):

    def enqueue(self, value: int):
        newNode = LinearNode(value=value)
        if self.size == -1:
            self.tail = newNode
            self.head = newNode
        else:
            self.head.setNextNode(newNode)
            self.head = newNode
        self.size += 1

    def dequeue(self) -> int:
        if self.size == 0:
            tempNode = self.tail
            self.tail = None
            self.head = None
            self.size -= 1
            return tempNode.value
        else:
            tempNode = self.tail
            self.tail = tempNode.next_node
            self.size -= 1
            return tempNode.value
