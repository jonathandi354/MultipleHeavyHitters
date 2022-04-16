from abc import abstractmethod

from tree_of_switches.keys_distibutor.keys_distributor import KeysDistributor


class GraduallyLevelDistributor(KeysDistributor):

    def __init__(self, keys, nodes, number_of_levels):
        KeysDistributor.__init__(self, keys, nodes)
        self._number_of_levels = number_of_levels

    @abstractmethod
    def distribute_keys(self):
        if len(self._keys) % self._number_of_levels != 0:
            raise Exception("number of keys is not valid!")