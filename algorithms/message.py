import uuid


class Message:

    def __init__(self, key: str):
        self._key = key
        self._id = uuid.uuid4()

    @property
    def key(self) -> str:
        return self._key
