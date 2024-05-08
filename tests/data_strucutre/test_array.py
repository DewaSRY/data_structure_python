from unittest import TestCase, skip
from src.data_structure import MayArrays


class TestMyArray(TestCase):
    def setUp(self) -> None:
        self.my_array = MayArrays[int]()

    def test_push_value(self):
        self.my_array.push(value=1)
        self.my_array.push(value=2)
        self.my_array.push(value=3)
        assert self.my_array.at(index_value=0) == 1
        assert self.my_array.at(index_value=1) == 2
        assert self.my_array.at(index_value=2) == 3

    def test_insert_value(self):
        self.my_array.push(value=1)
        self.my_array.push(value=2)
        self.my_array.push(value=3)
        self.my_array.insert(index_value=1, value=2)
        assert self.my_array.at(index_value=0) == 1
        assert self.my_array.at(index_value=1) == 2
        assert self.my_array.at(index_value=2) == 2
        assert self.my_array.at(index_value=3) == 3

    def test_delete_value(self):
        self.my_array.push(value=1)
        self.my_array.push(value=2)
        self.my_array.push(value=3)
        self.my_array.push(value=4)
        self.my_array.delete(index_value=2)

        assert self.my_array.at(index_value=0) == 1
        assert self.my_array.at(index_value=1) == 2
        assert self.my_array.at(index_value=2) == 4

    def test_delete_value_two(self):
        for n in range(10):
            self.my_array.push(value=n + 1)
        self.my_array.delete(index_value=4)
        assert self.my_array.at(index_value=4) == 6
        assert self.my_array.at(index_value=8) == 10

    def test_delete_pop(self):
        for n in range(10):
            self.my_array.push(value=n + 1)
        assert self.my_array.pop() == 10
