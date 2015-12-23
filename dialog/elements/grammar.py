from dialog.elements.element import Element


class Grammar(Element):
    _element_name = "grammar"

    def __init__(self, watson_items: list = None, items: list = None):
        self.items = items
        self.watson_items = watson_items

    def _set_dialog(self, value):
        self.dialog = value

    def create(self):
        doc = {}

        if self.watson_items is not None:
            doc["item"] = self.watson_items

        return doc

        # def process(self, process_request: ProcessRequest) -> GrammarProcessResponse:
        #     for x in iter(self.watson_items):
        #         if x == process_request.user_text_input:
        #             return GrammarProcessResponse(GrammarMatchType.exact)
        #
        #     return GrammarProcessResponse(GrammarMatchType.none)
