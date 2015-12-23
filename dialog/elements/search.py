from dialog.elements.element import Element


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
