from dialog.schema.elements import Goto
from dialog.schema.factories.action import StylePreferenceAction


class StylePreferenceInput:
    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceInput.__id())

    @staticmethod
    def __id():
        return "input_style_preference"


    @staticmethod
    def create():
        return {
            "@id": StylePreferenceInput.__id(),
            (0, "grammar"): {
                "item": [
                    "rated",
                    "$(STYLE)={Style_Preference}"
                ]
            },
            (1, "action"): StylePreferenceAction.set_to_value(),
            (2, "goto"): Goto(ref="input_zipcode")
        }
