"""_summary_
"""

from typing import Mapping


class MayArrays[T]:
    array_node: Mapping[int, T] = {}
    current_index = 0

    def push(self, value: T):
        self.array_node[self.current_index] = value
        self.current_index += 1

    def at(self, index_value: int) -> T:
        try:
            self._check_index(index_value=index_value)
            return self.array_node[index_value]
        except Exception as e:
            raise e

    def insert(self, index_value: int, value: T):
        try:
            self._check_index(index_value=index_value)
            self._shift(index_value=index_value)
            self.array_node[index_value] = value
        except Exception as e:
            raise e

    def delete(self, index_value: int):
        try:
            self._check_index(index_value=index_value)
            del self.array_node[index_value]
            self.current_index -= 1
            self._shift(index_value=index_value, increment=-1)
        except Exception as e:
            raise e

    def pop(self):
        last_index = self.current_index - 1
        last_item = self.array_node[last_index]
        self.delete(index_value=last_index)
        return last_item

    def _shift(self, index_value, increment=1):
        loopLength = self.current_index - index_value

        back_pointer = self.current_index - 1 if increment == 1 else index_value + 1
        while loopLength != 0:
            current_value = self.array_node[back_pointer]
            del self.array_node[back_pointer]
            self.array_node[back_pointer + increment] = current_value
            loopLength -= 1
            back_pointer -= increment

    def _check_index(self, index_value: int):
        if index_value < 0:
            raise Exception(f"there is no negative index")
        elif index_value > self.current_index:
            raise Exception(f"index out of bound")
        else:
            return
