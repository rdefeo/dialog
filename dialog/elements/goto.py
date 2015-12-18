from dialog.elements.element import Element


class Goto(Element):
    _element_name = "goto"

    def __init__(self, ref=None):
        self.ref = ref

    def create(self):
        doc = {}

        if self.ref is not None:
            doc["@ref"] = self.ref

        return doc