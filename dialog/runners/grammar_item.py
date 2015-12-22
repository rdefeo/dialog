from dialog.elements.dialog import Dialog
from dialog.elements.grammar_item import GrammarItem, RegExGrammarItem
from dialog.runners.conversation import Conversation
import re


class RegExGrammarItemRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, grammar_item: RegExGrammarItem):
        search_response = re.search(grammar_item.pattern, conversation.user_input)


        return False


