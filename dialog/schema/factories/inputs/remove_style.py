from dialog.elements import Goto, Grammar, Input
from dialog.schema.factories.action import PageAction, CurrentIndexAction, StylePreferenceAction


class RemoveStyleInput:
    @staticmethod
    def create():
        return Input(
            Grammar(
                watson_items=[
                    "Remove rating",
                    "$ remove (STYLE)={Style_Preference}",
                    "$ cancel (STYLE)={Style_Preference}",
                    "$ remove style",
                    "$ cancel style",
                    "$ all styles",
                    "$ all style",
                    "$ any styles",
                    "$ any style"
                ]
            ),
            children=[
                CurrentIndexAction.set_to_zero(),
                PageAction.set_to_new(),
                StylePreferenceAction.set_to_blank(),
                Goto(ref="output_ok_do_search")
            ]
        )
