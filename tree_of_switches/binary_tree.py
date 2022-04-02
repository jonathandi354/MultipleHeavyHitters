from tree_of_switches.nodes.algorithm_node import AlgorithmNode
from tree_of_switches.nodes.node import Node


def _check_if_size_valid(size):
    return ((size + 1) & size == 0) and (size != 0)


class BinaryTree:
    def __init__(self, size, node_factory):
        if not _check_if_size_valid(size):
            raise Exception("the size is not valid!")
        self._size = size
        self.nodes = []
        self._node_factory = node_factory
        self._build_tree()

    def _build_tree(self):
        self._root = self._node_factory.create()
        self.nodes.append(self._root)
        curr_node = self._root
        curr_node_index = 0
        for i in range(1, self._size):
            if (curr_node.left_son is not None) and (curr_node.right_son is not None):
                curr_node_index += 1
                curr_node = self.nodes[curr_node_index]

            new_node = self._node_factory.create()
            new_node.index = i
            self.nodes.append(new_node)
            curr_node.insert(new_node)

    def get_leaves(self):
        return self.nodes[int(self._size / 2):]


