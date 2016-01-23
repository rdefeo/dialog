from dialog.elements.element import Element
from dialog.runners.conversation import Conversation
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

    def run(self, conversation: Conversation):
        from dialog.elements import Input, Goto, Folder

        goto_position = conversation.get_first_goto_position(self)
        conversation.flow_position.append(self._id)
        if goto_position is None:
            raise GetUserInputException(conversation, self)
        else:
            if goto_position == self._id:
                # so now it needs to look through the possible responses
                goto_position = conversation.get_first_goto_position(self)
            else:
                raise Exception()

            for index, child in enumerate(self.children):
                if goto_position is None or index >= goto_position:
                    conversation.flow_position.append(index)
                    if isinstance(child, Input):
                        # from dialog.runners.input import InputRunner
                        child.run(conversation)
                    elif isinstance(child, Goto):
                        child.run(conversation)
                    elif isinstance(child, Folder):
                        child.run(conversation)
                    else:
                        raise NotImplementedError(type(child))

                    conversation.flow_position.pop()

            conversation.flow_position.pop()

class GetUserInputException(Exception):
    def __init__(self, conversation: Conversation, get_user_input: GetUserInput):
        self.get_user_input = get_user_input
        self.conversation = conversation
        self.conversation.goto_position = list(self.conversation.flow_position)

