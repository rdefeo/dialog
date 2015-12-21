from dialog.elements.element import Element


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
