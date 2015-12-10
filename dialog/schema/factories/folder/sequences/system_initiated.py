from dialog.schema.elements import Action, Goto
from dialog.schema.factories.action import TerminalExchangeAction, GreetingAction, SmallTalkAction, \
    RecencyPreferenceAction, GenrePreferenceAction, CertificationPreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYou
from dialog.schema.factories.prompts.generic import GenericPrompt

__author__ = 'robdefeo'


class SystemInitiatedSequences:
    @staticmethod
    def __id():
        return "output_help_with_anything_else"
    @staticmethod
    def goto():
        return Goto(ref=SystemInitiatedSequences.__id())
    @staticmethod
    def create():
        return {
            "@label": "SYSTEM INITIATED SEQUENCES",
            "output": [
                {
                    "@id": SystemInitiatedSequences.__id(),
                    (0, "prompt"): {
                        "item": "Is there anything else I can help you with?",
                        "@selectionType": "RANDOM"
                    },
                    (1, "action"): [
                        Action(varName="Page", operator="SET_TO", text="New").create(),
                        Action(varName="Current_Index", operator="SET_TO", text="0").create(),
                        CertificationPreferenceAction.set_to_blank(),
                        GenrePreferenceAction.set_to_blank(),
                        RecencyPreferenceAction.set_to_blank(),
                        Action(varName="Search_Now", operator="SET_TO_NO").create(),
                        Action(varName="Terminal_Exchange", operator="SET_TO_BLANK").create(),
                        Action(varName="Topic", operator="SET_TO_BLANK").create(),
                        Action(varName="ZIP_Code_Preference", operator="SET_TO_BLANK").create(),
                        Action(varName="Display_Trailer", operator="SET_TO_NO").create(),
                        Action(varName="Selected_Movie", operator="SET_TO_BLANK").create(),
                        Action(varName="Display_Movie_Details", operator="SET_TO_NO").create(),
                        Action(varName="Display_Reviews", operator="SET_TO_NO").create(),
                        Action(varName="Popularity_Score", operator="SET_TO", text="0.5").create()
                    ],
                    (2, "getUserInput"): {
                        (0, "input"): [
                            {
                                (0, "grammar"): GenericGrammar.yes(),
                                (1, "goto"): HowCanHelpYou.goto()
                            },
                            {
                                (0, "grammar"): GenericGrammar.no(),
                                (1, "output"): {
                                    (0, "prompt"): GenericPrompt.ok(),
                                    (1, "goto"): Goto(ref="output_did_find_what_looking_for")
                                }
                            }
                        ],
                        (1, "goto"): Goto(ref="search_preliminary_sequences")
                    }
                },
                {
                    (0, "prompt"): {
                        "item": "Did you find what you were looking for, {User_Name}?",
                        "@selectionType": "RANDOM"
                    },
                    (1, "getUserInput"): {
                        (0, "input"): [
                            {
                                (0, "grammar"): GenericGrammar().yes(),
                                (1, "action"): {
                                    "@varName": "Request_Success",
                                    "@operator": "SET_TO_YES"
                                },
                                (2, "output"): {
                                    (0, "prompt"): {
                                        "item": "Great!"
                                    },
                                    (1, "output"): {
                                        "@id": "output_goodbye",
                                        (0, "prompt"): {
                                            "item": "Goodbye.<br> <br>"
                                        },
                                        (1, "action"): [
                                            TerminalExchangeAction.set_to_yes(),
                                            GreetingAction.create_reset()
                                        ],
                                        (2, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": [
                                                        "Goodbye",
                                                        "$ goodbye"
                                                    ]
                                                },
                                                (1, "output"): {
                                                    "@id": "output_end_of_conversation",
                                                    (0, "prompt"): {
                                                        "item": "<i>Say anything to continue.</i>",
                                                        "@selectionType": "RANDOM"
                                                    },
                                                    (1, "getUserInput"): {
                                                        "output": {
                                                            "@id": "output_welcome_back",
                                                            (0, "prompt"): {
                                                                "item": "Welcome back!"
                                                            },
                                                            (1, "goto"): HowCanHelpYou.goto()
                                                        }
                                                    }
                                                }
                                            },
                                            (1, "goto"):HowCanHelpYou.goto()
                                        }
                                    }
                                }
                            },
                            {
                                (0, "grammar"): GenericGrammar.no(),
                                (1, "action"): {
                                    "@varName": "Request_Success",
                                    "@operator": "SET_TO_NO"
                                },
                                (2, "output"): {
                                    (0, "prompt"): {
                                        "item": "Oh no. Do you want to try again?"
                                    },
                                    (1, "getUserInput"): {
                                        "input": [
                                            {
                                                (0, "grammar"): GenericGrammar.no(),
                                                (1, "action"): TerminalExchangeAction.set_to_no(),
                                                (2, "output"): {
                                                    (0, "prompt"): GenericPrompt.ok(),
                                                    (1, "goto"): {
                                                        "@ref": "output_goodbye"
                                                    }
                                                }
                                            },
                                            {
                                                (0, "grammar"): GenericGrammar.yes(),
                                                (1, "output"): {
                                                    (0, "prompt"): {
                                                        "item": "Okay. What can I do for you?"
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "getUserInput_how_can_i_help_you"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ],
                        (1, "goto"): Goto(ref="search_preliminary_sequences")
                    },
                    "@id": "output_did_find_what_looking_for"
                },
                {
                    "@id": "output_too_much_small_talk",
                    (0, "prompt"): {
                        "item": "This is fun, but wouldn't you like to look up some movies?",
                        "@selectionType": "RANDOM"
                    },
                    (1, "getUserInput"): {
                        (0, "input"): [
                            {
                                (0, "grammar"): GenericGrammar.yes(),
                                (1, "goto"): Goto(ref="output_ask_for_recency")
                            },
                            {
                                (0, "grammar"): GenericGrammar.no(),
                                (1, "action"): SmallTalkAction.set_to_zero(),
                                (2, "output"): {
                                    "prompt": GenericPrompt.ok_fine()
                                }
                            },
                            {
                                (0, "grammar"): GenericGrammar.ok(),
                                (1, "goto"): Goto(ref="output_ask_for_recency")
                            }
                        ],
                        (1, "goto"): Goto(ref="search_preliminary_sequences")
                    }
                }
            ]
        }
