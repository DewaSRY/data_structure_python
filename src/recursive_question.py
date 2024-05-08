""" 
find the K larges element 
"""


def swapArr(arr: list[int], index_1: int, index_2: int):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    return arr


def partitionFindK(arr: list[int], left_i: int, right_i: int):
    pivotValue = arr[right_i]
    partitionIndex = left_i
    for index in range(left_i, right_i):
        if arr[index] < pivotValue:
            swapArr(arr=arr, index_1=index, index_2=partitionIndex)
            partitionIndex += 1

    swapArr(arr=arr, index_1=right_i, index_2=partitionIndex)
    return partitionIndex


def findKLargeElement(arr: list[int], k: int, left_i=None, right_i=None, KIndex=None):
    leftIndex = left_i if left_i != None else 0
    rightIndex = right_i if right_i != None else len(arr) - 1
    kIndex = KIndex if KIndex != None else len(arr) - (k)

    partitionIndex = partitionFindK(arr=arr, left_i=leftIndex, right_i=rightIndex)
    if kIndex == partitionIndex:
        # the partitionIndex is the first index put on right position, so if it equal to the kIndex we can return the recursive
        return arr[kIndex]
    # default we set the next recursive on the left side
    nextLeft = leftIndex
    nextRight = partitionIndex - 1
    # if the kIndex is in  bigger then the partition we go to the right side
    if kIndex > partitionIndex:
        nextLeft = partitionIndex + 1
        nextRight = rightIndex

    return findKLargeElement(
        arr=arr, k=k, left_i=nextLeft, right_i=nextRight, KIndex=kIndex
    )


""" 
BinarySearch
"""


def binarySearch(arr: list[int], target: int, left_p: int = None, right_p: int = None):
    left_p = left_p if left_p != None else 0
    right_p = right_p if right_p != None else len(arr) - 1

    if left_p > right_p:
        return -1

    midNum = int((right_p + left_p) / 2)

    if target == arr[midNum]:
        return midNum
    elif target > arr[midNum]:
        return binarySearch(arr=arr, target=target, left_p=midNum + 1, right_p=right_p)
    else:
        return binarySearch(arr=arr, target=target, left_p=left_p, right_p=midNum - 1)


""" 
Given an array of integer sorted in ascending order, return the string and ending index of given target value in an array, i.e [x,y],

- the array will contain duplicate number, we should return the start index of target and end of target
"""


def findStartAndEndPosition(
    arr: list[int], target: int, left_p: int = None, right_p: int = None
):
    left_p = left_p if left_p != None else 0
    right_p = right_p if right_p != None else len(arr) - 1

    if left_p > right_p:
        return [-1, -1]

    midNum = int((right_p + left_p) / 2)

    if target == arr[midNum]:

        return getStartAndEnding(arr=arr, target=target, targetArr=[midNum, midNum])
    elif target > arr[midNum]:
        return findStartAndEndPosition(arr=arr, left_p=midNum + 1, right_p=right_p)
    else:
        return (findStartAndEndPosition(arr=arr, left_p=left_p, right_p=midNum - 1),)


def getStartAndEnding(arr: list[int], target: int, targetArr: list[int]):
    start_idx, end_idx = targetArr
    nextStart = start_idx - 1
    nextEnd = end_idx + 1

    if arr[nextStart] != target and arr[nextEnd] != target:
        return targetArr
    elif arr[nextStart] == target:
        return getStartAndEnding(arr=arr, target=target, targetArr=[nextStart, end_idx])
    else:
        return getStartAndEnding(arr=arr, target=target, targetArr=[start_idx, nextEnd])


""" 
Expand the list by binary Search way

"""


def findStartAndEndPosition_2(
    arr: list[int], target: int, left_p: int = None, right_p: int = None
):
    left_p = left_p if left_p != None else 0
    right_p = right_p if right_p != None else len(arr) - 1

    if left_p > right_p:
        return [-1, -1]

    midNum = int((right_p + left_p) / 2)

    if target == arr[midNum]:
        leftExpand = expandSide(
            arr=arr, previousIdx=midNum, left_p=0, right_p=midNum - 1
        )
        rightExpand = expandSide(
            arr=arr, previousIdx=midNum, left_p=midNum + 1, right_p=len(arr) - 1
        )
        return [leftExpand, rightExpand]
    elif target > arr[midNum]:
        return findStartAndEndPosition_2(arr=arr, left_p=midNum + 1, right_p=right_p)
    else:
        return (findStartAndEndPosition_2(arr=arr, left_p=left_p, right_p=midNum - 1),)


def expandSide(arr: list[int], previousIdx: int, left_p: int, right_p: int):
    if left_p > right_p:
        return previousIdx
    searchIndex = binarySearch(
        arr=arr, target=arr[previousIdx], left_p=left_p, right_p=right_p
    )
    if searchIndex == -1:
        return previousIdx
    elif searchIndex < previousIdx:
        return expandSide(
            arr=arr, previousIdx=searchIndex, left_p=left_p, right_p=searchIndex - 1
        )
    else:
        return expandSide(
            arr=arr, previousIdx=searchIndex, left_p=searchIndex + 1, right_p=right_p
        )
