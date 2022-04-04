import random
from string import ascii_lowercase
from algorithms.message import Message


class DataGenerator:

    def __init__(self, keys_number, stream_size):
        self._keys_number = keys_number
        self._stream_size = stream_size
        self._keys = self._generate_keys()
        self._stream = []

    def _generate_keys(self):
        keys = []
        key_len = 5
        for i in range(self._keys_number):
            random_str = ''.join(random.choice(ascii_lowercase) for _ in range(key_len))
            keys.append(random_str)
        return keys

    def generate_stream(self) -> list:
        for i in range(self._stream_size):
            self._stream.append(Message(self._keys[random.randint(0, self._keys_number - 1)]))
        return self._stream

    def remove_random_keys(self, number_of_keys_to_remove):
        if number_of_keys_to_remove >= self._keys_number:
            raise Exception("too many keys to remove!!!")
        keys_to_remove = []
        prev_indexes = []
        for i in range(number_of_keys_to_remove):
            if len(prev_indexes) != 0:
                random_index = random.choice([i for i in range(0, self._keys_number) if i not in prev_indexes])
            else:
                random_index = random.randint(0, self._keys_number - 1)
            prev_indexes.append(random_index)
            keys_to_remove.append(self._keys[random_index])
        self._stream = [m for m in self._stream if (m._key not in keys_to_remove)]
        return self._stream, keys_to_remove

    @property
    def keys(self):
        return self._keys
