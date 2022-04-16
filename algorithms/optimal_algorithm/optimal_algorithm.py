from abc import ABC

from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from ..message import Message


class OptimalAlgorithm(IHeavyHittersAlgorithm, ABC):

    def __init__(self):
        self._dictionary = {}

    '''
    The optimal algorithm. Just add the key to the table.
    If already exists - increase the corresponding counter.
    '''
    def process_message(self, message: Message):
        key = message.key
        if key not in self._dictionary:
            self._dictionary[key] = 0
        self._dictionary[key] += 1

    @property
    def dictionary(self) -> dict:
        return self._dictionary

    '''
    Iterates over the entire dictionary and prints the keys and counters.
    '''
    def print_result(self):
        for key in self._dictionary:
            txt = "key: {}, value: {}".format(key, self._dictionary[key])
            print(txt)

    '''
    Sorts the dictionary according to the counters of each key.
    '''
    def _sort_dict(self):
        self._dictionary = {k: v for k, v in
                            sorted(self._dictionary.items(), key=lambda item: item[1], reverse=True)}

    '''
    Returns a dict of the top - k keys and their counters.
    '''
    def get_top_k_keys(self, k) -> dict:
        self._sort_dict()
        top_k = {}
        i = 0
        for key, value in self._dictionary.items():
            if i == k:
                return top_k
            top_k[key] = value
            i += 1
        return top_k
