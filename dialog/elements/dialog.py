from dialog.elements.entities import Entities
from dialog.elements.element import Element


class Dialog(Element):
    from dialog.elements.flow import Flow
    _element_name = "dialog"
    entity_dict = {}

    def __init__(self, flow: Flow = None, entities: Entities = None, variables=None):
        """
            Node defines a top-level container for the dialog that you design.
            :param flow: flow
            :param entities: entities
             # |  | reports | settings | variables
            """
        settings = {
            "@xsi:noNamespaceSchemaLocation": "WatsonDialogDocument_1.0.xsd",
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }

        super().__init__(settings, [flow, entities])
        self.variables = variables


        if entities is not None:
            self.entities = entities.entities
            for entity in self.entities:
                self.entity_dict[entity.name] = {}
                for value in entity.values:
                    for x in value.grammar.items:
                        self.entity_dict[entity.name][x] = value




        self.ref_ids = {}
        if flow is not None:
            self.flow = flow
            self.flow._set_dialog(self)
        else:
            raise Exception("flow needed")

