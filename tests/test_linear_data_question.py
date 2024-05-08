""" 
"""

from src.linear_data_question import validParentheses, removeBrackets, Queue
from unittest import TestCase


class TestLinearDataQuestion(TestCase):

    def test_validParentheses(self):
        actual = validParentheses("")
        actual_1 = validParentheses("{[()]}")
        actual_2 = validParentheses("{[(])]}")
        actual_3 = validParentheses("{()[]}")

        assert actual == True
        assert actual_1 == True
        assert actual_2 == False
        assert actual_3 == True

    def test_RemoveBrackets(self):
        actual = removeBrackets(string="a(b)cd)")

        assert actual == "a(b)cd"

    def test_queueImplementation(self):
        myQueue = Queue()
        listNum = [1, 2, 3, 4]
        for num in listNum:
            myQueue.enqueue(value=num)

        for num in listNum:
            assert myQueue.dequeue() == num
