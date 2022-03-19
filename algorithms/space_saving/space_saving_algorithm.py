from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from .space_saving_counter import SpaceSavingCounter
from .space_saving_counters_table import SpaceSavingCountersTable
from ..message import Message


class SpaceSavingAlgorithm(IHeavyHittersAlgorithm):
    def __init__(self, counters_number: int):
        self.counters_number = counters_number
        self.counters_table = SpaceSavingCountersTable(self.counters_number)

    def process_message(self, message: Message):
        key = message.key
        if self.counters_table.is_key_in_table(key):
            self.counters_table.increment_at_key(key)
        else:
            if not self.counters_table.is_table_full():
                self.counters_table.add_row_at_key(key)
                self.counters_table.increment_at_key(key)
            else:
                self.counters_table.swap_min_row(key)

    def get_counters(self):
        return self.counters_table.table
