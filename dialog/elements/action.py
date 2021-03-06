from dialog.elements.element import Element
from dialog.runners.conversation import Conversation

__author__ = 'robdefeo'

ACTION_APPEND = "APPEND"
ACTION_DECREMENT_BY = "DECREMENT_BY"
ACTION_DO_NOTHING_STR = "DO_NOTHING_STR"
ACTION_INCREMENT_BY = "INCREMENT_BY"
ACTION_NO = "NO"
ACTION_SET_AS_USER_INPUT = "SET_AS_USER_INPUT"
ACTION_SET_TO = "SET_TO"
ACTION_SET_TO_BLANK = "SET_TO_BLANK"
ACTION_SET_TO_NO = "SET_TO_NO"
ACTION_SET_TO_USER_INPUT = "SET_TO_USER_INPUT"
ACTION_SET_TO_USER_INPUT_CORRECTED = "SET_TO_USER_INPUT_CORRECTED"
ACTION_SET_TO_YES = "SET_TO_YES"
ACTION_YES = "YES"


class Action(Element):
    _element_name = "action"

    def __init__(self, var_name, operator, text=None):
        settings = {
            "var_name": var_name,
            "operator": operator
        }
        children = []
        super().__init__(settings, children)
        if text is not None:
            settings["text"] = text

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}
        if "var_name" in self.settings:
            doc["@varName"] = self.settings["var_name"]
        if "operator" in self.settings:
            doc["@operator"] = self.settings["operator"]
        if "text" in self.settings:
            doc["#text"] = self.settings["text"]

        return doc

    @property
    def operator(self):
        return self.settings["operator"]

    @property
    def var_name(self):
        return self.settings["var_name"]

    def run(self, conversation: Conversation):
        if self.operator == ACTION_SET_TO:
            if "{" in self.settings["text"] and "}" in self.settings["text"]:
                input_context_key = self.settings["text"].strip("{").strip("}").strip(".source")
                conversation.profile[self.var_name] = conversation.current_input_context[self.var_name]
            else:
                conversation.profile[self.var_name] = self.settings["text"]

            pass
        elif self.operator == ACTION_SET_TO_NO:
            conversation.profile[self.var_name] = False
        elif self.operator == ACTION_SET_TO_YES:
            conversation.profile[self.var_name] = True
        else:
            raise NotImplemented()

