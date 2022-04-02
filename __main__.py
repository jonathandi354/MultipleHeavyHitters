from algorithms.space_saving.space_saving_algorithm import SpaceSavingAlgorithm
from algorithms.optimal_algorithm.optimal_algorithm import OptimalAlgorithm
from data_generation.DataGenerator import DataGenerator
from tree_of_switches.binary_tree import BinaryTree

if __name__ == "__main__":

    data_generator = DataGenerator(26, 150)
    stream = data_generator.generate_stream()

    algo = SpaceSavingAlgorithm(7)
    for m in stream:
        algo.process_message(m)

    counters = algo.get_counters()
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in counters:
        print(txt.format(c, counters[c]._approximated_frequency, counters[c]._over_estimation, counters[c].get_count()))

    print("less keys:")

    try:
        stream_with_less_keys, removed_keys = data_generator.remove_random_keys(2)
    except Exception as e:
        print(e)
    algo.clear()

    for m in stream_with_less_keys:
        algo.process_message(m)

    print("removed keys: {}", removed_keys)
    counters = algo._counters_dict
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in counters:
        print(txt.format(c, counters[c]._approximated_frequency, counters[c]._over_estimation, counters[c].get_count()))

    print("optimal:")
    algo = OptimalAlgorithm()

    for m in stream:
        algo.process_message(m)

    counters = sorted(algo.get_counters().items(), key=lambda a: a[1], reverse=True)

    txt = "key: {}, freq: {}"
    for c in counters:
        print(txt.format(c[0], c[1]))

    binaryTree = BinaryTree()
