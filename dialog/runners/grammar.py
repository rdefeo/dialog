from dialog.elements import Output, Prompt, GetUserInput, Input, Grammar
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation

from dialog.runners.prompt import PromptRunner


class GrammarRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, grammar: Grammar):
        for x in grammar.items:
            if x == conversation.user_input.strip():
                return True

        return False
