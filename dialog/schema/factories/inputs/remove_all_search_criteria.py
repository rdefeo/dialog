from dialog.schema.elements import Goto


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
                {
                    "@varName": "Page",
                    "@operator": "SET_TO",
                    "#text": "new"
                },
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
