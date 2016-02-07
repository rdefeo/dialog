from dialog.elements.element import Element
from dialog.runners.conversation import Conversation


class GotoException(Exception):
    def __init__(self, conversation):
        self.converstaion = conversation


class Goto(Element):
    _element_name = "goto"

    def __init__(self, ref=None):
        self.ref = ref

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}

        if self.ref is not None:
            doc["@ref"] = self.ref

        return doc

    def run(self, conversation: Conversation):
        conversation.flow_position = []
        conversation.flow_goto_position = self.ref
        if self.ref in self.dialog.ref_ids:
            goto_object = self.dialog.ref_ids[self.ref]
            raise GotoException(conversation)


        else:
            raise Exception("can not find,id=%s" % self.ref)
