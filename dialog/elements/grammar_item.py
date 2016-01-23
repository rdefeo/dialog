import re
from enum import Enum

from dialog.runners.conversation import Conversation


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

    def run(self, conversation: Conversation):
        matches = re.findall(self.pattern, conversation.user_input, self.flags)
        if not any(matches):
            return False
        elif any(matches) and self.dynamic_field_assignments is None:
            return True
        elif len(matches) == len(self.dynamic_field_assignments):
            assignments = zip(self.dynamic_field_assignments, matches)
            conversation.current_input_context = {}
            for key, value in assignments:
                conversation.current_input_context[key] = value
            return True
        else:
            return False


class EntityGrammarItem(GrammarItem):
    def __init__(self, dynamic_field_assignment: str = None, entity_id: str = None):
        self.entity_id = entity_id
        self.dynamic_field_assignment = dynamic_field_assignment

    def run(self, conversation: Conversation):
        if self.entity_id not in self.dialog.entity_dict:
            raise Exception()
        entity_grammar = self.dialog.entity_dict[self.entity_id]
        search_term = conversation.user_input.strip().lower()
        if search_term in entity_grammar:
            conversation.current_input_context = {
                self.dynamic_field_assignment: entity_grammar[search_term].value
            }
            return True
        else:
            return False


class EntityRegExGrammarItem(GrammarItem):
    def __init__(self, pattern, dynamic_field_assignments: list = None, entity_id: str = None, flags=re.IGNORECASE):
        self.entity_id = entity_id
        self.dynamic_field_assignments = dynamic_field_assignments
        self.pattern = pattern
        self.flags = flags

    def run(self, conversation: Conversation):
        matches = re.findall(self.pattern, conversation.user_input, self.flags)
        if not any(matches):
            return False
        elif any(matches) and self.dynamic_field_assignments is None:
            return True
        elif len(matches) == len(self.dynamic_field_assignments):
            assignments = zip(self.dynamic_field_assignments, matches)
            current_input_context = {}
            for key, value in assignments:
                current_input_context[key] = value

            conversation.current_input_context = current_input_context
            return True
        else:
            return False
