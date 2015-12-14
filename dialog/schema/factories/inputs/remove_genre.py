from dialog.schema.elements import Goto
from dialog.schema.factories.action import PageAction


class RemoveGenreInput:
    @staticmethod
    def goto():
        return Goto(ref=RemoveGenreInput.__id())

    @staticmethod
    def __id():
        return "input_remove_genre"

    @staticmethod
    def create():
        return {
            "@id": RemoveGenreInput.__id(),
            (0, "grammar"): {
                "item": [
                    "Remove genre",
                    "$ remove (GENRE)={Genre_Preference}",
                    "$ cancel (GENRE)={Genre_Preference}",
                    "$ remove genre",
                    "$ cancel genre",
                    "$ any genre",
                    "$ all genre"
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
                    "@varName": "Genre_Preference",
                    "@operator": "SET_TO_BLANK"
                }
            ],
            (2, "goto"):  Goto(ref="output_ok_do_search")
        }
