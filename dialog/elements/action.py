from dialog.elements.element import Element
from dialog.process import ProcessRequest
from dialog.process.action_response import ActionProcessResponse

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

    def __init__(self, varName=None, operator=None, text=None):
        self.varName = varName
        self.operator = operator
        self.text = text

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}
        if self.varName is not None:
            doc["@varName"] = self.varName
        if self.operator is not None:
            doc["@operator"] = self.operator
        if self.text is not None:
            doc["#text"] = self.text

        return doc

    def process(self, process_request: ProcessRequest):
        if self.operator == ACTION_SET_TO_NO:
            new_value = False
        elif self.operator == ACTION_SET_TO_YES:
            new_value = True
        else:
            raise Exception("unknown operator=%s", self.operator)

        process_request.profile[self.varName] = new_value
        return ActionProcessResponse(self.varName, new_value)
        # look in profile for variable and perform the action

