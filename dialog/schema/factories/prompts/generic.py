from dialog.schema.elements import Prompt

__author__ = 'robdefeo'


class GenericPrompt:
    @staticmethod
    def ok():
        return Prompt(
            items=["Okay."]
        )

    @staticmethod
    def ok_fine():
        return Prompt(
            items=["Okay, fine."]
        )

    @staticmethod
    def what_is_your_name():
        return Prompt(
            selection_type="SEQUENTIAL",
            items=[
                "What can I call you?",
                "What's your name?"
            ]
        )
