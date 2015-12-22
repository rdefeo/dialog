from enum import Enum
import re

class GrammarItemMatchType(Enum):
    none = 1
    exact = 2


class GrammarItem:
    # def __init__(self):
    #     pass

    def _set_dialog(self, value):
        self.dialog = value


class RegExGrammarItem(GrammarItem):
    def __init__(self, pattern):
        self.pattern = pattern
