from dialog.elements.element import Element
from typing import Iterable


class Folder(Element):
    _element_name = "folder"

    def __init__(self, _id: str = None, label: str = None, selection_type=None, children: Iterable[Element] = None):
        """
        Node groups content.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param label: Specifies a unique name for a node.
        :param children: action | autoLearnVariations | concept | default | folder | function | getUserInput | goto | if | input | output | random | search
        """
        self.selection_type = selection_type
        self.label = label
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

        if self.label is not None:
            doc["@label"] = self.label

        if self.selection_type is not None:
            doc["@selectionType"] = self.selection_type

        if any(self.children):
            for i, child in enumerate(self.children):
                doc[(i, child._element_name)] = child

        return doc
