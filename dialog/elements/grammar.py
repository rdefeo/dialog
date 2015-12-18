from dialog.elements.element import Element
from dialog.process import ProcessRequest, GrammarProcessResponse
from dialog.process.grammar_response import GrammarMatchType


class Grammar(Element):
    _element_name = "grammar"

    def __init__(self, items: list = None):
        self.items = items

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}

        if self.items is not None:
            doc["item"] = self.items

        return doc

    def process(self, process_request: ProcessRequest) -> GrammarProcessResponse:
        for x in iter(self.items):
            if x == process_request.user_text_input:
                return GrammarProcessResponse(GrammarMatchType.exact)

        return GrammarProcessResponse(GrammarMatchType.none)
