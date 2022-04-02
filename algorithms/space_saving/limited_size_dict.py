
from collections.abc import MutableMapping


def _key_transform(key):
    return key


class LimitedSizeDict(MutableMapping):

    def __init__(self, dict_size):
        self._dict_size = dict_size
        self._store = dict()

    def __getitem__(self, key):
        return self._store[_key_transform(key)]

    def __setitem__(self, key, value):
        if len(self._store) == self._dict_size:
            raise Exception("Dictionary is full")
        else:
            self._store[_key_transform(key)] = value

    def __delitem__(self, key):
        del self._store[_key_transform(key)]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    @property
    def store(self):
        return self._store
