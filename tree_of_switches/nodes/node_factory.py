from algorithms.space_saving.space_saving_algorithm import SpaceSavingAlgorithm
from tree_of_switches.nodes.algorithm_node import AlgorithmNode
from tree_of_switches.nodes.dumb_node import DumbNode


class NodeFactory:
    def __init__(self, node_type):
        self._node_type = node_type

    def create(self):
        if self._node_type == DumbNode:
            return DumbNode()
        if self._node_type == AlgorithmNode:
            return AlgorithmNode(SpaceSavingAlgorithm(15))
