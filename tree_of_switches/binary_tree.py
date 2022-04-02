import math

from tree_of_switches.dumb_node import DumbNode
from tree_of_switches.node import Node


class BinaryTree:
    def __init__(self, size):
        if not self._check_if_size_valid(size):
            raise Exception("the size is not valid!")
        self._size = size
        self._nodes = []
        self._build_tree()

    def _build_tree(self):
        self._root = DumbNode()
        self._root.level = 0
        self._root.index = 0
        self._nodes.append(self._root)
        curr_node = self._root
        curr_node_index = 0
        for i in range(1, self._size):
            if (curr_node.left_son is not None) and  (curr_node.right_son is not None):
                curr_node_index += 1
                curr_node = self._nodes[curr_node_index]

            new_node = DumbNode()
            new_node.index = i
            self._nodes.append(new_node)
            curr_node.insert(new_node)





    def get_leaves(self):
        return self._nodes[int(self._size / 2):]


    def _check_if_size_valid(self, size):
        return ((size+1) & size == 0) and (size!=0)