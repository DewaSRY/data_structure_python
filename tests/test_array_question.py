from unittest import TestCase
from src.array_question import (
    reverseString,
    MargeSort,
    twoSum,
    twoSum_2,
    waterContainer,
    trappedWaterContainer_2,
    typeOutString,
    typeOutString_2,
    longestSubString,
    longesSubString_2,
    stringPalindrome,
    almostPalindrome,
)


class TestArrayQuestion(TestCase):

    def test_reverse_string(self):
        assert reverseString(string_input="dewa") == "awed"

    def test_marge_array(self):
        actual = MargeSort(left_arr=[1, 3], right_arr=[2, 4])
        assert actual == [1, 2, 3, 4]

    def test_twoSum(self):
        actual = twoSum(numbs=[1, 3, 7, 9, 2], target=11)

        assert actual == [3, 4]

    def test_twoSum_2(self):
        actual = twoSum_2(numbs=[1, 3, 7, 9, 2], target=11)

        assert actual == [3, 4]

    def test_waterContainer(self):
        actual = waterContainer(numbs=[1, 8, 6, 2, 9, 4])
        assert actual == 24

    def test_trappedWaterContainer_2(self):
        actual = trappedWaterContainer_2(nums=[0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2])

        assert actual == 8

    def test_typeOutString(self):
        actual_1 = typeOutString(string_1="abc", string_2="abc")
        actual_2 = typeOutString(string_1="abc", string_2="ad#bc")
        actual_3 = typeOutString(string_1="abc", string_2="adc")
        actual_4 = typeOutString(string_1="", string_2="ad##")
        actual_5 = typeOutString(string_1="a", string_2="abbbb####")
        actual_6 = typeOutString(string_1="b", string_2="a###b")
        actual_7 = typeOutString(string_1="b#", string_2="x#y#z#")

        assert actual_1 == True
        assert actual_2 == True
        assert actual_3 == False
        assert actual_4 == True
        assert actual_5 == True
        assert actual_6 == True
        assert actual_7 == True

    def test_typeOutString_2(self):
        actual_1 = typeOutString_2(string_1="abc", string_2="abc")
        actual_2 = typeOutString_2(string_1="abc", string_2="ad#bc")
        actual_3 = typeOutString_2(string_1="abc", string_2="adc")
        actual_4 = typeOutString_2(string_1="", string_2="ad##")
        actual_5 = typeOutString_2(string_1="a", string_2="abbbb####")
        actual_6 = typeOutString_2(string_1="b", string_2="a###b")
        actual_7 = typeOutString_2(string_1="b#", string_2="x#y#z#")
        actual_8 = typeOutString_2(string_1="bbbextm", string_2="bbb#extm")

        assert actual_1 == True
        assert actual_2 == True
        assert actual_3 == False
        assert actual_4 == True
        assert actual_5 == True
        assert actual_6 == True
        assert actual_7 == True
        assert actual_8 == False

    def test_longestSubString(self):
        actual = longestSubString(string="abcbdca")

        assert actual == 4

    def test_longestSubString_2(self):
        actual = longesSubString_2(string="abcbdca")

        assert actual == 4

    def test_isPalindrome(self):
        actual = stringPalindrome("abcba")
        actual_2 = stringPalindrome("abcdba")

        assert actual == True
        assert actual_2 == False

    def test_almostPalindrome(self):
        actual = almostPalindrome("abcba")
        actual_2 = almostPalindrome("abcdba")

        assert actual == True
        assert actual_2 == True

    # def test_map(self):
    #     test_map = {"a": 2, "b": 3}
    #     print("b" in test_map)
