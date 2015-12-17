from dialog.schema.elements import Goto
from dialog.schema.factories.action import PageAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs import RemoveGenreInput, RemoveRatingInput, RemoveAllSearchCriteriaInput

from dialog.schema.factories.outputs.anything_else_can_help_with import AnythingElseCanHelpWith
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch
from dialog.schema.factories.variables import NAME_RESULTS_COUNT

__author__ = 'robdefeo'


class AfterSearchResults:
    @staticmethod
    def __id():
        return "getUserInput_after_search_results"

    @staticmethod
    def goto():
        return Goto(ref=AfterSearchResults.__id())

    @staticmethod
    def create():
        from dialog.schema.factories.inputs.main_search_criteria import AgainOption, MoreOption, GoBackOption

        return {
            "@id": AfterSearchResults.__id(),
            (0, "input"):
                {
                    "@id": "input_2456878",
                    (0, "grammar"): {
                        "item": [
                            "Okay",
                            "okay",
                            "$ done"
                        ]
                    },
                    (1, "output"): AnythingElseCanHelpWith.create()
                },
            (1, "input"): {
                (0, "grammar"): {
                    "item": [
                        "What do you mean",
                        "$ what do you mean",
                        "$ what does that mean",
                        "$ what did you mean",
                        "$ what were those movies again",
                        "$ what did you mean",
                        "$ what are those"
                    ]
                },
                (1, "output"): {
                    (0, "prompt"): {
                        "item": "These are the {Recency_Preference} movies. Go ahead and click one!",
                        "@selectionType": "RANDOM"
                    },
                    (1, "goto"): AfterSearchResults.goto()
                }
            },
            # TODO could be the details flow?
            (2, "input"): {
                (0, "grammar"): {
                    "item": [
                        "When are those showing?",
                        "$ when * showing",
                        "$ when * playing",
                        "$ when * play",
                        "$ what times * showing",
                        "$ what times * playing",
                        "$ what times * play",
                        "$ what * showtimes",
                        "$ where * showing",
                        "$ where * playing",
                        "$ where * play"
                    ]
                },
                (1, "output"): {
                    "@id": "output_ask_search_for_movies_in_area",
                    (0, "prompt"): {
                        "item": "Oh. You mean movies in your area. I must direct you to Fandango for that. Would you like the link?",
                        "@selectionType": "RANDOM"
                    },
                    (1, "getUserInput"): {
                        (0, "input"): [
                            {
                                (0, "grammar"): GenericGrammar.yes(),
                                (1, "output"): {
                                    (0, "prompt"): GenericPrompt.ok(),
                                    (1, "goto"): Goto(ref="output_showtimes_zipcode")
                                }
                            },
                            {
                                (0, "grammar"): GenericGrammar.no(),
                                (1, "output"): {
                                    (0, "prompt"): GenericPrompt.ok(),
                                    (1, "goto"): AfterSearchResults.goto()
                                }
                            }
                        ],
                        (1, "goto"): AfterSearchResults.goto()
                    }
                }
            },
            (3, "if"): {
                (0, "cond"): {
                    "@varName": "Popularity_Score",
                    "@operator": "HAS_VALUE"
                },
                (1, "input"): [
                    {
                        (0, "grammar"): {
                            "item": [
                                "What are the ratings?",
                                "$ ratings for it",
                                "$ ratings does it get",
                                "$ ratings it gets",
                                "$ ratings it got",
                                "$ ratings it received",
                                "$ its ratings",
                                "$ how many * stars",
                                "why",
                                "why not",
                                "why do you say that"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "{Selected_Movie} gets {Popularity_Score} stars from users.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): {
                                    (0, "grammar"): {
                                        "item": [
                                            "okay",
                                            "okay",
                                            "$ sucks",
                                            "haha"
                                        ]
                                    },
                                    (1, "goto"): AnythingElseCanHelpWith.goto()
                                },
                                (1, "goto"): {
                                    "@ref": "input_2456878"
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "What is it about?",
                                "$ what's is about?"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "There should be a short description of {Selected_Movie} to the right.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): {
                                    (0, "grammar"): {
                                        "item": [
                                            "okay",
                                            "okay",
                                            "$ sucks",
                                            "haha"
                                        ]
                                    },
                                    (1, "goto"): AnythingElseCanHelpWith.goto()
                                },
                                (1, "goto"): {
                                    "@ref": "input_2456878"
                                }
                            }
                        }
                    }
                ],
                (2, "goto"): {
                    "@ref": "input_2459410"
                }
            },
            (4, "input"): {
                "@id": "input_2459410",
                (0, "grammar"): {
                    "item": [
                        "Are those",
                        "$ are those",
                        "$ are these",
                        "$ is that",
                        "$ were those",
                        "$ were these",
                        "$ does this",
                        "$ do these",
                        "$ are they"
                    ]
                },
                (1, "input"): [
                    {
                        (0, "grammar"): {
                            "item": [
                                "What are",
                                "$ what are",
                                "$ what were"
                            ]
                        },
                        (1, "action"): PageAction.set_to_repeat(),
                        (2, "goto"): {
                            "@ref": "output_2456876"
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "all of them",
                                "$ all",
                                "$ it"
                            ]
                        },
                        (1, "goto"): {
                            "@ref": "profileCheck_2459411"
                        }
                    }
                ],
                (2, "if"): {
                    "@id": "profileCheck_2459411",
                    (0, "cond"): {
                        "@varName": "Current_Index",
                        "@operator": "LESS_THEN",
                        "#text": "{%s}" % NAME_RESULTS_COUNT
                    },
                    (1, "output"): {
                        (0, "prompt"): {
                            "item": "No. Say <i>show me more</i> if you want to see more.",
                            "@selectionType": "RANDOM"
                        },
                        (1, "goto"): AfterSearchResults.goto()
                    }
                },
                (3, "output"): {
                    (0, "prompt"): {
                        "item": "Yes. I'm afraid that's all of them.",
                        "@selectionType": "RANDOM"
                    },
                    (1, "goto"): AfterSearchResults.goto()
                }
            },
            (5, "input"): RemoveGenreInput.create(),
            (6, "input"): RemoveRatingInput.create(),
            (7, "input"): RemoveAllSearchCriteriaInput.create(),
            # (8, "input"): Showtimes.create(),
            # (9, "input"): RecencyGenreRatingPreference.create(),
            # (10, "input"): RecencyGenrePreference.create(),
            # (11, "input"): RecencyRatingPreference.create(),
            # (12, "input"): GenreRecencyPreference.create(),
            # (13, "input"): RecencyPreference.create(),
            # (15, "input"): CertificationPreference.create(),
            # (16, "input"): UnsupportedGenre.create(),
            # (17, "input"): DateTimePreference.create(),
            (18, "input"): AgainOption.create(),
            (19, "input"): MoreOption.create(),
            (20, "input"): GoBackOption.create(),
            (21, "goto"): PreliminarySequencesSearch.goto()
        }
