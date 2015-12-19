from dialog.elements import Grammar, Action
from dialog.elements.element import Element
from dialog.process import ProcessRequest
from dialog.process.grammar_response import GrammarMatchType
from typing import Iterable


class Input(Element):
    _element_name = "input"

    def __init__(self, _id: str = None, children: Iterable[Element] = None):
        """
        Contains the nodes that contain the text that users submit.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param children: any of action | concept | default | folder | function | getUserInput | goto | grammar | if | input | output | search
        """
        self.children = children
        self.id = _id

    def _set_dialog(self, value):
        self.dialog = value
        for child in iter(self.children):
            child._set_dialog(value)

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if any(self.children):
            for i, child in enumerate(self.children):
                doc[(i, child._element_name)] = child

        return doc

    def process(self, process_request: ProcessRequest):
        grammar = list(self.children)[0]
        if not isinstance(grammar, Grammar):
            raise Exception("grammar not the first item")

        if grammar.process(process_request).match_type == GrammarMatchType.exact:
            response = {}
            response["actions"] = []
            for child in iter(self.children[1:]):
                if isinstance(child, Action):
                    response["actions"].append(child.process(process_request))
                else:

                    pass

            return response
        else:
            return None
