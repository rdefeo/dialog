from dialog.elements import Goto, Prompt, Output


class HowCanHelpYouOutput:
    @staticmethod
    def goto():
        return Goto(ref=HowCanHelpYouOutput.__id())

    @staticmethod
    def __id():
        return "output_how_can_i_help_you"

    @staticmethod
    def create():
        from dialog.schema.factories.inputs.how_can_i_help_you import HowCanHelpYouInput
        return Output(
            _id=HowCanHelpYouOutput.__id(),
            prompt=Prompt(
                items=[
                    "How can I help you?",
                    "What can I do for you?"
                ]
            ),
            children=[HowCanHelpYouInput.create()]
        )
