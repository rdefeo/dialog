from dialog.schema.elements import Goto, Prompt
from dialog.schema.factories.action import CertificationPreferenceAction, StylePreferenceAction
from dialog.schema.factories.conditions.style import StyleConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.search import PreliminarySequencesSearch


class StylePreferenceProfileCheck:
    @staticmethod
    def __id():
        return "profileCheck_style_preference"

    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceProfileCheck.__id())

    @staticmethod
    def create():
        return {
            "@id": StylePreferenceProfileCheck.__id(),
            (0, "cond"): StyleConditions.is_blank(),
            (1, "output"): {
                (0, "prompt"): Prompt(items=["Do you prefer a style? "]),
                (1, "if"): {
                    (0, "cond"): {
                        "@varName": "First_Time",
                        "@operator": "EQUAL_TO_YES"
                    },
                    (1, "output"): {
                        (0, "prompt"): {
                            "item": "<mct:link><b><mct:input>High heels</mct:input></b></mct:link>\n<mct:link><b><mct:input>Boots</mct:input></b></mct:link>\n<mct:link><b><mct:input>Sandals</mct:input></b></mct:link>\n<mct:link><b><mct:input>Trainers</mct:input></b></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): StylePreferenceProfileCheckInput.goto()
                    }
                },
                (2, "getUserInput"): StylePreferenceProfileCheckInput.create()
            }
        }


class StylePreferenceProfileCheckInput:
    @staticmethod
    def __id():
        return "getUserInput_profileCheck_style_preference"

    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceProfileCheckInput.__id())

    @staticmethod
    def create():
        return {
            "@id": StylePreferenceProfileCheckInput.__id(),
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
                                "styles",
                                "$ they",
                                "$ ones",
                                "$ choices",
                                "$ options",
                                "$ styles",
                                "$ what else"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): Prompt(items=["For example.... Boots, High heels, Sandals, Trainers or Flats <br> <br>"]),
                            (1, "goto"): StylePreferenceProfileCheckInput.goto()
                        }
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Rating",
                            "$ (Style)={Style_Preference}"
                        ]
                    },
                    (1, "action"): [
                        {
                            "@varName": "Current_Index",
                            "@operator": "SET_TO",
                            "#text": "0"
                        },
                        {
                            "@varName": "Page",
                            "@operator": "SET_TO",
                            "#text": "new"
                        },
                        {
                            "@varName": "Search_Now",
                            "@operator": "SET_TO_NO"
                        },
                        StylePreferenceAction.set_to_value()
                    ],
                    (2, "goto"): Goto(ref="output_ok_do_search")
                },
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
                #         (1, "goto"): StylePreferenceProfileCheckInput.goto()
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
                        {
                            "@varName": "Page",
                            "@operator": "SET_TO",
                            "#text": "new"
                        }
                    ],
                    (2, "goto"): {
                        "@ref": "output_2456875"
                    }
                },
                {
                    (0, "grammar"): GenericGrammar.yes(),
                    (1, "output"): {
                        (0, "prompt"): Prompt(items=["Which one?"]),
                        (1, "goto"): StylePreferenceProfileCheckInput.goto()
                    }
                }
            ],
            (1, "goto"): PreliminarySequencesSearch.goto()
        }
