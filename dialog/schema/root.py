from dialog.schema.entities import Entities
from dialog.schema.flow import Flow
from dialog.schema.variables import Variables


class Dialog:
    def create(self):
        dialog = {
            "dialog": {
                "@xsi:noNamespaceSchemaLocation": "WatsonDialogDocument_1.0.xsd",
                "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                (0, "flow"): Flow().create(),
                (1, "entities"): Entities().create(),
                (2, "variables"): Variables().create()
            }
        }
        return dialog

    def save_file(self):
        print(self.create())
