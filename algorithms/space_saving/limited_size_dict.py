from collections.abc import MutableMapping


class LimitedSizeDict(MutableMapping):

    def __init__(self, dict_size):
        self._dict_size = dict_size
        self.store = dict()

    def __getitem__(self, key):
        return self.store[self._key_transform(key)]

    def __setitem__(self, key, value):
        if len(self.store) == self._dict_size:
            raise Exception("Dictionary is full")
        else:
            self.store[self._key_transform(key)] = value

    def __delitem__(self, key):
        del self.store[self._key_transform(key)]

    def _key_transform(self, key):
        return key

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
