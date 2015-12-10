from dialog.schema.elements import Condition, If, Goto
from dialog.schema.factories.action import GreetingAction
from dialog.schema.factories.grammar import GenericGrammar, FeelingGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class OpeningSequences:
    @staticmethod
    def create():
        return {
            "@selectionType": "RANDOM",
            "@label": "OPENING SEQUENCES",
            (0, "input"): [
                {
                    (0, "grammar"): GenericGrammar.create_hello(),
                    (1, "action"): GreetingAction.create_increment(),
                    (2, "if"): [
                        If(
                            elements=[
                                Condition(name="Terminal_Exchange", operator="EQUAL_TO_YES"),
                                Goto(ref="output_welcome_back")
                            ]
                        ),
                        If(
                            match_type="ANY",
                            elements=[
                                Condition(name="Greeting_Count", operator="GREATER_THEN", root_text="2"),
                                Condition(name="Small_Talk_Count", operator="GREATER_THEN", root_text="2"),
                                Goto(ref="output_end_of_small_talk")
                            ]
                        )
                    ],
                    (3, "output"): {
                        (0, "prompt"): {
                            "item": [
                                "Hello.",
                                "Hi.",
                                "Hi there."
                            ],
                            "@selectionType": "RANDOM"
                        },
                        (1, "output"): {
                            "@id": "output_2459184",
                            (0, "prompt"): {
                                "item": [
                                    "How are you today?",
                                    "How are you feeling today?",
                                    "How is it going?"
                                ],
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): [
                                    {
                                        (0, "grammar"): {
                                            "item": [
                                                "Movies",
                                                "$ (GENRE)={Genre_Preference}",
                                                "$ (CERTIFICATION)={Certification_Preference}",
                                                "$ (RECENCY)={Recency_Preference}",
                                                "$ movies"
                                            ]
                                        },
                                        (1, "goto"): Goto(ref="input_main_search_criteria")
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_not_so_good(),
                                        (1, "goto"): Goto(ref="output_sorry_to_hear_that")
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_not_so_bad(),
                                        (1, "goto"): Goto(ref="output_good_to_hear")
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_fine(),
                                        (1, "output"): {
                                            "@id": "output_good_to_hear",
                                            (0, "prompt"): {
                                                "item": "Good to hear! <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): HowCanHelpYouOutput.goto()
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_great(),
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "Fantastic! So glad to hear it. <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): HowCanHelpYouOutput.goto()
                                        }
                                    },
                                    {
                                        (0, "grammar"): FeelingGrammar.create_feeling_bad(),
                                        (1, "output"): {
                                            "@id": "output_sorry_to_hear_that",
                                            (0, "prompt"): {
                                                "item": "I'm sorry to hear that. <br> <br>",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): HowCanHelpYouOutput.goto()
                                        }
                                    }
                                ],
                                (1, "goto"): PreliminarySequencesSearch.goto()
                            }
                        }
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "How are you",
                            "$ how have you been doing",
                            "$ how is it going",
                            "$ how are you",
                            "$ what's shaking",
                            "$ what's up"
                        ]
                    },
                    (1, "action"): GreetingAction.create_increment(),
                    (2, "if"): {
                        (0, "cond"): [
                            Condition(name="Greeting_Count", operator="GREATER_THEN", root_text="2"),
                            Condition(name="Small_Talk_Count", operator="GREATER_THEN", root_text="2"),
                        ],
                        (1, "output"): {
                            "@id": "output_end_of_small_talk",
                            (0, "prompt"): {
                                "item": "You're very polite, but don't you want me to look up movies for you?",
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
                                        (1, "action"): GreetingAction.create_reset(),
                                        (2, "output"): {
                                            "prompt": GenericPrompt.ok_fine()
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): Goto(ref="output_ask_for_recency")
                                    }
                                ],
                                (1, "goto"): PreliminarySequencesSearch.goto()
                            }
                        }
                    },
                    (3, "input"): {
                        (0, "grammar"): {
                            "item": [
                                "Fine",
                                "$ excellent",
                                "$ outstanding",
                                "$ fabulous",
                                "$ terrific",
                                "$ not good",
                                "$ not so good",
                                "$ not well",
                                "$ not so well",
                                "$ terrible",
                                "$ awful",
                                "$ worst",
                                "$ bored",
                                "$ sad",
                                "$ good",
                                "$ well",
                                "$ fine",
                                "$ thirsty",
                                "$ hungry",
                                "$ tired"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "I am doing well, thanks."
                            },
                            (1, "goto"): HowCanHelpYouOutput.goto()
                        }
                    },
                    (4, "output"): {
                        (0, "prompt"): {
                            "item": "I am doing well, thanks."
                        },
                        (1, "goto"): Goto(ref="output_2459184")
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Nice to meet you",
                            "$ nice to meet you",
                            "$ pleasure to meet you",
                            "$ make your acquaintance"
                        ]
                    },
                    (1, "if"): {
                        (0, "cond"): Condition(name="Greeting_Count", operator="GREATER_THEN", root_text="2"),
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "You're very polite, but don't you want me to look up movies for you?"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): [
                                    {
                                        (0, "grammar"): GenericGrammar.yes(),
                                        (1, "goto"): Goto(ref="output_ask_for_recency")
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.no(),
                                        (1, "action"): GreetingAction.create_reset(),
                                        (2, "output"): {
                                            "prompt": GenericPrompt.ok_fine()
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): Goto(ref="output_ask_for_recency")
                                    }
                                ],
                                (1, "goto"): PreliminarySequencesSearch.goto()
                            }
                        }
                    },
                    (2, "output"): {
                        (0, "prompt"): {
                            "item": "Nice to meet you too, {User_Name}!",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): HowCanHelpYouOutput.goto()
                    }
                }
            ]
        }
