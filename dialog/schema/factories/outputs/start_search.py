from dialog.schema.elements import Goto
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYou
from dialog.schema.factories.prompts.generic import GenericPrompt


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
            (0, "prompt"): {
                "item": "Would you like to find a movie that's now playing or coming soon?",
                "@selectionType": "RANDOM"
            },
            (1, "getUserInput"): {
                (0, "input"): [
                    {
                        (0, "grammar"): {
                            "item": "$ (DATE_TIME_RANGE)={DateTime_Mentioned_ENT}"
                        },
                        (1, "action"): {
                            "@varName": "DateTime_Current",
                            "@operator": "SET_TO",
                            "#text": "<mct:getTime>America/Tijuana</mct:getTime>"
                        },
                        (2, "goto"): Goto(ref="input_date_time")
                    },
                    {
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
                            (1, "goto"): HowCanHelpYou.goto()
                        }
                    },
                    {
                        (0, "grammar"): GenericGrammar.yes_okay(),
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "Something that's now playing or coming soon?",
                                "@selectionType": "RANDOM"
                            },
                            (1, "goto"): {
                                "@ref": "getUserInput_2414745"
                            }
                        }
                    },
                    {
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
                            (0, "prompt"): {
                                "item": "Sorry.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "goto"): {
                                "@ref": "input_user_knownas_name"
                            }
                        }
                    }
                ],
                (1, "goto"): {
                    "@ref": "search_preliminary_sequences"
                }
            }
        }
