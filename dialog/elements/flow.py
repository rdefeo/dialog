from dialog.elements.element import Element
from dialog.runners.conversation import Conversation
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

    def run(self, conversation: Conversation):
        # conversation.flow_position.append(flow._id)
        goto_position = conversation.get_first_goto_position(self)
        for index, folder in enumerate(self.folders):
            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                folder.run(conversation)
                conversation.flow_position.pop()
