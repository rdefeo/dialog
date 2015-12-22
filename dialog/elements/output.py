from dialog.elements.prompt import Prompt
from dialog.elements.element import Element
from dialog.process import ProcessRequest


class Output(Element):
    _element_name = "output"

    def __init__(self, prompt: Prompt, children=None, _id: str = None, is_insert_DNR_statement=False):
        """
            Contains the nodes that contain the system's response to user input.
            :param _id: Specifies a unique ID that is used as an anchor point.
            :param children: any of default | folder | function | getUserInput | goto | if | input | output | prompt | random | search

            Typically looks like prompt then get user input
            """
        settings = {
            "is_insert_DNR_statement": is_insert_DNR_statement
        }
        if _id is not None:
            settings["id"] = _id

        if children is not None:
            children = [prompt] + children
        else:
            children = [prompt]

        super().__init__(settings, children)

        if prompt is None:
            raise Exception()
        self.prompt = prompt

    def _set_dialog(self, value):
        self.dialog = value
        if "id" in self.settings:
            self.dialog.ref_ids[self.settings["id"]] = self

        if self.children is not None:
            for x in self.children:
                x._set_dialog(value)

    def create(self):
        doc = {}

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]

        if self.settings["is_insert_DNR_statement"]:
            doc["@isInsertDNRStatement"] = "true"

        for i, child in enumerate(self.children):
            doc[(i, child._element_name)] = child

        return doc

    def process(self, process_request: ProcessRequest):
        prompt = list(self.children)[0]
        if not isinstance(prompt, Prompt):
            raise Exception("grammar not the first item")

        for x in self.children:
            pass
