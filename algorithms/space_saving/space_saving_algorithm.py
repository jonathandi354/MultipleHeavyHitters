from abc import ABC

from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from .space_saving_counter import SpaceSavingCounter
from ..message import Message
from .limited_size_dict import LimitedSizeDict


class SpaceSavingAlgorithm(IHeavyHittersAlgorithm, ABC):
    def __init__(self, counters_number: int):
        self._counters_number = counters_number
        self._counters_dict = LimitedSizeDict(counters_number)

    def process_message(self, message: Message):
        key = message.key
        if key in self._counters_dict.keys():
            self._counters_dict[key].increment()
        else:
            try:
                self._counters_dict[key] = SpaceSavingCounter(key)
                self._counters_dict[key].increment()
            except Exception:
                min_key = self._find_min_counter_key()
                self._counters_dict[min_key].key = key
                self._counters_dict[key] = self._counters_dict.pop(min_key)
                self._counters_dict[key].increment()

    def _find_min_counter_key(self) -> str:
        min_counter = min(self._counters_dict.values(), key=lambda counter: counter.get_count())
        min_key = list(filter(lambda key: self._counters_dict[key] == min_counter, self._counters_dict))[0]
        return min_key

    def clear(self):
        self._counters_dict = LimitedSizeDict(self._counters_number)

    def get_counters(self):
        return self._counters_dict