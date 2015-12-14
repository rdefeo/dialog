from dialog.schema.elements import Goto, Prompt
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
        return {
            "@id": StartSearch.__id(),
            (0, "prompt"): Prompt(
                items=["Would you like to find a specific style of shoe?"]
                # "Would you like to find a movie that's now playing or coming soon?"
            ),
            (1, "getUserInput"): {
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
                (1, "input"): {
                    (0, "grammar"): {
                        "item": [
                            "neither",
                            "neither",
                            "$ either",
                            "no"
                        ]
                    },
                    (1, "output"): {
                        (0, "prompt"): GenericPrompt.ok(),
                        (1, "goto"): HowCanHelpYouOutput.goto()
                    }
                },
                (2, "input"): {
                    (0, "grammar"): GenericGrammar.yes_okay(wildcard=False),
                    (1, "output"): {
                        (0, "prompt"): Prompt(
                            items=[
                                "Please tell me the style you would like then.",
                                "Ok great what style would you like?"
                            ]
                        ),
                        (1, "goto"): StylePreferenceProfileCheckInput.goto()
                    }
                },
                (3, "input"): {
                    (0, "grammar"): {
                        "item": [
                            "My name is",
                            "$ my name is",
                            "$ I am",
                            "$ I'm",
                            "$ called",
                            "$ call me",
                            "$ known as"
                        ]
                    },
                    (1, "output"): {
                        (0, "prompt"): Prompt(items=["Sorry."]),
                        (1, "goto"): Goto(ref="input_user_knownas_name")
                    }
                },
                (4, "goto"): PreliminarySequencesSearch.goto()
            }
        }
