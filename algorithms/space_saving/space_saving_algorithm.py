from abc import ABC

from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from .space_saving_counter import SpaceSavingCounter
from ..message import Message
from .limited_size_dict import LimitedSizeDict


class SpaceSavingAlgorithm(IHeavyHittersAlgorithm, ABC):
    def __init__(self, counters_number: int):
        self.counters_number = counters_number
        self.counters_dict = LimitedSizeDict(counters_number)

    def process_message(self, message: Message):
        key = message.key
        if key in self.counters_dict.keys():
            self.counters_dict[key].increment()
        else:
            try:
                self.counters_dict[key] = SpaceSavingCounter(key)
                self.counters_dict[key].increment()
            except:
                min_key = self._find_min_counter_key()
                self.counters_dict[min_key].key = key
                self.counters_dict[key] = self.counters_dict.pop(min_key)
                self.counters_dict[key].increment()

    def _find_min_counter_key(self) -> str:
        min_counter = min(self.counters_dict.values(), key=lambda counter: counter.get_count())
        min_key = list(filter(lambda key: self.counters_dict[key] == min_counter, self.counters_dict))[0]
        return min_key
