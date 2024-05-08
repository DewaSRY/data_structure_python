""" 

"""

from unittest import TestCase
from src.sorting_algorithms import (
    bubbleShort,
    insertionShort,
    selectionShort,
    margeShort,
    quickSort,
)


class TestShortingAlgorithms(TestCase):

    def setUp(self) -> None:
        self.arraysList = [1, 9, 2, 8, 3, 7, 4, 6, 5, 15, 10, 11, 14, 12, 13]
        self.shortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def tearDown(self) -> None:
        self.arraysList = [1, 9, 2, 8, 3, 7, 4, 6, 5]

    def test_bubbleShort(self):
        actual = bubbleShort(arr=self.arraysList)

        assert actual == self.shortedArray

    def test_insertionShort(self):
        actual = insertionShort(arr=self.arraysList)

        assert actual == self.shortedArray

    def test_selectionShort(self):
        actual = selectionShort(arr=self.arraysList)
        assert actual == self.shortedArray

    def test_margeShort(self):
        actual = margeShort(arr=self.arraysList)
        assert actual == self.shortedArray

    def test_quickSort(self):
        actual = quickSort(arr=self.arraysList)
        assert actual == self.shortedArray
