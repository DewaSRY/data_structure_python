""" 
linear data is stack and queue
"""

"""
Given a sting containing only parentheses, determine if it is valid. the string is valid if all parentheses close  
"""


parenthesesMap = {
    "(": 0,
    ")": 0,
    "[": 1,
    "]": 1,
    "{": 2,
    "}": 2,
}


def equalPartParentheses(start_1: str, start_2: str):
    return parenthesesMap[start_1] == parenthesesMap[start_2]


def validParentheses(parentheses: str):
    if len(parentheses) == 0:
        return True
    if len(parentheses) % 2 != 0:
        return False

    stack = []
    stack.append(parentheses[0])

    for index_1 in range(1, len(parentheses)):
        currentChar = parentheses[index_1]
        stackPeek = stack[-1]
        if equalPartParentheses(start_1=currentChar, start_2=stackPeek):
            stack.pop()  # pop the last item
        else:
            stack.append(currentChar)

    return len(stack) == 0


""" 
minimum bracket to remove

Given a string only contain rounded brackets "(" and ")" and lowercase characters, remove the last amount of brackets so the string is valid 

as string is consider valid if it is empty or all bracket  is close 
"""

roundedBrackets = {"(": 0, ")": 1}


def removeChar(string: str, stack: list[int]):
    newChar = ""
    for index_i in range(len(string)):
        if index_i not in stack:
            newChar += string[index_i]

    return newChar


def isMatchBracket(char_1: str, chart_2: str):
    return roundedBrackets[char_1] == 0 and roundedBrackets[chart_2] == 1


def removeBrackets(string: str):
    currentString = string
    if len(currentString) == 0:
        return True
    stack = []
    for index_i in range(len(string)):
        currentChar = currentString[index_i]
        if currentChar not in roundedBrackets:
            continue
        elif len(stack) == 0:
            stack.append(index_i)
        else:
            currentPeekIndex = stack[-1]
            currentPeekBracket = currentString[currentPeekIndex]
            if isMatchBracket(char_1=currentPeekBracket, chart_2=currentChar):
                stack.pop()
            else:
                stack.append(index_i)

    return removeChar(string=currentString, stack=stack)


"""
Implement que with stack

"""


class Stack:
    def __init__(self) -> None:
        self.stackData = []

    def push(self, value: int):
        self.stackData.append(value)

    def pop(self):
        return self.stackData.pop()

    def size(self):
        return len(self.stackData)

    def getPeek(self):
        return self.stackData[-1]


class Queue:
    head: int = None
    stackInt = Stack()
    stackOut = Stack()

    def enqueue(self, value: int):
        self.stackInt.push(value=value)

    def peek(self):
        if self.stackOut.size() > 0:
            return self.stackOut.getPeek()
        else:
            self._fillStackOut()
            return self.peek()

    def dequeue(self) -> int:
        if self.stackOut.size() > 0:
            return self.stackOut.pop()
        else:
            self._fillStackOut()
            return self.dequeue()

    def _fillStackOut(self):
        while self.stackInt.size() > 0:
            self.stackOut.push(self.stackInt.pop())
