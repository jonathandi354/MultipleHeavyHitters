from abc import ABCMeta, abstractmethod


class KeysDistributor:
    __metaclass__ = ABCMeta

    def __init__(self, keys, nodes):
        self._keys = keys
        self._nodes = nodes

    @abstractmethod
    def distribute_keys(self):
        raise NotImplementedError

