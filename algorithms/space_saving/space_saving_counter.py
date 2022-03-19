class SpaceSavingCounter:

    def __init__(self):
        self.over_estimation = 0
        self.approximated_frequency = 0
        self.key = ''

    def increment(self):
        self.approximated_frequency += 1

    def get_count(self) -> int:
        return self.over_estimation + self.approximated_frequency

    def set_key(self, key: str):
        self.key = key

    def swap_key(self, new_key: str):
        self.set_key(new_key)
        self.over_estimation += self.approximated_frequency
        self.approximated_frequency = 0
