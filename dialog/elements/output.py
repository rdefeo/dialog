from dialog.elements.get_user_input import GetUserInput
from dialog.elements._if import If
from dialog.elements.prompt import Prompt
from dialog.elements.goto import Goto
from dialog.elements.element import Element
from dialog.process import ProcessRequest


class Output(Element):
    _element_name = "output"

    def __init__(self, prompt: Prompt, children = None, _id: str = None, is_insert_DNR_statement=False):

        """
        Contains the nodes that contain the system's response to user input.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param children: any of default | folder | function | getUserInput | goto | if | input | output | prompt | random | search

        Typically looks like prompt then get user input
        """

        if prompt is None:
            raise Exception()
        self.prompt = prompt
        if children is not None:
            self.children = [self.prompt] + children
        else:
            self.children = [self.prompt]

        self.is_insert_DNR_statement = is_insert_DNR_statement
        self.id = _id

    def _set_dialog(self, value):
        self.dialog = value
        self.prompt._set_dialog(value)
        for x in self.children:
            x._set_dialog(value)

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if self.is_insert_DNR_statement:
            doc["@isInsertDNRStatement"] = "true"

        for i, child in enumerate(self.children):
            doc[(i, child._element_name)] = child

        return doc

    def process(self, process_request: ProcessRequest):
        prompt = list(self.children)[0]
        if not isinstance(prompt, Prompt):
            raise Exception("grammar not the first item")
