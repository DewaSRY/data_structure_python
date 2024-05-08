""" 

"""

from typing import Self, Union
from dataclasses import dataclass


@dataclass
class TreeNode:
    left_node: Union[None, Self] = None
    right_node: Union[None, Self] = None
    value: int = 0

    def __init__(self, value: int) -> None:
        self.value = value

    def setLeftNode(self, node: Self):
        self.left_node = node

    def setRightNode(self, node: Self):
        self.right_node = node

    def compare(self, node: Self):
        """compare
        if input node is lest then this node
        """
        return self.value > node.value

    def hasLeft(self) -> bool:
        return self.left_node != None

    def hasRight(self) -> bool:
        return self.right_node != None


class MyTree:
    root = None

    def insert(self, value: int):
        newNode = TreeNode(value=value)
        if self.root == None:
            self.root = newNode
            return
        else:
            self._traverseToInsertTwo(node=newNode, currentNode=self.root)

    def lookup(self, value: int) -> bool:

        if self.root == None:
            return False
        return self._lookup(value=value, currentNode=self.root)

    def delete(self, value: int):
        parentNode = self._getParent(value=value, currentNode=self.root)
        nodeToDelete = self._getNodeWontDelete(value_to_delete=value, parent=parentNode)

        if nodeToDelete.hasLeft() and nodeToDelete.hasRight():
            self._deleteTwoChild(parent=parentNode, nodeToDelete=nodeToDelete)
        elif nodeToDelete.hasLeft() or nodeToDelete.hasRight():
            self._deleteOneChild(parent=parentNode, nodeToDelete=nodeToDelete)
        else:
            self._deleteNoChild(parent=parentNode, nodeToDelete=nodeToDelete)

    def _getNodeWontDelete(self, value_to_delete: int, parent: TreeNode):
        if parent.left_node.value == value_to_delete:
            return parent.left_node
        else:
            return parent.right_node

    def _deleteNoChild(self, parent: TreeNode, nodeToDelete: TreeNode):
        if parent.compare(nodeToDelete):
            parent.setLeftNode(None)
        else:
            parent.setRightNode(None)

    def _deleteOneChild(self, parent: TreeNode, nodeToDelete: TreeNode):
        childrenNode = (
            nodeToDelete.left_node
            if nodeToDelete.hasLeft()
            else nodeToDelete.right_node
        )
        if parent.compare(nodeToDelete):
            parent.setLeftNode(childrenNode)
        else:
            parent.setRightNode(childrenNode)

    def _deleteTwoChild(self, parent: TreeNode, nodeToDelete: TreeNode):
        rightChild = nodeToDelete.right_node
        leftChild = nodeToDelete.left_node
        if parent.compare(nodeToDelete):
            rightChild.setLeftNode(leftChild)
            parent.setLeftNode(rightChild)
        else:
            leftChild.setRightNode(rightChild)
            parent.setRightNode(leftChild)

    def _getParent(self, value: int, currentNode: TreeNode):
        if (
            currentNode.right_node.value == value
            or currentNode.left_node.value == value
        ):
            return currentNode
        elif value < currentNode.value:
            return self._getParent(value=value, currentNode=currentNode.left_node)
        else:
            return self._getParent(value=value, currentNode=currentNode.right_node)

    def _lookup(self, value: int, currentNode: TreeNode) -> bool:
        if currentNode == None:
            return False
        if currentNode.left_node and value < currentNode.value:
            return self._lookup(value=value, currentNode=currentNode.left_node)
        elif currentNode.right_node and value > currentNode.value:
            return self._lookup(value=value, currentNode=currentNode.right_node)
        else:
            return currentNode.value == value

    def _traverseToInsertTwo(self, node: TreeNode, currentNode: TreeNode):
        if currentNode.compare(node=node):
            if currentNode.left_node != None:
                self._traverseToInsertTwo(node=node, currentNode=currentNode.left_node)
            else:
                currentNode.setLeftNode(node=node)
        else:
            if currentNode.right_node != None:
                self._traverseToInsertTwo(node=node, currentNode=currentNode.right_node)
            else:
                currentNode.setRightNode(node=node)

    def _traverseToInsert(self, node: TreeNode):
        currentNode = self.root
        while currentNode != None:
            if currentNode.compare(node=node):
                if currentNode.left_node != None:
                    currentNode = currentNode.left_node
                else:
                    currentNode.setLeftNode(node=node)
                    return
            else:
                if currentNode.right_node != None:
                    currentNode = currentNode.right_node
                else:
                    currentNode.setRightNode(node=node)
                    return
