""" 

"""

from unittest import TestCase
from src.recursive_question import (
    findKLargeElement,
    binarySearch,
    findStartAndEndPosition,
    findStartAndEndPosition_2,
)


class TestRecursive(TestCase):

    def setUp(self) -> None:
        self.sortArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def test_findKElement(self):
        array = [1, 9, 2, 8, 3, 7, 4, 6, 5, 15, 10, 11, 14, 12, 13]

        actual = findKLargeElement(arr=array, k=7)
        assert actual == 9

    def test_binarySearch(self):
        actual = binarySearch(arr=self.sortArr, target=15)
        assert actual == 14

    def test_findStartAndEndPosition(self):
        actual = findStartAndEndPosition(arr=[1, 3, 3, 5, 5, 5, 8, 9], target=5)
        assert actual == [3, 5]

    def test_findStartAndEndPosition_2(self):
        actual = findStartAndEndPosition_2(arr=[1, 3, 3, 5, 5, 5, 8, 9], target=5)
        assert actual == [3, 5]
