from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, GenrePreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYou

__author__ = 'robdefeo'


class ShowtimesInput:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "Showtimes",
                    "$ showtimes",
                    "$ what theaters",
                    "$ where is * playing",
                    "$ where is * showing",
                    "$ fandango"
                ]
            },
            (1, "action"): [
                GenrePreferenceAction.create_set_to_value(),
                GreetingAction.create_reset(),
                SmallTalkAction.create_reset()
            ],
            (2, "input"): [
                {
                    (0, "grammar"): {
                        "item": [
                            "near me",
                            "$ (ZIPCODE)={ZIP_Code_Preference}",
                            "$ near me",
                            "$ by me",
                            "$ my area",
                            "$ what theaters",
                            "$ where is * playing",
                            "$ where is * showing"
                        ]
                    },
                    (1, "action"): {
                        "@varName": "ZIP_Code_Preference",
                        "@operator": "SET_TO",
                        "#text": "{ZIP_Code_Preference.value:main}"
                    },
                    (2, "goto"): {
                        "@ref": "input_2510077"
                    }
                },
                {
                    "@id": "input_2510077",
                    (0, "grammar"): {
                        "item": "$ (ZIPCODE)={ZIP_Code_Preference}"
                    },
                    (1, "output"): {
                        (0, "prompt"): "",
                        (1, "action"): {
                            "@varName": "ZIP_Code_Preference",
                            "@operator": "SET_TO",
                            "#text": "{ZIP_Code_Preference.source}"
                        },
                        (2, "goto"): Goto(ref="profileCheck_zipcode")
                    }
                }
            ],
            (3, "if"): {
                "@id": "profileCheck_zipcode",
                (0, "cond"): {
                    "@varName": "ZIP_Code_Preference",
                    "@operator": "IS_BLANK"
                },
                (1, "output"): {
                    "@id": "output_2503331",
                    (0, "prompt"): {
                        "item": "What's your ZIP code?"
                    },
                    (1, "getUserInput"): {
                        "@id": "getUserInput_2503332",
                        (0, "input"): [
                            {
                                (0, "grammar"): {
                                    "item": [
                                        "zipcode",
                                        "$(ZIPCODE)={ZIP_Code_Preference}"
                                    ]
                                },
                                (1, "action"): {
                                    "@varName": "ZIP_Code_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{ZIP_Code_Preference.source}"
                                },
                                (2, "goto"): {
                                    "@ref": "output_2503344"
                                }
                            },
                            {
                                (0, "grammar"): {
                                    "item": [
                                        "I don't know it",
                                        "$ don't know",
                                        "$ don't have"
                                    ]
                                },
                                (1, "output"): {
                                    (0, "prompt"): {
                                        "item": "I'm afraid I can only use ZIP codes to find movies."
                                    },
                                    (1, "getUserInput"): {
                                        "input": {
                                            (0, "grammar"): {
                                                "item": "Okay"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_help_with_anything_else"
                                            }
                                        }
                                    }
                                }
                            },
                            {
                                (0, "grammar"): {
                                    "item": "Okay"
                                },
                                (1, "goto"): {
                                    "@ref": "output_help_with_anything_else"
                                }
                            }
                        ],
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "I don't think that's a ZIP code. Please only type 5 numbers."
                            },
                            (1, "goto"): {
                                "@ref": "getUserInput_2503332"
                            }
                        }
                    }
                }
            },
            (4, "output"): {
                "@id": "output_2503344",
                (0, "prompt"): {
                    "item": "Okay. <a target=\"@blank\" href=\"http://www.fandango.com/{ZIP_Code_Preference}_movietimes?q={ZIP_Code_Preference}\">Click here</a> to get show times for the {ZIP_Code_Preference} area."
                },
                (1, "getUserInput"): {
                    "@id": "getUserInput_2503345",
                    (0, "input"): [
                        {
                            "@id": "input_2503346",
                            (0, "grammar"): {
                                "item": "Okay"
                            },
                            (1, "output"): {
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
                                                (0, "prompt"): {
                                                    "item": "Okay."
                                                },
                                                (1, "goto"): {
                                                    "@ref": "getUserInput_2503345"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": "Yes"
                                            },
                                            (1, "action"): [
                                                {
                                                    "@varName": "Request_Success",
                                                    "@operator": "SET_TO_BLANK"
                                                },
                                                {
                                                    "@varName": "Terminal_Exchange",
                                                    "@operator": "SET_TO_BLANK"
                                                },
                                                {
                                                    "@varName": "Topic",
                                                    "@operator": "SET_TO_BLANK"
                                                }
                                            ],
                                            (2, "goto"): HowCanHelpYou.goto()
                                        },
                                        {
                                            (0, "grammar"): GenericGrammar.no(),
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": "Okay."
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_did_find_what_looking_for"
                                                }
                                            }
                                        }
                                    ],
                                    (1, "goto"): {
                                        "@ref": "input_2503346"
                                    }
                                }
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Zipcode",
                                    "$ (ZIPCODE)={ZIP_Code_Preference}"
                                ]
                            },
                            (1, "action"): {
                                "@varName": "ZIP_Code_Preference",
                                "@operator": "SET_TO",
                                "#text": "{ZIP_Code_Preference.source}"
                            },
                            (2, "goto"): {
                                "@ref": "output_2503344"
                            }
                        }
                    ],
                    (1, "goto"): {
                        "action": {
                            "@varName": "ZIP_Code_Preference",
                            "@operator": "SET_TO_BLANK"
                        },
                        "@ref": "search_preliminary_sequences"
                    }
                }
            }
        }
