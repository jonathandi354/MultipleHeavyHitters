import random

from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from data_generation.DataGenerator import DataGenerator
from tree_of_switches.binary_tree import BinaryTree
from tree_of_switches.keys_distibutor.equally_level_distributor import EquallyLevelDistributor
from tree_of_switches.nodes.algorithm_node import AlgorithmNode
from tree_of_switches.nodes.node_factory import NodeFactory

if __name__ == "__main__":

    node_factory = NodeFactory(AlgorithmNode)
    binaryTree = BinaryTree(7, node_factory)
    leaves = binaryTree.get_leaves()
    dataGenerator = DataGenerator(33, 500)
    stream = dataGenerator.generate_stream()

    key_distributor = EquallyLevelDistributor(dataGenerator.keys, binaryTree.nodes, 3)
    key_distributor.distribute_keys()
    for i in range(500):
        random_leaf = random.randint(0, 3)
        leaves[random_leaf].process_message(stream[i])
    for node in binaryTree.nodes:
        print("node:", node.index)
        node._algorithm.print_result()

    optimal = OptimalAlgorithm()
    for m in stream:
        optimal.process_message(m)

    optimal.print_result()

def compare_space_saving_to_optimal():
    pass


