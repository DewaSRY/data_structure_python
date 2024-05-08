""" 

"""

from src.data_structure import MyHashMap
from unittest import TestCase


class TestHashTable(TestCase):

    def setUp(self) -> None:
        self.hash_table = MyHashMap()

    def test_generate_hash_ke(self):
        test_key = "bar"
        assert (self.hash_table._get_hash(test_key)) < 10
        assert (self.hash_table._get_hash(test_key)) < 10
        assert (self.hash_table._get_hash(test_key)) < 10
        assert (self.hash_table._get_hash(test_key)) < 10

    def test_create_hash_table(self):
        self.hash_table.set("one", 1)
        list = ["a", "b", "c", "d"]
        for char in list:
            self.hash_table.set(value=ord(char), key=char)
        assert self.hash_table.get("one") == 1

    def test_get_none(self):
        assert (self.hash_table.get("hallo_two")) == None

    def test_delete(self):
        self.hash_table.set("hallo", 100)
        assert self.hash_table.get("hallo") == 100
        self.hash_table.delete("hallo")
        assert (self.hash_table.get("hallo")) == None
