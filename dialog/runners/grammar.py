from dialog.elements import Output, Prompt, GetUserInput, Input, Grammar
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation

from dialog.runners.prompt import PromptRunner
from dialog.elements.grammar_item import RegExGrammarItem

class GrammarRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, grammar: Grammar):
        if grammar.items is not None:
            from dialog.runners.grammar_item import RegExGrammarItemRunner

            for grammar_item in grammar.items:
                if isinstance(grammar_item, RegExGrammarItem):
                    if RegExGrammarItemRunner.run(dialog, conversation, grammar_item):
                        return True
                else:
                    raise NotImplemented(type(grammar_item))
            pass
        else:
            for x in grammar.watson_items:
                if x == conversation.user_input.strip():
                    return True

        return False
