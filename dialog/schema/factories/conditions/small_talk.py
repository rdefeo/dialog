from dialog.elements import If, Condition, Goto

__author__ = 'robdefeo'


class SmallTalkConditions:
    @staticmethod
    def too_much_small_talk_goto():
        return If(
            elements=[
                Condition(name="Small_Talk_Count", operator="GREATER_THEN", root_text="2"),
                Goto(ref="output_too_much_small_talk")
            ]
        )


