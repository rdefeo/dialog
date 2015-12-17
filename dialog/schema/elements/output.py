from dialog.schema.elements.element import Element
from typing import Iterable


class Output(Element):
    _element_name = "output"

    def __init__(self, _id: str = None, children: Iterable[Element] = None, ):
        """
        Contains the nodes that contain the system's response to user input.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param children: any of default | folder | function | getUserInput | goto | if | input | output | prompt | random | search
        """
        self.children = children
        self.id = _id

    def create(self):
        doc = {}

        if self.id is not None:
            doc["@id"] = self.id

        if any(self.children):
            for i, child in enumerate(self.children):
                doc[(i, child._element_name)] = child

        return doc