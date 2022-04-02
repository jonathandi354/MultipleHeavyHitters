from abc import ABCMeta, abstractmethod


class Node:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.right_son = None
        self.left_son = None
        self.parent = None
        self.level = 0
        self.index = 0

    def insert(self, node):
        if self.left_son is None:
            self.left_son = node
            node.parent = self
            node.level = self.level + 1
        else:
            if self.right_son is None:
                self.right_son = node
                node.parent = self
                node.level = self.level + 1

    @abstractmethod
    def process_message(self, message):
        raise NotImplementedError


