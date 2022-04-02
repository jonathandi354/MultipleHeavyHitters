from abc import ABC

from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from ..message import Message


class OptimalAlgorithm(IHeavyHittersAlgorithm, ABC):

    def __init__(self):
        self._dict = {}

    def process_message(self, message: Message):
        key = message.key
        if key not in self._dict:
            self._dict[key] = 0
        self._dict[key] += 1

    def get_counters(self):
        return self._dict
