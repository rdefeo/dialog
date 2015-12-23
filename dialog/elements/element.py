from bson import ObjectId
from dialog.process import ProcessRequest
from dialog.process.response import ProcessResponse


class Element:
    _element_name = None
    dialog = None
    settings = {}
    children = []
    _id = None
    
    def __init__(self, settings: dict, children: list):
        self.settings = settings
        self.children = children
        self._id = ObjectId()

    # @property
    # def dialog(self):
    #     return self.__dialog
    #
    # @dialog.setter
    # def dialog(self, value):
    #     raise NotImplemented()
    #
    def _set_dialog(self, value):
        raise NotImplemented(self._element_name)

    def create(self):
        raise NotImplemented()

