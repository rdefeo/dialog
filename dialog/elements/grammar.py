from dialog.elements.element import Element
from dialog.elements.grammar_item import RegExGrammarItem, EntityRegExGrammarItem, EntityGrammarItem
from dialog.runners.conversation import Conversation


class Grammar(Element):
    _element_name = "grammar"

    def __init__(self, watson_items: list = None, items: list = None):
        self.items = items
        self.watson_items = watson_items

    def _set_dialog(self, value):
        self.dialog = value
        if self.items is not None:
            for x in self.items:
                x.dialog = value

    def create(self):
        doc = {}

        if self.watson_items is not None:
            doc["item"] = self.watson_items

        return doc

    def run(self, conversation: Conversation):
        if self.items is not None:
            for grammar_item in self.items:
                if isinstance(grammar_item, RegExGrammarItem):
                    if grammar_item.run(conversation):
                        return True
                elif isinstance(grammar_item, EntityRegExGrammarItem):
                    if grammar_item.run(conversation):
                        return True
                elif isinstance(grammar_item, EntityGrammarItem):
                    if grammar_item.run(conversation):
                        return True
                else:
                    raise NotImplementedError(type(grammar_item))
            pass
        else:
            for x in self.watson_items:
                if x == conversation.user_input.strip():
                    return True

        return False