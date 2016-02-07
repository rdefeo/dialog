from dialog.elements.dialog import Dialog
from dialog.elements.element import Element
from dialog.runners.conversation import Conversation


class Search(Element):
    _element_name = "search"

    def __init__(self, ref: str, _id: str = None):
        """
        Tells the system where to find the output that matches the input.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param ref: Specifies a reference ID that matches an anchor point.

        """
        settings = {
            "ref": ref
        }

        if _id is not None:
            settings["id"] = _id

        super().__init__(settings, [])


    def _set_dialog(self, value):
        self.dialog = value
        if "id" in self.settings:
            self.dialog.ref_ids[self.settings["id"]] = self
        if self.children is not None:
            for x in self.children:
                x._set_dialog(value)

    @property
    def ref(self):
        return self.settings["ref"]

    def create(self):
        doc = {}

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]


        doc["@ref"] = self.settings["ref"]

        for i, child in enumerate(self.children):
            doc[(i, child._element_name)] = child

        return doc

    def run(self, conversation: Conversation):
        from dialog.elements import Prompt, GetUserInput, Output, Goto, Action, Input

        conversation.flow_position.append(self._id)
        goto_position = conversation.get_first_goto_position(self)
        if goto_position is not None:
            if goto_position == self._id:
                goto_position = conversation.get_first_goto_position(self)
            else:
                raise Exception()

        search_object = self.dialog.ref_ids[self.ref]
        input_handled = False
        for index, child in enumerate(search_object.children):
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
                elif isinstance(child, Action):
                    child.run(conversation)
                elif isinstance(child, Input):
                    if not input_handled:
                        input_handled = child.run(conversation)
                else:
                    raise NotImplementedError(child)
                conversation.flow_position.pop()

        conversation.flow_position.pop()
