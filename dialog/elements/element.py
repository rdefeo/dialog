from dialog.process import ProcessRequest
from dialog.process.response import ProcessResponse

__author__ = 'robdefeo'


class Element:
    _element_name = None
    dialog = None
    settings = {}
    children = []
    
    def __init__(self, settings: dict, children: list):
        self.settings = settings
        self.children = children

    # @property
    # def dialog(self):
    #     return self.__dialog
    #
    # @dialog.setter
    # def dialog(self, value):
    #     raise NotImplemented()
    #
    def _set_dialog(self, value):
        raise NotImplemented()

    def create(self):
        raise NotImplemented()

    def process(self, process_request: ProcessRequest) -> ProcessResponse:
        raise NotImplemented()
