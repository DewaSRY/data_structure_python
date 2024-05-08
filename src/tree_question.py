""" 

"""

from typing import Self, Union, Callable


class TreeNode:
    left_node: Union[Self, None] = None
    right_node: Union[Self, None] = None
    value: int = -1

    def __init__(self, value: int) -> None:
        self.value = value

    def insert(self, value: int):
        newNode = TreeNode(value=value)
        self._insert(node=newNode)

    def _insert(self, node: Self):
        if self._compare(node=node):
            if self._hasLeft():
                self.left_node._insert(node=node)
            else:
                self.left_node = node
        else:
            if self._hasRight():
                self.right_node._insert(node=node)
            else:
                self.right_node = node

    def toString(self, dept: int = 0) -> str:
        leftSide = ""
        rightSide = ""
        if self._hasLeft():
            leftSide = "left: " + self.left_node.toString(dept=dept + 1)
        if self._hasRight():
            rightSide = "right: " + self.right_node.toString(dept=dept + 1)
        return f"""
    {"+"* dept}> value: {self.value}
    {"  "* dept } {leftSide}
    {"  "* dept } {rightSide}"""

    def _compare(self, node: Self) -> bool:
        return self.value > node.value

    def _hasLeft(self) -> bool:
        return self.left_node != None

    def _hasRight(self) -> bool:
        return self.right_node != None


""" 
birth first search

"""


def fillStackWithNode(currentNode: TreeNode, stack: list[TreeNode]) -> list[TreeNode]:
    if currentNode._hasLeft():
        stack.append(currentNode.left_node)
    if currentNode._hasRight():
        stack.append(currentNode.right_node)

    return stack


def breadthFirstSearch(head: TreeNode):
    stackNode = [head]
    valueCollector = []
    while len(stackNode) > 0:
        currentNode = stackNode.pop(0)  # return the first value
        stackNode = fillStackWithNode(currentNode=currentNode, stack=stackNode)
        valueCollector.append(currentNode.value)

    return valueCollector


""" 
depth first search
"""


def depthFirstSearch_inOrder(head: TreeNode, values: list[int] = []):
    if head._hasLeft():
        depthFirstSearch_inOrder(head=head.left_node, values=values)

    values.append(head.value)
    if head._hasRight():
        depthFirstSearch_inOrder(head=head.right_node, values=values)

    return values


def depthFirstSearch_preOrder(head: TreeNode, values: list[int] = []):
    values.append(head.value)

    if head._hasLeft():
        depthFirstSearch_preOrder(head=head.left_node, values=values)
    if head._hasRight():
        depthFirstSearch_preOrder(head=head.right_node, values=values)

    return values


def depthFirstSearch_postOrder(head: TreeNode, values: list[int] = []):
    if head._hasLeft():
        depthFirstSearch_postOrder(head=head.left_node, values=values)

    if head._hasRight():
        depthFirstSearch_postOrder(head=head.right_node, values=values)

    values.append(head.value)
    return values


""" 
Maximum Depth of tree
"""


def greaterVal(value_1: int, value_2: int):
    return value_1 if value_1 >= value_2 else value_2


def maxDepthOfTree(head: TreeNode, depth=0, maxDepth=0):
    maxDepth = greaterVal(value_1=depth, value_2=maxDepth)
    if head == None:
        return maxDepth
    return greaterVal(
        value_1=maxDepthOfTree(
            head=head.right_node,
            depth=depth + 1,
            maxDepth=maxDepth,
        ),
        value_2=maxDepthOfTree(
            head=head.left_node,
            depth=depth + 1,
            maxDepth=maxDepth,
        ),
    )


""" 
Level order of binary tree 
Given a binary tree, return the level order traversal of the nodes value as an array
"""


def levelOrderTree(
    head: TreeNode, currentLevel: int = None, listNode: list[list[int]] = [[]]
) -> list[list[int]]:
    currentLevel = currentLevel if currentLevel != None else 0
    if currentLevel > len(listNode) - 1:
        listNode.append([])

    listCurrentLevel = listNode[currentLevel]
    listCurrentLevel.append(head.value)
    # print
    if head._hasLeft():
        levelOrderTree(
            head=head.left_node, currentLevel=currentLevel + 1, listNode=listNode
        )
    if head._hasRight():
        levelOrderTree(
            head=head.right_node, currentLevel=currentLevel + 1, listNode=listNode
        )

    return listNode


def _fillTheQueue(currentNode: TreeNode, queue: list[TreeNode]):
    if currentNode._hasLeft():
        queue.append(currentNode.left_node)
    if currentNode._hasRight():
        queue.append(currentNode.right_node)

    return queue


def iterativeLevelOrder(head: TreeNode) -> list[list[int]]:
    if head == None:
        return []
    result: list[list[int]] = []
    queue = [head]
    while len(queue) > 0:
        currentLevel: list[int] = []
        queLength = len(queue)
        count = 0
        while count < queLength:
            currentNode = queue.pop(0)
            currentLevel.append(currentNode.value)
            queue = _fillTheQueue(currentNode=currentNode, queue=queue)
            count += 1

        result.append(currentLevel)

    return result


