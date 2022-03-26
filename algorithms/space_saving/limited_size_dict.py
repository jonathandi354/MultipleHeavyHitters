
from collections.abc import MutableMapping


class LimitedSizeDict(MutableMapping):

    def __init__(self, dict_size):
        self.dict_size = dict_size
        self.store = dict()

    def __getitem__(self, key):
        return self.store[self._keytransform(key)]

    def __setitem__(self, key, value):
        if len(self.store) == self.dict_size:
            raise Exception("Dictionary is full")
        else:
            self.store[self._keytransform(key)] = value

    def _keytransform(self, key):
        return key

    def __delitem__(self, key):
        del self.store[self._keytransform(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
