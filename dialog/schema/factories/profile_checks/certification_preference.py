from dialog.schema.elements import Goto
from dialog.schema.factories.action import CertificationPreferenceAction
from dialog.schema.factories.conditions import CertificationsConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.search import PreliminarySequencesSearch


class CertificationPreferenceProfileCheck:
    @staticmethod
    def create():
        return {
            "@id": "profileCheck_certification_preference",
            (0, "cond"): CertificationsConditions.is_blank(),
            (1, "output"): {
                (0, "prompt"): {
                    "item": "Do you prefer a certain movie rating? ",
                    "@selectionType": "RANDOM"
                },
                (1, "if"): {
                    (0, "cond"): {
                        "@varName": "First_Time",
                        "@operator": "EQUAL_TO_YES"
                    },
                    (1, "output"): {
                        (0, "prompt"): {
                            "item": "<mct:link><b><mct:input>G</mct:input></b></mct:link>\n<mct:link><b><mct:input>PG</mct:input></b></mct:link>\n<mct:link><b><mct:input>PG-13</mct:input></b></mct:link>\n<mct:link><b><mct:input>R</mct:input></b></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): {
                            "@ref": "getUserInput_2443780"
                        }
                    }
                },
                (2, "getUserInput"): {
                    "@id": "getUserInput_2443780",
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
                                        "ratings",
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
                                        "item": "G, PG, PG-13, R or NR <br> <br>",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "goto"): {
                                        "@ref": "getUserInput_2443780"
                                    }
                                }
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Rating",
                                    "$ (CERTIFICATION)={Certification_Preference}"
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
                                CertificationPreferenceAction.set_to_value()
                            ],
                            (2, "goto"):  Goto(ref="output_ok_do_search")
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "NC-17",
                                    "$ NC-17"
                                ]
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "I'm afraid I cannot look up NC-17-rated movies.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): {
                                    "@ref": "getUserInput_2443780"
                                }
                            }
                        },
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
                                (0, "prompt"): {
                                    "item": "Which one?"
                                },
                                (1, "goto"): {
                                    "@ref": "getUserInput_2443780"
                                }
                            }
                        }
                    ],
                    (1, "goto"): PreliminarySequencesSearch.goto()
                }
            }
        }
