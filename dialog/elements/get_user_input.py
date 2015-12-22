from dialog.elements.element import Element
from typing import Iterable


class GetUserInput(Element):
    _element_name = "getUserInput"

    def __init__(self, _id: str = None, children: Iterable[Element] = None):
        """
            Contains the nodes that contain the system's response to users' input that cannot be matched to output in the dialog.
            :param _id: Specifies a unique ID that is used as an anchor point.
            :param children: any of action | cond | default | folder |function | getUserInput | goto |if | input | output | script | search
            """
        settings = {}
        if _id is not None:
            settings["id"] = _id

        super().__init__(settings, children)

    def _set_dialog(self, value):
        self.dialog = value
        if "id" in self.settings:
            self.dialog.ref_ids[self.settings["id"]] = self
        for child in iter(self.children):
            child._set_dialog(value)

    def create(self):
        doc = {}

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]

        if any(self.children):
            for i, child in enumerate(self.children):
                doc[(i, child._element_name)] = child

        return doc
