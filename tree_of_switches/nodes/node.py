from abc import ABCMeta, abstractmethod


class Node:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._right_son = None
        self._left_son = None
        self._parent = None
        self._level = 0
        self._index = 0

    def insert(self, node):
        if self._left_son is None:
            self._left_son = node
            node.parent = self
            node.level = self._level + 1
        else:
            if self._right_son is None:
                self._right_son = node
                node.parent = self
                node.level = self._level + 1

    @abstractmethod
    def process_message(self, message):
        raise NotImplementedError

    @property
    def right_son(self):
        return self._right_son

    @property
    def left_son(self):
        return self._left_son

    @property
    def parent(self):
        return self._parent

    @property
    def level(self) -> int:
        return self._level

    @property
    def index(self) -> int:
        return self._index

    @parent.setter
    def parent(self, value):
        self._parent = value

    @level.setter
    def level(self, value):
        self._level = value

    @index.setter
    def index(self, value):
        self._index = value
