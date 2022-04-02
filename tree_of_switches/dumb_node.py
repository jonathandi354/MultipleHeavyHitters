from abc import ABC

from tree_of_switches.node import Node


class DumbNode(Node, ABC):

    def process_message(self, message):
        print("process message at index {}!", self.index)
        print("passing to parent to process")
        if (self.parent is not None):
            self.parent.process_message(message)

