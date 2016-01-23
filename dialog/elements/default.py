from dialog.elements.output import Output
from dialog.elements.element import Element
from dialog.runners.conversation import Conversation


class Default(Element):
    _element_name = "default"

    def __init__(self, children=None):
        """

        """
        settings = {
        }

        super().__init__(settings, children)


    def _set_dialog(self, value):
        self.dialog = value
        if self.children is not None:
            for x in self.children:
                x._set_dialog(value)

    def create(self):
        doc = {}

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
                if isinstance(child, Output):
                    child.run(conversation)
                else:
                    # for now seems important to only have default on here
                    raise NotImplementedError(child)
                conversation.flow_position.pop()

        conversation.flow_position.pop()
