from dialog.elements.entities import Entities
from dialog.elements.flow import Flow
from dialog.elements.element import Element
from typing import Iterable


class Dialog(Element):
    _element_name = "folder"

    def __init__(self, flow: Flow = None, entities: Entities=None):
        """
        Node defines a top-level container for the dialog that you design.
        :param flow: flow
        :param entities: entities
         # |  | reports | settings | variables
        """
        self.__entities = entities
        self.flow = flow
        if self.flow is not None:
            self.flow = flow
            self.flow._set_dialog(self)
        else:
            raise Exception("flow needed")

    @property
    def entities(self):
        return self.__entities

    # def create(self):
    #     doc = {}
    #
    #     if any(self.children):
    #         for i, child in enumerate(self.children):
    #             doc[(i, child._element_name)] = child
    #
    #     return doc
