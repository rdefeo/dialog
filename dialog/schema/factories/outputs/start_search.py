from dialog.elements import Goto, Prompt, Grammar, Output, Input, GetUserInput
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.profile_checks.style_preference import StylePreferenceProfileCheckInput
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch


class StartSearch:
    @staticmethod
    def goto():
        return Goto(ref=StartSearch.__id())

    @staticmethod
    def __id():
        return "output_start_search"

    @staticmethod
    def create():
        return Output(
            _id=StartSearch.__id(),
            prompt=Prompt(
                items=["Would you like to find a specific style of shoe?"]
                # "Would you like to find a movie that's now playing or coming soon?"
            ),
            children=[
                GetUserInput(
                    children=[
                        # TODO Not sure how this is useful
                        # (0, "input"): {
                        #     (0, "grammar"): {
                        #         "item": "$ (DATE_TIME_RANGE)={DateTime_Mentioned_ENT}"
                        #     },
                        #     (1, "action"): {
                        #         "@varName": "DateTime_Current",
                        #         "@operator": "SET_TO",
                        #         "#text": "<mct:getTime>America/Tijuana</mct:getTime>"
                        #     },
                        #     (2, "goto"): Goto(ref="input_date_time")
                        # },
                        Input(
                            children=[
                                Grammar(
                                    items=[
                                        "neither",
                                        "neither",
                                        "$ either",
                                        "no"
                                    ]
                                ),
                                Output(
                                    prompt=GenericPrompt.ok(),
                                    children=[HowCanHelpYouOutput.goto()]
                                )
                            ]
                        ),
                        Input(
                            children=[
                                GenericGrammar.yes_okay(wildcard=False),
                                Output(
                                    Prompt(
                                        items=[
                                            "Please tell me the style you would like then.",
                                            "Ok great what style would you like?"
                                        ]
                                    ),
                                    children=[StylePreferenceProfileCheckInput.goto()]
                                )
                            ]
                        ),
                        Input(
                            children=[
                                Grammar(
                                    items=[
                                        "My name is",
                                        "$ my name is",
                                        "$ I am",
                                        "$ I'm",
                                        "$ called",
                                        "$ call me",
                                        "$ known as"
                                    ]
                                ),
                                Output(
                                    prompt=Prompt(items=["Sorry."]),
                                    children=[
                                        Goto(ref="input_user_knownas_name")
                                    ]
                                )
                            ]
                        ),
                        PreliminarySequencesSearch.goto()
                    ]
                )
            ]
        )
