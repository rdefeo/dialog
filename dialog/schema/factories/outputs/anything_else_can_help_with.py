from dialog.schema.elements import Goto
from dialog.schema.factories.action import TerminalExchangeAction, RequestSuccessAction, TopicAction, \
    CertificationPreferenceAction, RecencyPreferenceAction, ColorPreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.prompts.generic import GenericPrompt


class AnythingElseCanHelpWith:
    @staticmethod
    def goto():
        return Goto(ref=AnythingElseCanHelpWith.__id())

    @staticmethod
    def __id():
        return "output_anything_else_can_help_with"

    @staticmethod
    def create():
        from dialog.schema.factories.inputs import AfterSearchResults

        return {
            "@id": AnythingElseCanHelpWith.__id(),
            (0, "prompt"): {
                "item": "Is there anything else I can help you with?"
            },
            (1, "getUserInput"): {
                (0, "input"): [
                    {
                        (0, "grammar"): {
                            "item": [
                                "Go back",
                                "$ go back",
                                "$ wait",
                                "$ not done",
                                "$ not finished"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): GenericPrompt.ok(),
                            (1, "goto"): AfterSearchResults.goto()
                        }
                    },
                    {
                        (0, "grammar"): GenericGrammar.yes(),
                        (1, "action"): [
                            RequestSuccessAction.set_to_blank(),
                            TerminalExchangeAction.set_to_blank(),
                            TopicAction.set_to_blank(),
                            CertificationPreferenceAction.set_to_blank(),
                            ColorPreferenceAction.set_to_blank(),
                            RecencyPreferenceAction.set_to_blank()
                        ],
                        (2, "goto"): HowCanHelpYouOutput.goto()
                    },
                    {
                        (0, "grammar"): GenericGrammar.no(),
                        (1, "output"): {
                            (0, "prompt"): GenericGrammar.ok(),
                            (1, "goto"): Goto(ref="output_did_find_what_looking_for")
                        }
                    }
                ],
                (1, "goto"): {
                    "@ref": "input_2456878"
                }
            }
        }
