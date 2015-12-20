from dialog.elements.get_user_input import GetUserInput
from dialog.elements._if import If
from dialog.elements.prompt import Prompt
from dialog.elements.goto import Goto
from dialog.elements.element import Element
from dialog.process import ProcessRequest


class Output(Element):
    _element_name = "output"

    def __init__(self, prompt: Prompt, _if: If = None, output: Element = None, get_user_input: GetUserInput = None,
                 goto: Goto = None,
                 _id: str = None, is_insert_DNR_statement=False
                 ):

        """
        Contains the nodes that contain the system's response to user input.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param children: any of default | folder | function | getUserInput | goto | if | input | output | prompt | random | search

        Typically looks like prompt then get user input
        """

        if prompt is None:
            raise Exception()
        self.prompt = prompt
        self._if = _if
        self.output = output
        self.goto = goto
        self.get_user_input = get_user_input

        self.is_insert_DNR_statement = is_insert_DNR_statement
        self.id = _id

    def _set_dialog(self, value):
        self.dialog = value
        self.prompt._set_dialog(value)
        if self._if is not None:
            self._if._set_dialog(value)

        if self.goto is not None:
            self.goto._set_dialog(value)

        if self.output is not None:
            self.output._set_dialog(value)

        if self.get_user_input is not None:
            self.get_user_input._set_dialog(value)

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if self.is_insert_DNR_statement:
            doc["@isInsertDNRStatement"] = "true"

        children = []
        children.append(self.prompt)
        if self._if is not None:
            children.append(self._if)
        if self.output is not None:
            children.append(self.output)
        if self.get_user_input is not None:
            children.append(self.get_user_input)
        if self.goto is not None:
            children.append(self.goto)

        for i, child in enumerate(children):
            doc[(i, child._element_name)] = child

        return doc

    def process(self, process_request: ProcessRequest):
        prompt = list(self.children)[0]
        if not isinstance(prompt, Prompt):
            raise Exception("grammar not the first item")
