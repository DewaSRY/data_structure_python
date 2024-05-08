from unittest import TestCase

from src.data_structure import LinkedListNode, LinkedList
from src.linkedList_question import (
    reverseLinkedList,
    packingLinkedListNode,
    arrayToLinkedList,
    linkedListToArray,
    reverseLinkedList_2,
    linkedListMAndNReverse,
    nestedArrayToDoubleLinked,
    flatterDoubleLinkedList,
    doubleListToArray,
    createCycleNode,
    cycleDetection,
)
from pprint import pprint


class TestFirst(TestCase):
    def setUp(self) -> None:
        self.linkedList = LinkedList()
        for n in range(4):
            self.linkedList.append(n)

    def test_reverseLinkedList(self):
        newReverseList = packingLinkedListNode(
            LinkedListNode=reverseLinkedList(linkedList=self.linkedList)
        )

        assert newReverseList.at(0) == 3
        assert newReverseList.at(1) == 2
        assert newReverseList.at(2) == 1
        assert newReverseList.at(3) == 0

    def test_reverseLinkedList_2(self):
        nodes = arrayToLinkedList(arr=[5, 4, 3, 2, 1])
        reverseNode = reverseLinkedList_2(head=nodes)
        actualReverse = linkedListToArray(head=reverseNode)
        assert actualReverse == [1, 2, 3, 4, 5]

    def test_linkedListMAndNReverse(self):
        nodes = arrayToLinkedList(arr=[1, 2, 3, 4, 5, 6, 7])
        actualNode = linkedListMAndNReverse(head=nodes, M=3, N=5)
        actualArray = linkedListToArray(head=actualNode)

        assert actualArray == [1, 2, 5, 4, 3, 6, 7]

    def test_linkedListMAndNReverse_two(self):
        nodes = arrayToLinkedList(arr=[1, 2, 3, 4, 5])
        actualNode = linkedListMAndNReverse(head=nodes, M=2, N=4)
        actualArray = linkedListToArray(head=actualNode)

        assert actualArray == [1, 4, 3, 2, 5]

    def test_createNestedDoubleLinkedList(self):
        nestedList = [1, 2, [3, [4, 5], 6, [7, 8]]]
        doubleLInkedList = nestedArrayToDoubleLinked(array=nestedList)
        doubleArray = doubleListToArray(head=doubleLInkedList)
        assert doubleArray == nestedList

    def test_flatterDoubleLinkedList(self):
        nestedList = [1, 2, [3, [4, 5], 6, [7, 8]]]
        doubleLInkedList = nestedArrayToDoubleLinked(array=nestedList)
        flatterList = flatterDoubleLinkedList(head=doubleLInkedList)

        flatterArray = doubleListToArray(head=flatterList)
        assert flatterArray == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_cycleList(self):
        linkedList = arrayToLinkedList(arr=[0, 1, 2, 3, 4, 5, 6])
        isCycle, nodeIndex = cycleDetection(head=linkedList)
        assert isCycle == False
        assert nodeIndex == -1

        createCycleNode(head=linkedList, index=3)
        isCycle, nodeIndex = cycleDetection(head=linkedList)
        assert isCycle == True
        assert nodeIndex == 3
