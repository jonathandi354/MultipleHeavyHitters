import uuid


class Message:

    def __init__(self, key: str):
        self.key = key
        self.id = uuid.uuid4()
