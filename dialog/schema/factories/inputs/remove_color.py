from dialog.elements import Goto, Grammar, Input
from dialog.schema.factories.action import PageAction, CurrentIndexAction, ColorPreferenceAction


class RemoveColorInput:
    @staticmethod
    def goto():
        return Goto(ref=RemoveColorInput.__id())

    @staticmethod
    def __id():
        return "input_remove_color"

    @staticmethod
    def create():
        return Input(
            _id=RemoveColorInput.__id(),
            grammar=Grammar(
                watson_items=[
                    "Remove genre",
                    "$ remove (COLOR)={Color_Preference}",
                    "$ cancel (COLOR)={Color_Preference}",
                    "$ remove color",
                    "$ cancel color",
                    "$ any color",
                    "$ all color"
                ]
            ),
            children=[
                CurrentIndexAction.set_to_zero(),
                PageAction.set_to_new(),
                ColorPreferenceAction.set_to_blank(),
                Goto(ref="output_ok_do_search")
            ]
        )
