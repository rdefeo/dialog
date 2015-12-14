from dialog.schema.elements import Goto
from dialog.schema.factories.action import PageAction


class RemoveAllSearchCriteriaInput:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "all movies",
                    "$ all movies",
                    "$ all results"
                ]
            },
            (1, "action"): [
                {
                    "@varName": "Current_Index",
                    "@operator": "SET_TO",
                    "#text": "0"
                },
                PageAction.set_to_new(),
                {
                    "@varName": "Certification_Preference",
                    "@operator": "SET_TO_BLANK"
                },
                {
                    "@varName": "Genre_Preference",
                    "@operator": "SET_TO_BLANK"
                }
            ],
            (2, "goto"):  Goto(ref="output_ok_do_search")
        }
