from dialog.elements import Goto, Input, Grammar
from dialog.schema.factories.action import ColorPreferenceAction


class ColorPreferenceInput:
    @staticmethod
    def goto():
        return Goto(ref=ColorPreferenceInput.__id())

    @staticmethod
    def __id():
        return "input_color_preference"

    @staticmethod
    def create(goto: Goto):
        return Input(
            Grammar(
                    items=[
                        "rated",  # TODO find out what they were thinking with this
                        "$(Color)={Color_Preference}"
                    ]
                ),
            _id=ColorPreferenceInput.__id(),
            children=[
                ColorPreferenceAction.set_to_value(),
                goto
            ]
        )
