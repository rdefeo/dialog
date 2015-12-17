from dialog.schema.elements import Goto, Prompt
from dialog.schema.factories.action import ColorPreferenceAction, PageAction
from dialog.schema.factories.conditions import ColorConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.search import PreliminarySequencesSearch


class ColorPreferenceProfileCheck:
    @staticmethod
    def __id():
        return "profileCheck_color_preference"

    @staticmethod
    def goto():
        return Goto(ref=ColorPreferenceProfileCheck.__id())

    @staticmethod
    def create():
        return {
            "@id": ColorPreferenceProfileCheck.__id(),
            (0, "cond"): ColorConditions.is_blank(),
            (1, "output"): {
                (0, "prompt"): Prompt(items=["Do you prefer a certain color?"]),
                (1, "if"): {
                    (0, "cond"): {
                        "@varName": "First_Time",
                        "@operator": "EQUAL_TO_YES"
                    },
                    (1, "output"): {
                        (0, "prompt"): {
                            "item": "<mct:link><b><mct:input>Black</mct:input></b></mct:link>\n<mct:link><b><mct:input>White</mct:input></b></mct:link>\n<mct:link><b><mct:input>Red</mct:input></b></mct:link>\n<mct:link><b><mct:input>Green</mct:input></b></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): ColorPreferenceProfileCheckInput.goto()
                    }
                },
                (2, "getUserInput"): ColorPreferenceProfileCheckInput.create()
            }
        }


class ColorPreferenceProfileCheckInput:
    @staticmethod
    def __id():
        return "getUserInput_profileCheck_color_preference"

    @staticmethod
    def goto():
        return Goto(ref=ColorPreferenceProfileCheckInput.__id())

    @staticmethod
    def create():
        return {
            "@id": ColorPreferenceProfileCheckInput.__id(),
            (0, "input"): [
                {
                    (0, "grammar"): {
                        "item": [
                            "What",
                            "$ what",
                            "$ which",
                            "$ tell me"
                        ]
                    },
                    (1, "input"): {
                        (0, "grammar"): {
                            "item": [
                                "colors",
                                "$ they",
                                "$ ones",
                                "$ choices",
                                "$ options",
                                "$ ratings",
                                "$ certifications",
                                "$ what else"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "Black, White, Red, Brown or Green <br> <br>",
                                "@selectionType": "RANDOM"
                            },
                            (1, "goto"): ColorPreferenceProfileCheckInput.goto()
                        }
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Color",
                            "$ (COLOR)={Color_Preference}"
                        ]
                    },
                    (1, "action"): [
                        {
                            "@varName": "Current_Index",
                            "@operator": "SET_TO",
                            "#text": "0"
                        },
                        PageAction.set_to_new(),
                        {
                            "@varName": "Search_Now",
                            "@operator": "SET_TO_NO"
                        },
                        ColorPreferenceAction.set_to_value()
                    ],
                    (2, "goto"): Goto(ref="output_ok_do_search")
                },
                # TODO NOT SUPPORTED PATH
                # {
                #     (0, "grammar"): {
                #         "item": [
                #             "NC-17",
                #             "$ NC-17"
                #         ]
                #     },
                #     (1, "output"): {
                #         (0, "prompt"): {
                #             "item": "I'm afraid I cannot look up NC-17-rated movies.",
                #             "@selectionType": "RANDOM"
                #         },
                #         (1, "goto"): {
                #             "@ref": "getUserInput_2443780a"
                #         }
                #     }
                # },
                {
                    (0, "grammar"): {
                        "item": [
                            "No",
                            "$ don't care",
                            "$ don't know",
                            "$ no preference",
                            "$ no",
                            "$ none",
                            "$ all",
                            "$ any",
                            "$ anything",
                            "$ whatever",
                            "$ nothing specific",
                            "$ don't have a preference"
                        ]
                    },
                    (1, "action"): [
                        {
                            "@varName": "Current_Index",
                            "@operator": "SET_TO",
                            "#text": "0"
                        },
                        PageAction.set_to_new()
                    ],
                    (2, "goto"): {
                        "@ref": "output_2456875"
                    }
                },
                {
                    (0, "grammar"): GenericGrammar.yes_okay(wildcard=False),
                    (1, "output"): {
                        (0, "prompt"): {
                            "item": "Which one?"
                        },
                        (1, "goto"): ColorPreferenceProfileCheckInput.goto()
                    }
                }
            ],
            (1, "goto"): PreliminarySequencesSearch.goto()
        }
