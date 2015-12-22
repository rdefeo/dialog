import re
from enum import Enum


class GrammarItemMatchType(Enum):
    none = 1
    exact = 2


class GrammarItem:
    # def __init__(self):
    #     pass

    def _set_dialog(self, value):
        self.dialog = value


class RegExGrammarItem(GrammarItem):
    def __init__(self, pattern, dynamic_field_assignments: list = None, flags=re.IGNORECASE):
        self.dynamic_field_assignments = dynamic_field_assignments
        self.pattern = pattern
        self.flags = flags
