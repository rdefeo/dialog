from dialog.elements.grammar import Grammar
from dialog.elements.element import Element
from dialog.runners.conversation import Conversation
from typing import Iterable


class Input(Element):
    _element_name = "input"

    def __init__(self, grammar: Grammar, children: Iterable[Element] = None, _id: str = None):
        """
        Contains the nodes that contain the text that users submit.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param children: any of action | concept | default | folder | function | getUserInput | goto | grammar | if | input | output | search
        """
        self.grammar = grammar
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
        children = [self.grammar] + self.children
        if any(children):
            for i, child in enumerate(children):
                doc[(i, child._element_name)] = child

        return doc

    def run(self, conversation: Conversation):
        from dialog.elements.goto import Goto
        from dialog.elements.output import Output
        from dialog.elements.action import Action

        handled = False
        conversation.flow_position.append(self._id)
        goto_position = conversation.get_first_goto_position(self)
        if goto_position is not None:
            if goto_position == self._id:
                goto_position = conversation.get_first_goto_position(self)
            else:
                raise Exception()
        if self.grammar.run(conversation):
            for index, child in enumerate(self.children):
                if goto_position is None or index >= goto_position:
                    conversation.flow_position.append(index)
                    if isinstance(child, Action):
                        child.run(conversation)
                    elif isinstance(child, Output):
                        child.run(conversation)
                    elif isinstance(child, Goto):
                        child.run(conversation)
                    else:
                        raise NotImplementedError(type(child))
                    conversation.flow_position.pop()

            handled = True

        conversation.flow_position.pop()
        return handled