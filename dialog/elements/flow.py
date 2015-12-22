from dialog.elements.folder import Folder
from dialog.elements.element import Element


class Flow(Element):
    _element_name = "flow"

    def __init__(self, folders: list = None):
        """
        Is a container for the main content of a dialog flow.
        :param folders: only <Folder>
        """
        self.folders = folders

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
