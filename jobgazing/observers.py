
from . import Database


class Observer:

    def __init__(self):
        self._db = Database()


class AIObserver(Observer):

    def __init__(self):
        super().__init__()

    def get_random(self):
        return self._db.get_enterprise(None)


class WebObserver(Observer):

    def __init__(self):
        super().__init__()
        raise NotImplemented('WebObserver is not yet implemented.')
