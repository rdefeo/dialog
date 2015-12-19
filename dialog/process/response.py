from enum import Enum


class ProcessResponseStatus(Enum):
    handled = 1
    not_handled = 2


class ProcessResponse:
    def __init__(self, handled: ProcessResponseStatus):
        self.handled = handled
