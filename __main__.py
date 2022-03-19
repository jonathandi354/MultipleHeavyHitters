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

    counters = algo.get_counters().values()
    dict = {}
    for c in counters:
        dict[c.key] = c.get_count()

    print(dict)
