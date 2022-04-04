from ..iheavy_hitters_algorithm import IHeavyHittersAlgorithm
from ..message import Message


class OptimalAlgorithm(IHeavyHittersAlgorithm):

    def __init__(self):
        self._dict = {}

    def process_message(self, message: Message):
        key = message.key
        if key not in self._dict:
            self._dict[key] = 0
        self._dict[key] += 1

    def get_counters(self):
        return self._dict

    def print_result(self):
        for key in self._dict:
            txt = "key: {}, value: {}".format(key, self._dict[key])
            print(txt)

    def _sort_dict(self):
        self._dict = {k: v for k, v in
                      sorted(self._dict.items(), key=lambda item: item[1], reverse=True)}

    def get_top_k_keys(self, k):
        self._sort_dict()
        top_k = {}
        i = 0
        for key, value in self._dict.items():
            if i == k:
                return top_k
            top_k[key] = value
            i += 1
        return top_k
