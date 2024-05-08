""" 

"""

from src.tree_question import (
    TreeNode,
    breadthFirstSearch,
    depthFirstSearch_inOrder,
    depthFirstSearch_postOrder,
    depthFirstSearch_preOrder,
    maxDepthOfTree,
    levelOrderTree,
    iterativeLevelOrder,
    seeRightSideOfTree,
    numberOfNodeInCompleteTree,
)
from unittest import TestCase
from typing import Callable


class TestTreeQuestion(TestCase):

    def setUp(self) -> None:
        self.myTree = TreeNode(value=9)
        insertList = [6, 12, 1, 4, 34, 45]
        for n in insertList:
            self.myTree.insert(value=n)
        # print()
        # print(myTree.toString())

    def test_breadthFirstSearch(self):
        collectValue = breadthFirstSearch(head=self.myTree)
        assert collectValue == [9, 6, 12, 1, 34, 4, 45]

    def test_depthFirstSearch_inOrder(self):
        collectValue = depthFirstSearch_inOrder(head=self.myTree)
        assert collectValue == [1, 4, 6, 9, 12, 34, 45]

    def test_depthFirstSearch_preOrder(self):
        collectValue = depthFirstSearch_preOrder(head=self.myTree)
        assert collectValue == [9, 6, 1, 4, 12, 34, 45]

    def test_depthFirstSearch_postOrder(self):
        collectValue = depthFirstSearch_postOrder(head=self.myTree)
        assert collectValue == [4, 1, 6, 45, 34, 12, 9]

    def test_maxDepthOfTree(self):
        for n in [2, 3, 5, 7, 8, 10, 11]:
            self.myTree.insert(n)
        actual = maxDepthOfTree(head=self.myTree)
        # print(actual)
        # print(self.myTree.toString())
        assert actual == 6

    def test_levelOrderTree(self):
        for n in [2, 3, 5, 7, 8, 10, 11]:
            self.myTree.insert(n)
        actual = levelOrderTree(head=self.myTree)
        # print(actual)
        # print(self.myTree.toString())
        assert actual == [[9], [6, 12], [1, 7, 10, 34], [4, 8, 11, 45], [2, 5], [3]]

    def test_iterativeLevelOrder(self):
        for n in [2, 3, 5, 7, 8, 10, 11]:
            self.myTree.insert(n)
        actual = iterativeLevelOrder(head=self.myTree)
        # print(actual)
        # print(self.myTree.toString())
        assert actual == [[9], [6, 12], [1, 7, 10, 34], [4, 8, 11, 45], [2, 5], [3]]

    def test_rightSideTree(self):
        for n in [2, 3, 5, 7, 8, 10, 11]:
            self.myTree.insert(n)
        actual = seeRightSideOfTree(head=self.myTree)
        # print(actual)
        # print(self.myTree.toString())
        assert actual == [9, 12, 34, 45, 5, 3]

    def test_numberOfNodeInCompleteTree(self):
        for n in [2, 3, 5, 7, 8, 10, 11]:
            self.myTree.insert(n)
        actual = numberOfNodeInCompleteTree(head=self.myTree)
        # print(self.myTree.toString())
        assert actual == 9

    def test_callable(self):
        compareFunction: Callable[[int, int], bool] = (
            lambda value_1, value_2: value_1 > value_2
        )

        assert compareFunction(4, 2) == True
