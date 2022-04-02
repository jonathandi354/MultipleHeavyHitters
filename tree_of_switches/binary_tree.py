import math

from tree_of_switches.node import Node


class BinaryTree:
    def __init__(self, size):
        if not self._check_if_size_valid(size):
            raise Exception("the size is not valid!")
        self._size = size
        self._nodes = []

    def _build_tree(self):
        for i in range(math.log2(self._size + 1)):
            for j in range(math.pow(2, i)):
                self._nodes[i + j] = Node()






    def _check_if_size_valid(self, size):
        return ((size+1) & size == 0) and (size!=0)