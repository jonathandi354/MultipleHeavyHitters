import random
from decimal import Decimal
from string import ascii_lowercase
from algorithms.message import Message
from data_generation.DataGenerator import DataGenerator


class UnevenDataGenerator(DataGenerator):

    def __init__(self, keys_number, stream_size, probabilities: list):
        DataGenerator.__init__(self, keys_number, stream_size)
        self._keys = self._generate_keys()
        self._stream = []
        self._probabilities = probabilities
        if not self._validate_probabilities_list():
            raise Exception(
                "probability list doesn't sum to 1 or probabilities list size doesn't divide number of keys!")

    def _validate_probabilities_list(self) -> bool:
        count = 0
        for i in self._probabilities:
            count += i
        return abs(count - 1) < 0.0001 and len(self._keys) % len(self._probabilities) == 0

    '''
    Generates a list from a certain size of random keys.
    '''

    def _generate_keys(self) -> list:
        keys = []
        key_len = 5
        for i in range(self._keys_number):
            random_str = ''.join(random.choice(ascii_lowercase) for _ in range(key_len))
            keys.append(random_str)
        return keys

    def _match_probability_to_keys(self):
        self._expand_probabilities_list()
        key_to_probability = {}
        for i in range(len(self._keys)):
            key_to_probability[self._keys[i]] = self._probabilities[i]

    def _expand_probabilities_list(self):
        expansion_factor = int(len(self._keys) / len(self._probabilities))
        new_probabilities_list = []
        for prob in self._probabilities:
            for i in range(expansion_factor):
                new_probabilities_list.append(prob / expansion_factor)
        self._probabilities = new_probabilities_list



    def generate_stream(self) -> list:
        self._expand_probabilities_list()
        for i in range(self._stream_size):
            self._stream.append(Message(random.choices(self._keys, self._probabilities)[0]))
        random.shuffle(self._stream)
        return self._stream

    # def remove_random_keys(self, number_of_keys_to_remove):
    #    if number_of_keys_to_remove >= self._keys_number:
    #        raise Exception("too many keys to remove!!!")
    #    keys_to_remove = []
    #    prev_indexes = []
    #    for i in range(number_of_keys_to_remove):
    #        if len(prev_indexes) != 0:
    #            random_index = random.choice([i for i in range(0, self._keys_number) if i not in prev_indexes])
    #        else:
    #            random_index = random.randint(0, self._keys_number - 1)
    #        prev_indexes.append(random_index)
    #        keys_to_remove.append(self._keys[random_index])
    #    self._stream = [m for m in self._stream if (m.key not in keys_to_remove)]
    #    return self._stream, keys_to_remove

    @property
    def keys(self) -> list:
        return self._keys
