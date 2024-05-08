""" 

"""


def swapArray(arr: list[int], index_1: int, index_2: int):
    tempNum = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = tempNum

    return arr


""" 
Bubble Short

"""


def bubbleShort(arr: list[int]):
    # totalLoop = 0
    for index_i in range(len(arr)):
        for index_j in range(len(arr) - 1):
            # totalLoop += 1
            if arr[index_i] < arr[index_j]:
                swapArray(arr=arr, index_1=index_i, index_2=index_j)
    # print(f"quick short total loop loop {totalLoop} array length {len(arr)}")
    return arr


""" 
insertion Shorting 
"""


def insertionShort(arr: list[int]):

    # totalLoop = 0
    for index_i in range(1, len(arr)):  # start from index 1
        currentVa = arr[index_i]

        index_j = index_i - 1

        while index_j > -1 and currentVa < arr[index_j]:
            arr[index_j + 1] = arr[index_j]

            index_j -= 1
            # totalLoop += 1
        arr[index_j + 1] = (
            currentVa  # in this case index j is -1 so plush 1 is 0, then we put the current value to the start position
        )

    # print(f"insertion short total loop {totalLoop } array length {(arr)}")
    return arr


""" 
Selection short 
"""


def selectionShort(arr: list[int]):
    # totalLoop = 0
    for index_i in range(len(arr)):
        indexMinVal = index_i
        for index_j in range(index_i + 1, len(arr)):
            # totalLoop += 1
            if arr[index_j] < arr[indexMinVal]:
                indexMinVal = index_j

        if indexMinVal != index_i:
            swapArray(arr=arr, index_1=indexMinVal, index_2=index_i)

    # print(f"selection short total loop {totalLoop} arr length {len(arr)}")

    return arr


""" 
Marge Short 
"""


def margeShort(arr: list[int]):
    if len(arr) == 1:
        return arr
    midNumber = int(len(arr) / 2)
    leftArr = margeShort(arr=arr[:midNumber])
    rightArr = margeShort(arr=arr[midNumber:])

    return MargeArray(arr_1=leftArr, arr_2=rightArr)


def MargeArray(arr_1: list[int], arr_2: list[int]):
    result = []
    while (
        len(arr_1) != 0 and len(arr_2) != 0
    ):  # the looping roo as long boot have value to compare
        if (
            arr_1[0] < arr_2[0]
        ):  # we compare every first element so the result arr ordered correctly
            result.append(arr_1.pop(0))
        else:
            result.append(arr_2.pop(0))

    return (
        result + arr_1 + arr_2
    )  # either one of them still have one value how doest have value to compare


""" 
Quick Short
"""


def quickSort(arr: list[int], left_i=None, right_i=None):
    leftIndex = left_i if left_i != None else 0
    rightIndex = right_i if right_i != None else len(arr) - 1
    if leftIndex >= rightIndex:
        return

    pivotIndex = partition(arr=arr, left_i=leftIndex, right_i=rightIndex)
    quickSort(arr=arr, left_i=leftIndex, right_i=pivotIndex - 1)
    quickSort(arr=arr, left_i=pivotIndex + 1, right_i=rightIndex)

    return arr


def partition(arr: list[int], left_i: int, right_i: int):
    """partition
    partition is process to look the right position of the pivot val then return the pivot index to make new quick short
    """
    pivotValue = arr[right_i]
    partitionIndex = left_i

    for index in range(left_i, right_i):
        if arr[index] < pivotValue:
            swapArray(arr=arr, index_1=index, index_2=partitionIndex)
            partitionIndex += 1

    swapArray(arr=arr, index_1=right_i, index_2=partitionIndex)

    return partitionIndex


""" 
Radix Short
"""
