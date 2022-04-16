from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from tree_of_switches.nodes.node import Node


class AlgorithmNode(Node):

    def __init__(self, algorithm):
        Node.__init__(self)
        self._algorithm = algorithm
        self._optimal = OptimalAlgorithm()
        self.keys = []
        self._number_of_messages_in = 0

    def process_message(self, message):
        if message.key in self.keys:
            self._algorithm.process_message(message)
            self._optimal.process_message(message)

        if self.parent is not None:
            self.parent.process_message(message)

    def get_top_k_keys(self, k):
        return self._algorithm.get_top_k_keys(k)


