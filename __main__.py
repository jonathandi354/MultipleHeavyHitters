from algorithms.space_saving.space_saving_algorithm import SpaceSavingAlgorithm
from algorithms.message import Message
if __name__ == "__main__":
    algo = SpaceSavingAlgorithm(3)
    messages = []
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("a"))
    messages.append(Message("a"))
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("c"))
    messages.append(Message("c"))
    messages.append(Message("d"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    messages.append(Message("d"))
    messages.append(Message("d"))
    messages.append(Message("c"))
    messages.append(Message("e"))
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("c"))


    for m in messages:
        algo.process_message(m)


    #counters = algo.get_counters().values()
    dict = algo.counters_dict
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in dict:
        print(txt.format(c, dict[c].approximated_frequency, dict[c].over_estimation, dict[c].get_count()))

    print("without d:")

    algo = SpaceSavingAlgorithm(3)
    messages = []
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("a"))
    messages.append(Message("a"))
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("c"))
    messages.append(Message("c"))
    # messages.append(Message("d"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    messages.append(Message("e"))
    # messages.append(Message("d"))
    # messages.append(Message("d"))
    messages.append(Message("c"))
    messages.append(Message("e"))
    messages.append(Message("a"))
    messages.append(Message("b"))
    messages.append(Message("c"))

    for m in messages:
        algo.process_message(m)


    #counters = algo.get_counters().values()
    dict = algo.counters_dict
    txt = "key: {}, approximated-freq: {}, over-estimation: {}, total-count: {}"
    for c in dict:
        print(txt.format(c, dict[c].approximated_frequency, dict[c].over_estimation, dict[c].get_count()))
