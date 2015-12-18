from enum import Enum

from dialog.process.response import ProcessResponse


class GrammarMatchType(Enum):
    none = 1
    exact = 2


class GrammarProcessResponse(ProcessResponse):
    def __init__(self, match_type: GrammarMatchType): 
        self.match_type = match_type
