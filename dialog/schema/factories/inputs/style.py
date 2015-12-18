from dialog.schema.elements import Goto, Input, Grammar
from dialog.schema.factories.action import StylePreferenceAction


class StylePreferenceInput:
    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceInput.__id())

    @staticmethod
    def __id():
        return "input_style_preference"

    @staticmethod
    def create(goto: Goto):
        return Input(
            _id=StylePreferenceInput.__id(),
            children=[
                Grammar(
                    items=[
                        "rated",  # TODO find out what they were thinking with this
                        "$(STYLE)={Style_Preference}"
                    ]
                ),
                StylePreferenceAction.set_to_value(),
                goto
            ]
        )
