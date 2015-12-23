from dialog.elements import Goto, Output, Grammar, Input, GetUserInput, Prompt
from dialog.schema.factories.action import TerminalExchangeAction, RequestSuccessAction, TopicAction, \
    RecencyPreferenceAction, ColorPreferenceAction, StylePreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
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

        return Output(
            _id=AnythingElseCanHelpWith.__id(),
            prompt=Prompt(
                items=["Is there anything else I can help you with?"]
            ),
            children=[
                GetUserInput(
                    children=[
                        Input(
                            Grammar(
                                watson_items=[
                                    "Go back",
                                    "$ go back",
                                    "$ wait",
                                    "$ not done",
                                    "$ not finished"
                                ]
                            ),
                            children=[
                                Output(
                                    GenericPrompt.ok(),
                                    children=[AfterSearchResults.goto()]
                                )
                            ]
                        ),
                        Input(
                            GenericGrammar.yes(),
                            children=[
                                RequestSuccessAction.set_to_blank(),
                                TerminalExchangeAction.set_to_blank(),
                                TopicAction.set_to_blank(),
                                StylePreferenceAction.set_to_blank(),
                                ColorPreferenceAction.set_to_blank(),
                                RecencyPreferenceAction.set_to_blank()
                            ]
                        ),
                        Input(
                            GenericGrammar.no(),
                            children=[
                                Output(
                                    GenericGrammar.ok(),
                                    children=[Goto(ref="output_did_find_what_looking_for")]
                                )
                            ]
                        ),
                        Goto(ref="input_2456878")
                    ]

                )
            ]
        )
