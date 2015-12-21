from dialog.elements import Grammar, Goto, Input, Prompt, GetUserInput, Output
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, StylePreferenceAction, TopicAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.profile_checks.style_preference import StylePreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class PreliminarySequencesFolder:
    @staticmethod
    def _id():
        return "folder_preliminary_sequences"

    @staticmethod
    def create():
        return {
            "@label": "PRELIMINARY SEQUENCES",
            "@id": PreliminarySequencesFolder._id(),
            (0, "action"): [
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero()
            ],
            (1, "input"): {
                (0, "grammar"): Grammar(
                    items=[
                        "Do you know",
                        "$ do you know",
                        "$ can you",
                        "$ do you have information",
                        "$ can I",
                        "$ can you tell",
                        "$ what kind of",
                        "$ what else do you know"
                    ]
                ),
                (1, "action"): [
                    GreetingAction.reset(),
                    SmallTalkAction.set_to_zero()
                ],
                (2, "input"): [
                    Input(
                        children=[
                            Grammar(
                                items=[
                                    "out-of-scope movie topics",
                                    "$ (OTHER_MOVIE)={Topic}"
                                ]
                            ),
                            TopicAction.set_to_value(),
                            Input(
                                children=[
                                    Grammar(
                                        items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    Goto(ref="output_no_topic_lookup")
                                ]
                            ),
                            Output(
                                Prompt(
                                    items=["No."]
                                ),
                                children=[
                                    Output(
                                        _id="output_no_topic_lookup",
                                        prompt=Prompt(
                                            items=[
                                                "I'm afraid I can't look up movies by {Topic}, only by Genre or MPAA Rating."]
                                        ),
                                        children=[
                                            GetUserInput(
                                                children=[
                                                    Input(
                                                        children=[
                                                            GenericGrammar.ok(),
                                                            HowCanHelpYouOutput.goto()
                                                        ]
                                                    ),
                                                    PreliminarySequencesSearch.goto()
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    Input(
                        children=[
                            Grammar(
                                items=[
                                    "by out-of-scope movie topics",
                                    "$ (BY_OTHER_MOVIE)={Topic}"
                                ]
                            ),
                            TopicAction.set_to_value(),
                            Input(
                                children=[
                                    Grammar(
                                        items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    Goto(ref="output_2503370"),

                                ]
                            ),
                            Output(
                                Prompt(
                                    items=["No."]
                                ),
                                children=[
                                    Output(
                                        _id="output_2503370",
                                        prompt=Prompt(
                                            items=[
                                                "I'm afraid I can't look up {Topic}, only Current and Upcoming movies by Genre or MPAA Rating.", ]
                                        ),
                                        children=[
                                            GetUserInput(
                                                children=[
                                                    Input(
                                                        children=[
                                                            Grammar(
                                                                items=["Okay."]
                                                            ),
                                                            HowCanHelpYouOutput.goto()
                                                        ]
                                                    ),
                                                    PreliminarySequencesSearch.goto()
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    {
                        (0, "grammar"): {
                            "item": [
                                "unsupported genres",
                                "$ (UNSUPPORTED_GENRES)={Topic}"
                            ]
                        },
                        (1, "action"): {
                            "@varName": "Topic",
                            "@operator": "SET_TO",
                            "#text": "{Topic.value:main}"
                        },
                        (2, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2510164"
                            }
                        },
                        (3, "output"): {
                            (0, "prompt"): {
                                "item": "No.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "output"): {
                                "@id": "output_2510164",
                                (0, "prompt"): {
                                    "item": "I'm afraid {Topic} isn't a movie genre I know. Please try another one.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): {
                                            "item": "Okay."
                                        },
                                        (1, "goto"): HowCanHelpYouOutput.goto()
                                    },
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "theaters",
                                "$ theaters",
                                "$ fandango"
                            ]
                        },
                        (1, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2503320"
                            }
                        },
                        (2, "output"): {
                            (0, "prompt"): {
                                "item": "No."
                            },
                            (1, "output"): {
                                "@id": "output_2503320",
                                (0, "prompt"): {
                                    "item": "I'm afraid I cannot look up theaters myself, but I can give you a link to Fandango.com where you can buy tickets in your ZIP code. ",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYouOutput.goto()
                                    },
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "reviews",
                                "$ reviews",
                                "$ highest rating",
                                "$ highest rated",
                                "$ best rating",
                                "$ best rated",
                                "$ lowest rating",
                                "$ lowest rated",
                                "$ oscar winners",
                                "$ best movie",
                                "$ best movies"
                            ]
                        },
                        (1, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2469539"
                            }
                        },
                        (2, "output"): {
                            (0, "prompt"): {
                                "item": "No.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "output"): {
                                "@id": "output_2469539",
                                (0, "prompt"): {
                                    "item": "I'm afraid I cannot find movie reviews or search by number of stars at this time.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYouOutput.goto()
                                    },
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": "$ (STYLE)={Style_Preference}"
                        },
                        (1, "action"): StylePreferenceAction.set_to_value(),
                        (2, "goto"): {
                            "@ref": "search_2414740"
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "genres",
                                "$ genres"
                            ]
                        },
                        (1, "output"): {
                            (0, "prompt"): {
                                "item": "Action, adventure, animated, comedy, crime, documentary, drama, family, fantasy, foreign, historical, horror, music, mystery, romance, science fiction, TV movie, thriller, war movies and western.  <br> <br>",
                                "@selectionType": "RANDOM"
                            },
                            (1, "getUserInput"): {
                                (0, "input"): {
                                    (0, "grammar"): GenericGrammar.ok(),
                                    (1, "goto"): HowCanHelpYouOutput.goto()
                                },
                                (1, "goto"): PreliminarySequencesSearch.goto()
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "old movies",
                                "$ old movies",
                                "$ classic movies",
                                "$ oldies",
                                "$ classics"
                            ]
                        },
                        (1, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2503380"
                            }
                        },
                        (2, "output"): {
                            (0, "prompt"): {
                                "item": "No."
                            },
                            (1, "output"): {
                                "@id": "output_2503380",
                                (0, "prompt"): {
                                    "item": "I'm afraid I cannot look up Old Movies, only Current and Upcoming.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYouOutput.goto()
                                    },
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "movies",
                                "$ movies"
                            ]
                        },
                        (1, "action"): {
                            "@varName": "Topic",
                            "@operator": "SET_TO",
                            "#text": "movies"
                        },
                        (2, "input"): Input(
                            children=[
                                Grammar(
                                    items=[
                                        "what",
                                        "$ what"
                                    ]
                                ),
                                Goto(ref="output_what_jemboo_knows")
                            ]
                        ),
                        (3, "output"): Output(
                            prompt=Prompt(
                                items=["Yes."]
                            ),
                            children=[
                                Output(
                                    _id="output_what_jemboo_knows",
                                    prompt=Prompt(
                                        items=[
                                            "I can look up current and upcoming movies by Genre or MPAA Rating and show you trailers for them. But I'm afraid I cannot search by number of stars or by movie titles or actor and director names at this time.", ]
                                    ),
                                    children=[
                                        GetUserInput(
                                            children=[
                                                Input(
                                                    children=[
                                                        GenericGrammar.ok(),
                                                        HowCanHelpYouOutput.goto()
                                                    ]
                                                ),
                                                PreliminarySequencesSearch.goto()
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "trailer",
                                "$ trailer",
                                "$ trailers"
                            ]
                        },
                        (1, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2510290"
                            }
                        },
                        (2, "output"): {
                            (0, "prompt"): {
                                "item": "Yes."
                            },
                            (1, "output"): {
                                "@id": "output_2510290",
                                (0, "prompt"): {
                                    "item": "After searching for movies, you can click on a particular movie result to watch its <i>trailer</i>, or video preview.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYouOutput.goto()
                                    },
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": [
                                "out-of-scope topics",
                                "$ (DINING)={Topic}",
                                "$ (WEATHER)={Topic}",
                                "$ (TRAFFIC)={Topic}"
                            ]
                        },
                        (1, "action"): [
                            {
                                "@varName": "Topic",
                                "@operator": "SET_TO",
                                "#text": "{Topic.value:main}"
                            },
                            {
                                "@varName": "Out-of-Scope_Count",
                                "@operator": "INCREMENT_BY",
                                "#text": "1"
                            }
                        ],
                        (2, "if"): {
                            (0, "cond"): {
                                "@varName": "Out-of-Scope_Count",
                                "@operator": "GREATER_THEN",
                                "#text": "2"
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "I'm sorry I don't know about that. Can I look up some movies for you?"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): [
                                        {
                                            (0, "grammar"): GenericGrammar.yes(),
                                            (1, "goto"): StylePreferenceProfileCheck.goto()
                                        },
                                        {
                                            (0, "grammar"): GenericGrammar.no(),
                                            (1, "action"): {
                                                "@varName": "Out-of-Scope_Count",
                                                "@operator": "SET_TO",
                                                "#text": "0"
                                            },
                                            (2, "output"): {
                                                "prompt": GenericPrompt.ok_fine()
                                            }
                                        },
                                        {
                                            (0, "grammar"): GenericGrammar.ok(),
                                            (1, "goto"): StylePreferenceProfileCheck.goto()
                                        }
                                    ],
                                    (1, "goto"): PreliminarySequencesSearch.goto()
                                }
                            }
                        },
                        (3, "input"): {
                            (0, "grammar"): {
                                "item": [
                                    "what",
                                    "$ what"
                                ]
                            },
                            (1, "goto"): Goto(ref="output_2497989")
                        },
                        (4, "output"): {
                            (0, "prompt"): Prompt(items=["No."]),
                            (1, "output"): {
                                "@id": "output_2497989",
                                (0, "prompt"): Prompt(
                                    items=["I'm afraid I don't know much about {Topic}. Just movies."]),
                                (1, "getUserInput"): GetUserInput(
                                    children=[
                                        Input(
                                            children=[
                                                Grammar(
                                                    items=["Okay."]
                                                ),
                                                HowCanHelpYouOutput.goto()
                                            ]
                                        ),
                                        PreliminarySequencesSearch.goto()
                                    ]
                                )
                            }
                        }
                    }
                ],
                (3, "goto"): Goto(ref="output_what_jemboo_knows")
            }
        }
