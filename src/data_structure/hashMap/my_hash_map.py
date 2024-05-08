""" 
"""

from dataclasses import dataclass
from typing import Union


@dataclass
class Entry:
    key: str
    value: int
    index: int


class MyHashMap:
    table_length = 10
    table: list[list[Entry]] = []

    def __init__(self, table_length=10) -> None:
        self.table_length = table_length
        self._innit_table()

    def set(self, key: str, value: int):
        hash_key = self._get_hash(key=key)
        hash_list_pointer = self.table[hash_key]
        entry_index = len(hash_list_pointer)
        enter = Entry(key=key, value=value, index=entry_index)
        hash_list_pointer.append(enter)

    def delete(self, key: str):
        hash_key = self._get_hash(key=key)
        entry: Entry = self._get_entry(key=key)
        entry_list_pointer = self.table[hash_key]
        entry_list_pointer.pop(entry.index)

    def get(self, key: str):
        entry_get = self._get_entry(key=key)
        if isinstance(entry_get, Entry):
            return entry_get.value
        return None

    def _get_entry(self, key: str) -> Union[Entry, None]:
        hash_key = self._get_hash(key=key)
        table_entry = self.table[hash_key]
        for entry in table_entry:
            if entry.key == key:
                return entry

        return None

    def _innit_table(self):
        for _ in range(self.table_length):
            self.table.append([])

    def _get_hash(self, key: str):
        hash_num = 0
        for chart in key:
            hash_num = (ord(chart) * 7) % self.table_length
        return hash_num
