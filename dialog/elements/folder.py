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
        settings = {}
        if selection_type is not None:
            settings["selection_type"] = selection_type
        if label is not None:
            settings["label"] = label
        if _id is not None:
            settings["id"] = _id
        super().__init__(settings, list(children if children is not None else []))


    def _set_dialog(self, value):
        self.dialog = value
        for child in iter(self.children):
            child._set_dialog(value)

    def create(self):
        doc = {}

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]

        if "label" in self.settings:
            doc["@label"] = self.settings["label"]

        if "selection_type" in self.settings:
            doc["@selectionType"] = self.settings["selection_type"]

        if any(self.children):
            for i, child in enumerate(self.children):
                doc[(i, child._element_name)] = child

        return doc