""" 
Given a binary tree, imagine you're standing to the right of the tree. Return an array of the values f the nodes you can see ordered from top to bottom 
"""


def seeRightSideOfTree(
    head: TreeNode, currentLevel=0, nodeList: list[int] = []
) -> list[int]:
    if currentLevel > len(nodeList) - 1:
        nodeList.append(head.value)
    # print(f"current level is {currentLevel}")
    if head._hasRight():
        seeRightSideOfTree(
            head=head.right_node, currentLevel=currentLevel + 1, nodeList=nodeList
        )

    if head._hasLeft():
        seeRightSideOfTree(
            head=head.left_node, currentLevel=currentLevel + 1, nodeList=nodeList
        )

    return nodeList


def fillTheQueue(currentNode: TreeNode, queue: list[int]):
    if currentNode._hasLeft():
        queue.append(currentNode.left_node)
    if currentNode._hasRight():
        queue.append(currentNode.right_node)
    return queue


# def seeRightSideOfTree_bfs(head: TreeNode):
#     result = []
#     currentLevel = 0
#     queue = [head]
#     countNode = 0
#     while len(queue) > 0:
#         currentNode = queue.pop(0)
#         queue = fillTheQueue(currentNode=currentNode, queue=queue)

#         if currentLevel > len(result) - 1:
#             result.append(currentNode.value)

#     return result


""" 
Number of node in Complete tree
"""


def isCompleteTree(currentNode: TreeNode):
    case_one = currentNode._hasLeft() and currentNode._hasRight()
    case_two = currentNode.left_node == None and currentNode.right_node == None
    return case_one or case_two


def numberOfNodeInCompleteTree(head: TreeNode, countNode=[0]):

    if isCompleteTree(currentNode=head):
        countNode[0] = countNode[0] + 1

    if head._hasLeft():
        numberOfNodeInCompleteTree(head=head.left_node, countNode=countNode)
    if head._hasRight():
        numberOfNodeInCompleteTree(head=head.right_node, countNode=countNode)

    return countNode[0]


""" 
Given perfect binary tree, count the node of the three,
- first we already know three is complete tree
- the perfect three is the tree with full node on the every level except for the last level 
- every level of the tree have value of 2^ n-1 ~ >  n = node level 
- then the relationship for the prev level to the next level is next_level = sum all prevLevel node
- we can conclude for the perfect binary tree the count of upper level node is (2^ h-1) - 1 
- the the we can count all the total node of the tree with formula upper_node + rest_node => ( (2^h-1) - 1 ) + rest_node
- the probability ov the amount of the rest_node is min = 1, and max == upper_node
"""
import math


def getTreeHight(head: TreeNode) -> int:
    height = 0
    while head._hasLeft():
        head = head.left_node
        height += 1

    return height


def nodeExists(indexToFind: int, height: int, node: TreeNode) -> bool:
    left = 0
    right = math.pow(2, height) - 1
    count = 0
    while count < height:
        midOfNode = math.ceil((left + right) / 2)
        if indexToFind >= midOfNode:
            node = node.right_node
            left = midOfNode
        else:
            node = node.left_node
            right = midOfNode - 1

    count += 1

    return node != None


def countNode(head: TreeNode):
    if head == None:
        return 0
    height = getTreeHight(head=head)
    if height == 0:
        return 1
    upperCount = math.pow(2, height) - 1
    left = 0
    right = upperCount
    while left < right:
        indexToFind = math.ceil((left + right) / 2)
        if nodeExists(indexToFind=indexToFind, height=height, node=head):
            left = indexToFind
        else:
            right = indexToFind - 1

    return upperCount + left + 1


""" 
Binary search tree. 

Given a binary tree, determine if it is a valid binary search  tree
"""


def isValidTree(
    head: TreeNode, parentCompare: Callable[[TreeNode], bool] = lambda node: True
) -> bool:
    case_one = True
    case_two = True
    if head._hasLeft():
        case_one = head.value > head.left_node.value and parentCompare(head.left_node)
    if head._hasRight():
        case_two = head.value < head.right_node.value and parentCompare(head.right_node)
    return case_one and case_two


def isValidBinarySearchTree(head: TreeNode) -> bool:
    if head == None:
        return True
    if isValidTree(head=head) == False:
        return False
    gtThenParen: Callable[[TreeNode], bool] = lambda node: node.value > head.value
    lsThenParen: Callable[[TreeNode], bool] = lambda node: node.value < head.value
    leftChild = _isValidBinarySearchTree(head=head.left_node, parentCompare=lsThenParen)
    rightChild = _isValidBinarySearchTree(
        head=head.right_node, parentCompare=gtThenParen
    )

    return leftChild and rightChild


def _isValidBinarySearchTree(
    head: TreeNode, parentCompare: Callable[[TreeNode], bool]
) -> bool:
    if head == None:
        return True
    if isValidTree(head=head, parentCompare=parentCompare) == False:
        return False
    leftChild = isValidBinarySearchTree(
        head=head.left_node, parentCompare=parentCompare
    )
    rightChild = isValidBinarySearchTree(
        head=head.right_node, parentCompare=parentCompare
    )
    return leftChild and rightChild
