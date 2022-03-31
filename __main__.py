from algorithms.space_saving.space_saving_algorithm import SpaceSavingAlgorithm
from algorithms.message import Message
from data_generation.DataGenerator import  DataGenerator

if __name__ == "__main__":

    data_generator = DataGenerator(8, 35)
    stream = data_generator.generate_stream()

    algo = SpaceSavingAlgorithm(3)
    for m in stream:
        algo.process_message(m)



    dict = algo._counters_dict
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in dict:
        print(txt.format(c, dict[c]._approximated_frequency, dict[c]._over_estimation, dict[c].get_count()))

    print("less keys:")

    try:
        stream_with_less_keys = data_generator.remove_random_keys(1)
    except:
        print("error")
    algo.clear()

    for m in stream_with_less_keys:
        algo.process_message(m)


    #counters = algo.get_counters().values()
    dict = algo._counters_dict
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in dict:
        print(txt.format(c, dict[c]._approximated_frequency, dict[c]._over_estimation, dict[c].get_count()))
