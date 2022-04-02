from algorithms.message import Message
from algorithms.space_saving.space_saving_algorithm import SpaceSavingAlgorithm
from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from data_generation.DataGenerator import DataGenerator
from tree_of_switches.binary_tree import BinaryTree

if __name__ == "__main__":

    binaryTree = BinaryTree(7)
    leaves = binaryTree.get_leaves()
    leaves[0].process_message(Message("a"))
    print("a")
