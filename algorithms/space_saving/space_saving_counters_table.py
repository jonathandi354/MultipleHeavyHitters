from .space_saving_counter import SpaceSavingCounter


class SpaceSavingCountersTable:

    def __init__(self, table_rows_number: int):
        self.table_rows_number = table_rows_number
        self.table = dict()

    def is_table_full(self) -> bool:
        return len(self.table.keys()) >= self.table_rows_number

    def is_key_in_table(self, key: str) -> bool:
        return key in self.table.keys()

    def get_min_key(self) -> str:
        min_counter = min(self.table.values(), key=lambda counter: counter.get_count())
        min_key = list(filter(lambda key: self.table[key]==min_counter, self.table))[0]
        return min_key

    def increment_at_key(self, key: str):
        self.table.get(key).increment()

    def add_row_at_key(self, key: str):
        self.table[key] = SpaceSavingCounter()
        self.table.get(key).set_key(key)

    def swap_min_row(self, new_key: str):
        min_key = self.get_min_key()
        min_counter = self.table.get(min_key)
        min_counter.swap_key(new_key)
        del self.table[min_key]
        self.table[new_key] = min_counter
        self.increment_at_key(new_key)
