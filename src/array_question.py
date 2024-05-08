from typing import Mapping

""" 
Reverse string
"""


def reverseString(string_input: str, string_temp=""):
    if len(string_input) == 0:
        return string_temp
    return reverseString(
        string_input=string_input[:-1],
        string_temp=string_temp + string_input[-1],
    )


def MargeSort(left_arr: list[int], right_arr: list[int]):
    marge_array = []
    while len(left_arr) != 0 and len(right_arr) != 0:
        if left_arr[0] < right_arr[0]:
            marge_array.append(left_arr.pop(0))
        else:
            marge_array.append(right_arr.pop(0))

    return marge_array + left_arr + right_arr


""" 
Given an array of integers, return teh indices of the two numbers that add up to a given target
"""


def twoSum(numbs: list[int], target: int):
    mapNum: Mapping[int, int] = {}

    for n in range(len(numbs)):
        mapNum[target - numbs[n]] = n

    for m in range(len(numbs)):
        try:
            mappedIndex = mapNum[m]
            return [mappedIndex, n]
        except Exception as e:
            continue

    return []


def twoSum_2(numbs: list[int], target: int):

    for idx_i in range(len(numbs)):

        rest_num = target - numbs[idx_i]
        for idx_j in range(idx_i + 1, len(numbs)):
            if numbs[idx_j] == rest_num:
                return [idx_i, idx_j]

    return []


""" 
you are given an array of positive integers where 
each integer represents the height of a vertical 
line on a chart. Find two ines which together with 
the x-axis forms a container that would hold the 
greater amount of  water. return the area of water 
it would hold.

answer: 
- the we should return the area which hight multiple by long, with the hight result

"""


def min(num_1: int, num_2: int):
    return num_1 if num_1 < num_2 else num_2


def max(num_1: int, num_2: int):
    return num_1 if num_1 > num_2 else num_2


def waterContainer(numbs: list[int]):
    currentGreaterArea = 0
    index_1 = 0
    index_2 = len(numbs) - 1
    while index_1 != index_2:
        hightUse = min(num_1=numbs[index_1], num_2=numbs[index_2])
        wideUse = index_2 - index_1
        currentGreaterArea = max(num_1=currentGreaterArea, num_2=(hightUse * wideUse))
        if numbs[index_1] <= numbs[index_2]:
            index_1 += 1
        else:
            index_2 -= 1
    return currentGreaterArea


""" 
given an array of integers representing an elevation map where rhe width of each 
bar is 1, return ho much rainwater can be trapped
"""


def waterCollector(num_1: int, num_2: int):
    water = num_1 - num_2
    return water if water > 0 else 0


def collectWater(nums: list[int], index: int, bound: int, increment: int):
    hightNum = nums[index]
    index += increment
    waterCollected = 0
    while index != bound:
        hightNum = max(num_1=hightNum, num_2=nums[index])
        waterCollected += waterCollector(num_1=hightNum, num_2=nums[index])
        index += increment
    return waterCollected


def trappedWaterContainer_2(nums: list[int]):
    left_p = 0
    left_r = len(nums) - 1
    midNumber = int((left_r / 2) + 1)
    left_side = collectWater(nums=nums, index=left_p, bound=midNumber, increment=1)
    right_side = collectWater(nums=nums, index=left_r, bound=midNumber, increment=-1)
    return left_side + right_side


""" 
Given two string S and T, return if they equal when both are typed out,. any # that appears in the string counts as a backspace
"""


def cleanTheString(strings: str):
    result = ""
    for n in strings:
        if n == "#":
            result = result[:-1]
        else:
            result += n
    return result


def typeOutString(string_1: str, string_2: str) -> int:
    cleanStrOne = cleanTheString(strings=string_1)
    cleanStrTwo = cleanTheString(strings=string_2)

    if len(cleanStrOne) != len(cleanStrTwo):
        return False
    else:
        for n in range(len(cleanStrOne)):
            if cleanStrOne[n] != cleanStrTwo[n]:
                return False

        return True


def getChar(string: str, currentIndex: int):
    if currentIndex <= -1:
        return ["", 0]

    if string[currentIndex] != "#":
        return [string[currentIndex], currentIndex]
    #  b#c#d#
    backSpaceAmount = 2
    while backSpaceAmount > 0:
        currentIndex -= 1
        backSpaceAmount -= 1
        if currentIndex <= -1:  # in this scenario the string will get circular
            return ["", 0]
        if string[currentIndex] == "#":
            backSpaceAmount += 2
    return [string[currentIndex], currentIndex]


def typeOutString_2(string_1: str, string_2: str):
    backPOne = len(string_1) - 1
    backPTwo = len(string_2) - 1
    while backPOne > -1 or backPTwo > -1:
        charOne, nextIndexOne = getChar(string=string_1, currentIndex=backPOne)
        charTwo, nextIndexTwo = getChar(string=string_2, currentIndex=backPTwo)

        if charOne != charTwo:
            return False

        backPOne = nextIndexOne - 1
        backPTwo = nextIndexTwo - 1
    # print(f"index one {backPOne} index two {backPTwo} {string_2}")
    return True


""" 
Longest sub string, given a string, find the length of the longest substring without repeating characters
"""


def longestSubString(string: str):
    backPointer = 0
    frondPointer = 1
    longestSub = 0
    currentSub = string[:frondPointer]
    while frondPointer < len(string) - 1:
        frondPointer += 1
        if string[frondPointer] in currentSub:
            backPointer += 1

        currentSub = string[backPointer:frondPointer]
        longestSub = max(num_1=longestSub, num_2=len(currentSub))
    return longestSub


""" 
Longest sub string, given a string, find the length of the longest substring without repeating characters
- answer with sliding window 
    from a window over some portion of sequential data then move the window through the data to capture different parts of it
"""


def checkInMap(string: str, currentIndex: int, map: Mapping[int, int]):
    char = string[currentIndex]
    prevCharIndex = 0
    isInMap = False
    if char in map:
        prevCharIndex = map[char]
        map[char] = currentIndex
        isInMap = True
    else:
        map[char] = currentIndex

    return [isInMap, map, prevCharIndex]


def newLeftP(isInMap: bool, currentLeft: int, prefCharIdx: int):
    if isInMap == False or currentLeft > prefCharIdx:
        return currentLeft
    return prefCharIdx + 1


def longesSubString_2(string: str):
    left_p = 0
    longesSub = 0
    numMap: Mapping[int, int] = {}
    for right_p in range(len(string)):
        isInMap, map, prevCharIndex = checkInMap(
            string=string, currentIndex=right_p, map=numMap
        )
        numMap = map
        left_p = newLeftP(
            isInMap=isInMap, currentLeft=left_p, prefCharIdx=prevCharIndex
        )
        currentSub = right_p - left_p + 1
        longesSub = max(num_1=longesSub, num_2=currentSub)

    return longesSub


""" 
string palindrome
"""


def stringPalindrome(string: str):
    left_p = 0
    right_p = len(string) - 1
    while left_p != right_p:
        if string[left_p] != string[right_p]:
            return False
        left_p += 1
        right_p -= 1

    return True


""" 
         abzcba
"""


def almostPalindrome(string: str):
    left_p = 0
    right_p = 0
    while left_p != right_p:
        if string[left_p] != string[right_p]:
            return stringPalindrome(
                string=string[left_p + 1 : right_p]
            ) or stringPalindrome(string=string[left_p : right_p - 1])

    return True
