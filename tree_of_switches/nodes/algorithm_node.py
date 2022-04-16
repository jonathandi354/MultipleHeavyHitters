from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from tree_of_switches.nodes.node import Node


class AlgorithmNode(Node):

    def __init__(self, algorithm):
        Node.__init__(self)
        self._algorithm = algorithm
        self._optimal = OptimalAlgorithm()
        self._keys = []
        self._number_of_messages_in = 0
        self._num_message_passed = 0
        self._num_message_matched = 0

    def process_message(self, message):
        self._num_message_passed += 1
        if message.key in self._keys:
            self._num_message_matched += 1
            self._algorithm.process_message(message)
            self._optimal.process_message(message)

        if self.parent is not None:
            self.parent.process_message(message)

    def get_top_k_keys(self, k) -> dict:
        return self._algorithm.get_top_k_keys(k)

    def print_num_message_passed(self):
        txt = "number of message passed: {}, in index: {}".format(self._num_message_passed, self.index)
        print(txt)

    def print_num_message_matched(self):
        txt = "number of message matched: {}, in index: {}".format(self._num_message_matched, self.index)
        print(txt)

    @property
    def keys(self) -> list:
        return self._keys
    @keys.setter
    def keys(self, value):
        self._keys = value


