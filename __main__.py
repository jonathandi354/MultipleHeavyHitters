import random

from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from data_generation.DataGenerator import DataGenerator
from tree_of_switches.binary_tree import BinaryTree
from tree_of_switches.keys_distibutor.equally_level_distributor import EquallyLevelDistributor
from tree_of_switches.nodes.algorithm_node import AlgorithmNode
from tree_of_switches.nodes.node_factory import NodeFactory


def compare_node_top_k_and_optimal_top_k(k, optimal, node):
    optimal_top_k = optimal.get_top_k_keys(k)
    node_algorithm_top_k = node.get_top_k_keys(k)
    count = 0
    for optimal_top_key in optimal_top_k:
        if optimal_top_key not in node_algorithm_top_k:
            count += 1
    txt = "node: {} there are {} keys in top-{} optimal but not in top-{} algorithm".format(node.index, count, k, k)
    print(txt)


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

    for node in binaryTree.nodes:
        optimal_for_level = OptimalAlgorithm()
        for m in stream:
            if m.key in node.keys:
                optimal.process_message(m)
        compare_node_top_k_and_optimal_top_k(7, optimal, node)

