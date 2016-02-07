from dialog.elements.action import Action
from dialog.elements.input import Input
from dialog.elements.goto import Goto
from dialog.elements.get_user_input import GetUserInput
from dialog.elements.prompt import Prompt
from dialog.elements.element import Element
from dialog.runners.conversation import Conversation


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

    def run(self, conversation: Conversation):
        conversation.flow_position.append(self._id)
        goto_position = conversation.get_first_goto_position(self)
        if goto_position is not None:
            if goto_position == self._id:
                goto_position = conversation.get_first_goto_position(self)
            else:
                raise Exception()

        for index, child in enumerate(self.children):
            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                if isinstance(child, Prompt):
                    child.run(conversation)
                elif isinstance(child, GetUserInput):
                    child.run(conversation)
                elif isinstance(child, Output):
                    child.run(conversation)
                elif isinstance(child, Goto):
                    child.run(conversation)
                elif isinstance(child, Input):
                    child.run(conversation)
                elif isinstance(child, Action):
                    child.run(conversation)
                else:
                    raise NotImplementedError(child)
                conversation.flow_position.pop()

        conversation.flow_position.pop()
