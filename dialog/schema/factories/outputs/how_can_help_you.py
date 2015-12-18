from dialog.elements import Goto


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
        return {
            "@id": HowCanHelpYouOutput.__id(),
            (0, "prompt"): {
                "item": [
                    "How can I help you?",
                    "What can I do for you?"
                ],
                "@selectionType": "RANDOM"
            },
            (1, "getUserInput"): HowCanHelpYouInput.create()
        }
