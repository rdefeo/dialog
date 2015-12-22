from dialog.elements.dialog import Dialog
from dialog.elements.grammar_item import GrammarItem, RegExGrammarItem
from dialog.runners.conversation import Conversation
import re


class RegExGrammarItemRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, grammar_item: RegExGrammarItem):
        matches = re.findall(grammar_item.pattern, conversation.user_input, grammar_item.flags)
        if not any(matches):
            return False
        elif any(matches) and grammar_item.dynamic_field_assignments is None:
            return True
        elif len(matches) == len(grammar_item.dynamic_field_assignments):
            assignments = zip(grammar_item.dynamic_field_assignments, matches)
            conversation.current_input_context = {}
            for key, value in assignments:
                conversation.current_input_context[key] = value
            return True
        else:
            return False


