import random
from abc import ABCMeta, abstractmethod
from string import ascii_lowercase
from algorithms.message import Message

'''
Generates a random datastream of generated messages.
'''


class DataGenerator:

    __metaclass__ = ABCMeta

    def __init__(self, keys_number, stream_size):
        self._keys_number = keys_number
        self._stream_size = stream_size

    @abstractmethod
    def generate_stream(self) -> list:
        raise NotImplementedError

