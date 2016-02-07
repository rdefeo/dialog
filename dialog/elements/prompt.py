from random import choice

from dialog.elements.dialog import Dialog
from dialog.elements.element import Element
from dialog.runners.conversation import Conversation
from typing import Iterable


class Prompt(Element):
    _element_name = "prompt"

    def __init__(self, selection_type="RANDOM", items: Iterable[str] = None):
        settings = {
            "selection_type": selection_type
        }
        super().__init__(settings, [])
        self.items = items

    def create(self):
        doc = {}

        if "selection_type" in self.settings:
            doc["@selectionType"] = self.settings["selection_type"]

        if self.items is not None:
            doc["item"] = self.items

        return doc

    def _set_dialog(self, value):
        self.dialog = value

    @property
    def selection_type(self):
        return self.settings["selection_type"]

    def run(self, conversation: Conversation):
        if self.selection_type == "RANDOM":
            self.dialog.write_to_user(conversation, choice(self.items))
        else:
            raise NotImplemented()