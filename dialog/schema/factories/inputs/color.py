from dialog.schema.elements import Goto
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
        return {
            "@id": ColorPreferenceInput.__id(),
            (0, "grammar"): {
                "item": [
                    "rated",  # TODO find out what they were thinking with this
                    "$(Color)={Color_Preference}"
                ]
            },
            (1, "action"): ColorPreferenceAction.set_to_value(),
            (2, "goto"): goto
        }
