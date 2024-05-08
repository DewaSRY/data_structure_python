""" 
"""

from dataclasses import dataclass, field
from src.data_structure import LinkedList, LinkedListNode
from typing import Self, Union


def reverseLinkedList(linkedList: LinkedList) -> LinkedListNode:
    if linkedList.size <= 1:
        return linkedList
    reverse_node: Union[None, LinkedListNode] = None
    next_node: Union[None, LinkedListNode] = linkedList.tail

    while next_node != None:
        temp_node: LinkedListNode = next_node.next_node
        next_node.next_node = reverse_node
        reverse_node = next_node
        next_node = temp_node

    return reverse_node


def packingLinkedListNode(LinkedListNode: LinkedListNode) -> LinkedList:
    currentNode = LinkedListNode
    packingList = LinkedList()
    while currentNode != None:
        packingList.append(currentNode.value)
        currentNode = currentNode.next_node
    return packingList


""" 
leetcode inked list reverse
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"value {self.val} next {self.next}"


def reverseLinkedList_2(head: ListNode):
    reverse = None
    currentNode = head
    while currentNode != None:
        tempNode = currentNode.next
        currentNode.next = reverse
        reverse = currentNode
        currentNode = tempNode

    return reverse


def arrayToLinkedList(arr: list[int]):
    currentNode = ListNode()
    currentPointer = currentNode
    for n in range(len(arr)):

        if n < len(arr) - 1:
            currentPointer.next = ListNode()

        currentPointer.val = arr[n]
        currentPointer = currentPointer.next

    return currentNode


def linkedListToArray(head: ListNode):
    currentNode = head
    array = []
    while currentNode != None:
        array.append(currentNode.val)
        currentNode = currentNode.next

    return array


""" 
given a linked list and numbers m and n, and return it back with only m and n reverse
"""


def getNodeByIndex(head: ListNode, index: int):
    currentNode = head
    while index > 0:
        currentNode = currentNode.next
        index -= 1

    return currentNode


""" 

"""


def linkedListMAndNReverse(head: ListNode, M: int, N: int):

    mNode = getNodeByIndex(
        head=head, index=M - 2
    )  # mNode is the node before the M node, because se get the node by index, node Before M is Always on -2 Index, it s because the linked list node start from 1 node value

    currentMNode = mNode.next
    nextMNode = currentMNode.next

    loopLength = N - M
    for _ in range(loopLength):
        tempNode = nextMNode.next
        nextMNode.next = currentMNode
        currentMNode = nextMNode
        nextMNode = tempNode

    mNode.next = currentMNode
    nNode = getNodeByIndex(
        head=currentMNode, index=loopLength
    )  # take the new N node position which the previous M node
    nNode.next = nextMNode  # pointing the new N node to the rest node

    return head


""" 
marge Multi Level double linked list, 
Given a Doubly linked list, list nodes also have a child 
property that can point to separate double linked list. 
These child ist alo have one or more chid doubly lined list 
of their own, and so on. 

Return the list as a single level flattened doubly linked list
"""


@dataclass
class DoubleListNode(ListNode):
    val: int = field(default=0)
    next: Union[Self, None] = field(default=None)
    prev: Union[Self, None] = field(default=None)
    child: Union[Self, None] = field(default=None)


def nestedArrayToDoubleLinked(array: list[Union[list[int], int]], nestedLevel=1):
    nodeCreate = DoubleListNode()

    currentNode = nodeCreate
    currentPrev = None
    for n in range(len(array)):
        if n < len(array) - 1:
            newNode = DoubleListNode()
            currentNode.next = newNode
            newNode.prev = currentNode

        if type(array[n]) == list:
            currentNode = currentNode.prev
            currentNode.child = nestedArrayToDoubleLinked(
                array=array[n], nestedLevel=nestedLevel + 1
            )
            currentNode = currentNode.next
            if n == len(array) - 1:
                currentNode = currentNode.prev
                currentNode.next = None
        else:
            currentNode.val = array[n]
            currentNode.prev = currentPrev
            currentPrev = currentNode
            currentNode = currentNode.next
    return nodeCreate


def doubleListToArray(head: DoubleListNode):
    array = []
    currentNode = head
    while currentNode != None:
        array.append(currentNode.val)

        if currentNode.child != None:
            result = doubleListToArray(head=currentNode.child)
            array.append(result)
        currentNode = currentNode.next

    return array


def getTailNode(node: DoubleListNode):

    while node.next != None:
        node = node.next
    return node


def flatterDoubleLinkedList(head: DoubleListNode):
    headNode = head

    currentNode = headNode
    while currentNode != None:
        if currentNode.child != None:
            themChidNode = flatterDoubleLinkedList(head=currentNode.child)
            currentNode.child = None
            prevNextNode = currentNode.next
            currentNode.next = themChidNode
            currentTail = getTailNode(node=currentNode)
            currentTail.next = prevNextNode
        else:
            currentNode = currentNode.next

    return headNode


""" 
Cycle detection
"""


def createCycleNode(head: ListNode, index: int):
    tailNode = getTailNode(node=head)
    currentNode = head
    while index > 0:
        currentNode = currentNode.next
        index -= 1
    tailNode.next = currentNode
    return head


def nodeMove(node: ListNode, move: int):
    currentNode = node
    while move > 0:
        currentNode = currentNode.next
        move -= 1

    return currentNode


def nodeComparator(node_1: ListNode, node_2: ListNode):
    return node_1.val == node_2.val and node_1.next == node_2.next


def getCycleNode(startNode: ListNode, metingNode: ListNode) -> ListNode:
    node_1 = startNode
    node_2 = metingNode

    while nodeComparator(node_1=node_1, node_2=node_2) == False:
        node_1 = nodeMove(node_1, move=1)
        node_2 = nodeMove(node_2, move=1)

    return node_1


def cycleDetection(head: ListNode):
    tortoise = head
    floyd = head
    while tortoise != None and floyd != None:
        try:
            tortoise = nodeMove(node=tortoise, move=1)
            floyd = nodeMove(node=floyd, move=2)
        except Exception as e:
            break

        if nodeComparator(node_1=tortoise, node_2=floyd):
            return [True, getCycleNode(startNode=head, metingNode=tortoise).val]

    return [False, -1]
