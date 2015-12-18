from dialog.elements import Goto
from dialog.schema.factories.action import PageAction


class RemoveRatingInput:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "Remove rating",
                    "$ remove (CERTIFICATION)={Certification_Preference}",
                    "$ cancel (CERTIFICATION)={Certification_Preference}",
                    "$ remove rating",
                    "$ cancel rating",
                    "$ all ratings",
                    "$ all rating",
                    "$ any ratings",
                    "$ any rating"
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
                }
            ],
            (2, "goto"):  Goto(ref="output_ok_do_search")
        }
