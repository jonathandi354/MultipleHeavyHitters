from abc import ABCMeta, abstractmethod
from .message import Message


class IHeavyHittersAlgorithm:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_message(self, message: Message):
        raise NotImplementedError

    @abstractmethod
    def get_counters(self):
        raise NotImplementedError

    @abstractmethod
    def get_top_k_keys(self, k):
        raise NotImplementedError
