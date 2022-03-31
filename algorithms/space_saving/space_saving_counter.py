class SpaceSavingCounter:

    def __init__(self, key):
        self._over_estimation = 0
        self._approximated_frequency = 0
        self._key = key

    def increment(self):
        self._approximated_frequency += 1

    def get_count(self) -> int:
        return self._over_estimation + self._approximated_frequency

    @property
    def key(self) -> str:
        return self._key()

    @key.setter
    def key(self, new_key):
        self._key = new_key
        self._over_estimation += self._approximated_frequency
        self._approximated_frequency = 0

