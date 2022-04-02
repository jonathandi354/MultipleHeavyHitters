from abc import abstractmethod

from tree_of_switches.keys_distibutor.keys_distributor import KeysDistributor


class EquallyLevelDistributor(KeysDistributor):

    def __init__(self, keys, nodes, number_of_levels):
        KeysDistributor.__init__(self, keys, nodes)
        self._number_of_levels = number_of_levels

    @abstractmethod
    def distribute_keys(self):
        if len(self._keys) % self._number_of_levels != 0:
            raise Exception("number of keys is not valid!")
        chunk_size = int(len(self._keys) / self._number_of_levels)
        chunks = [self._keys[x:x + chunk_size] for x in range(0, len(self._keys), chunk_size)]
        for i in range(self._number_of_levels):
            nodes_in_level_i = [node for node in self._nodes if node.level == i]
            for node in nodes_in_level_i:
                node.keys = chunks[i]
