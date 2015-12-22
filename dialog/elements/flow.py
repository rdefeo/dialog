from dialog.elements.element import Element
from typing import Iterable


class Flow(Element):
    _element_name = "flow"

    def __init__(self, folders: Iterable[Element] = None):
        """
        Is a container for the main content of a dialog flow.
        :param folders: only <Folder>
        """
        self.folders = list(folders)

    def _set_dialog(self, value):
        self.dialog = value
        for folder in iter(self.folders):
            folder._set_dialog(value)

    def create(self):
        doc = {}

        if any(self.folders):
            for i, folder in enumerate(self.folders):
                doc[(i, folder._element_name)] = folder

        return doc
