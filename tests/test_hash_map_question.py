""" 
"""

from unittest import TestCase
from src.hash_map_question import firstRecurring


class TestHashMapQuestion(TestCase):

    def test_recurring(self):
        array_test = [2, 5, 1, 2, 3, 5, 2, 1, 4]
        assert firstRecurring(array=array_test) == 2
