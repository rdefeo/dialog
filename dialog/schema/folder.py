from dialog.schema.elements import Action
from dialog.schema.factories.action import GreetingAction, TerminalExchangeAction
from dialog.schema.factories.grammar import FeelingGrammar, ProfileGrammar, GenericGrammar


class LibraryFolder:
    def create(self):
        return {
            "folder": [
                {
                    "output": [
                        {
                            "@id": "output_help_with_anything_else",
                            (0, "prompt"): {
                                "item": "Is there anything else I can help you with?",
                                "@selectionType": "RANDOM"
                            },
                            (1, "action"): [
                                Action(varName="Page", operator="SET_TO", text="New").create(),
                                Action(varName="Current_Index", operator="SET_TO", text="0").create(),
                                Action(varName="Certification_Preference", operator="SET_TO_BLANK").create(),
                                Action(varName="Genre_Preference", operator="SET_TO_BLANK").create(),
                                Action(varName="Recency_Preference", operator="SET_TO_BLANK").create(),
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
                                        (0, "grammar"): GenericGrammar.create_yes(),
                                        (1, "goto"): {
                                            "@ref": "output_how_can_i_help_you"
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.create_no(),
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "Okay.",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_2458386"
                                            }
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
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
                                        (0, "grammar"): GenericGrammar().create_yes(),
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
                                                    TerminalExchangeAction.create_yes(),
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
                                                                    (1, "goto"): {
                                                                        "@ref": "output_how_can_i_help_you"
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_how_can_i_help_you"
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.create_no(),
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
                                                        (0, "grammar"): GenericGrammar.create_no(),
                                                        (1, "action"): TerminalExchangeAction.create_no(),
                                                        (2, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Okay."
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "output_goodbye"
                                                            }
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): GenericGrammar.create_yes(),
                                                        (1, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Okay. What can I do for you?"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "getUserInput_2414745"
                                                            }
                                                        }
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
                            },
                            "@id": "output_2458386"
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
                                        (0, "grammar"): GenericGrammar.create_yes(),
                                        (1, "goto"): {
                                            "@ref": "output_2449874"
                                        }
                                    },
                                    {
                                        (0, "grammar"): GenericGrammar.create_no(),
                                        (1, "action"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "SET_TO",
                                            "#text": "0"
                                        },
                                        (2, "output"): {
                                            "prompt": {
                                                "item": "Okay, fine.",
                                                "@selectionType": "RANDOM"
                                            }
                                        }
                                    },
                                    {
                                        (0, "grammar"): {
                                            "item": "Okay"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_2449874"
                                        }
                                    }
                                ],
                                (1, "goto"): {
                                    "@ref": "search_2414738"
                                }
                            }
                        }
                    ],
                    "@label": "SYSTEM INITIATED SEQUENCES"
                },
                {
                    "@label": "PRELIMINARY SEQUENCES",
                    "@id": "folder_2414695",
                    (0, "action"): [
                        GreetingAction.create_reset(),
                        {
                            "@varName": "Small_Talk_Count",
                            "@operator": "SET_TO",
                            "#text": "0"
                        }
                    ],
                    (1, "input"): {
                        (0, "grammar"): {
                            "item": [
                                "Do you know",
                                "$ do you know",
                                "$ can you",
                                "$ do you have information",
                                "$ can I",
                                "$ can you tell",
                                "$ what kind of",
                                "$ what else do you know"
                            ]
                        },
                        (1, "action"): [
                            GreetingAction.create_reset(),
                            {
                                "@varName": "Small_Talk_Count",
                                "@operator": "SET_TO",
                                "#text": "0"
                            }
                        ],
                        (2, "input"): [
                            {
                                (0, "grammar"): {
                                    "item": [
                                        "out-of-scope movie topics",
                                        "$ (OTHER_MOVIE)={Topic}"
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
                                        "@ref": "output_2449762"
                                    }
                                },
                                (3, "output"): {
                                    (0, "prompt"): {
                                        "item": "No.",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "output"): {
                                        "@id": "output_2449762",
                                        (0, "prompt"): {
                                            "item": "I'm afraid I can't look up movies by {Topic}, only by Genre or MPAA Rating.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": "Okay."
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                }
                            },
                            {
                                (0, "grammar"): {
                                    "item": [
                                        "by out-of-scope movie topics",
                                        "$ (BY_OTHER_MOVIE)={Topic}"
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
                                        "@ref": "output_2503370"
                                    }
                                },
                                (3, "output"): {
                                    (0, "prompt"): {
                                        "item": "No."
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm afraid I can't look up {Topic}, only Current and Upcoming movies by Genre or MPAA Rating.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": "Okay."
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        },
                                        "@id": "output_2503370"
                                    }
                                }
                            },
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
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                }
                            },
                            {
                                (0, "grammar"): {
                                    "item": [
                                        "showtimes",
                                        "$ showtimes"
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
                                        "@ref": "output_2459443"
                                    }
                                },
                                (2, "output"): {
                                    (0, "prompt"): {
                                        "item": "No.",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm afraid I cannot look up showtimes myself, but I can give you a link to Fandango.com where you can buy tickets in your ZIP code. ",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        },
                                        "@id": "output_2459443"
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
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
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
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                }
                            },
                            {
                                (0, "grammar"): {
                                    "item": "$ (GENRE)={Genre_Preference}"
                                },
                                (1, "action"): {
                                    "@varName": "Genre_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Genre_Preference.value:main}"
                                },
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
                                            (0, "grammar"): {
                                                "item": "Okay"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_how_can_i_help_you"
                                            }
                                        },
                                        (1, "goto"): {
                                            "@ref": "search_2414738"
                                        }
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
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
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
                                (2, "input"): {
                                    (0, "grammar"): {
                                        "item": [
                                            "what",
                                            "$ what"
                                        ]
                                    },
                                    (1, "goto"): {
                                        "@ref": "output_2443814"
                                    }
                                },
                                (3, "output"): {
                                    (0, "prompt"): {
                                        "item": "Yes.",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "output"): {
                                        "@id": "output_2443814",
                                        (0, "prompt"): {
                                            "item": "I can look up current and upcoming movies by Genre or MPAA Rating and show you trailers for them. But I'm afraid I cannot search by number of stars or by movie titles or actor and director names at this time.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                }
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
                                                (0, "grammar"): {
                                                    "item": "Okay"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
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
                                                    (0, "grammar"): {
                                                        "item": GenericGrammar.create_yes()
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_2449874"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): GenericGrammar.create_no(),
                                                    (1, "action"): {
                                                        "@varName": "Out-of-Scope_Count",
                                                        "@operator": "SET_TO",
                                                        "#text": "0"
                                                    },
                                                    (2, "output"): {
                                                        "prompt": {
                                                            "item": "Okay, fine."
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": "Okay"
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_2449874"
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
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
                                    (1, "goto"): {
                                        "@ref": "output_2497989"
                                    }
                                },
                                (4, "output"): {
                                    (0, "prompt"): {
                                        "item": "No."
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm afraid I don't know much about {Topic}. Just movies."
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): {
                                                    "item": "Okay."
                                                },
                                                (1, "goto"): {
                                                    "@ref": "output_how_can_i_help_you"
                                                }
                                            },
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        },
                                        "@id": "output_2497989"
                                    }
                                }
                            }
                        ],
                        (3, "goto"): {
                            "@ref": "output_2443814"
                        }
                    }
                },
                {
                    "@id": "folder_routing_seqeuences",
                    "@selectionType": "RANDOM",
                    "@label": "ROUTING SEQUENCES",
                    (0, "action"): [
                        GreetingAction.create_reset(),
                        {
                            "@varName": "Small_Talk_Count",
                            "@operator": "SET_TO",
                            "#text": "0"
                        }
                    ],
                    (1, "input"): [
                        {
                            (0, "grammar"): {
                                "item": [
                                    "out-of-scope movie topics",
                                    "$ (OTHER_MOVIE)={Topic}"
                                ]
                            },
                            (1, "action"): {
                                "@varName": "Topic",
                                "@operator": "SET_TO",
                                "#text": "{Topic.value:main}"
                            },
                            (2, "goto"): {
                                "@ref": "output_2449762"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "by out-of-scope movie topics",
                                    "$ (BY_OTHER_MOVIE)={Topic}"
                                ]
                            },
                            (1, "action"): {
                                "@varName": "Topic",
                                "@operator": "SET_TO",
                                "#text": "{Topic.value:main}"
                            },
                            (2, "goto"): {
                                "@ref": "output_2503370"
                            }
                        },
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
                            (2, "goto"): {
                                "@ref": "output_2510164"
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
                            (1, "goto"): {
                                "@ref": "output_2503380"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Review",
                                    "$ review",
                                    "$ find movies by rating",
                                    "$ look up movies by rating",
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
                            (1, "action"): [
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
                            ],
                            (2, "goto"): {
                                "@ref": "output_2469539"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Movie theaters",
                                    "$ movie theaters"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "output_2503320"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "trailer",
                                    "$ trailer",
                                    "$ trailers"
                                ]
                            },
                            (1, "action"): [
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
                            ],
                            (2, "goto"): {
                                "@ref": "output_2510290"
                            }
                        }
                    ]
                },
                {
                    (0, "action"): [
                        GreetingAction.create_reset(),
                        {
                            "@varName": "Small_Talk_Count",
                            "@operator": "SET_TO",
                            "#text": "0"
                        }
                    ],
                    (1, "input"): [
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Favorites",
                                    "$ favorites",
                                    "$ favorite movies",
                                    "$ favorited",
                                    "$ hearted"
                                ]
                            },
                            (1, "action"): [
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
                            ],
                            (2, "output"): {
                                (0, "prompt"): {
                                    "item": "When you get the details for a movie, you can save the movie in your <i>Favorites</i> by clicking on the heart icon above the trailer.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): {
                                            "item": "Okay."
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_how_can_i_help_you"
                                        }
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_2414738"
                                    }
                                }
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Details",
                                    "$ details",
                                    "$ detail",
                                    "$ movie info",
                                    "$ movie information"
                                ]
                            },
                            (1, "action"): [
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
                            ],
                            (2, "output"): {
                                (0, "prompt"): {
                                    "item": "After searching for movies, you can click on a particular movie result to see <i>details</i>, such as rating, summary and trailer.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): {
                                            "item": "Okay."
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_how_can_i_help_you"
                                        }
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_2414738"
                                    }
                                }
                            }
                        },
                        {
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
                                {
                                    "@varName": "Genre_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Genre_Preference.value:main}"
                                },
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
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
                                        (2, "goto"): {
                                            "@ref": "profileCheck_2503330"
                                        }
                                    }
                                }
                            ],
                            (3, "if"): {
                                "@id": "profileCheck_2503330",
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
                                                            (2, "goto"): {
                                                                "@ref": "output_how_can_i_help_you"
                                                            }
                                                        },
                                                        {
                                                            (0, "grammar"): GenericGrammar.create_no(),
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "Okay."
                                                                },
                                                                (1, "goto"): {
                                                                    "@ref": "output_2458386"
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
                                        "@ref": "search_2414738"
                                    }
                                }
                            }
                        },
                        {
                            "@id": "input_2443892",
                            (0, "grammar"): {
                                "item": [
                                    "Movies",
                                    "$ (GENRE)={Genre_Preference}",
                                    "$ (CERTIFICATION)={Certification_Preference}",
                                    "$ (RECENCY)={Recency_Preference}",
                                    "$ movies"
                                ]
                            },
                            (1, "action"): [
                                GreetingAction.create_reset(),
                                {
                                    "@varName": "Small_Talk_Count",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                },
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
                                    "@varName": "Genre_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Genre_Preference.value:main}"
                                },
                                {
                                    "@varName": "Topic",
                                    "@operator": "SET_TO",
                                    "#text": "movies"
                                },
                                {
                                    "@varName": "Certification_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Certification_Preference.value:main}"
                                },
                                {
                                    "@varName": "Recency_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Recency_Preference.value:main}"
                                }
                            ],
                            (2, "input"): [
                                {
                                    "@id": "input_2503411",
                                    (0, "grammar"): {
                                        "item": "$ (DATE_TIME_RANGE)={DateTime_Mentioned_ENT}"
                                    },
                                    (1, "action"): {
                                        "@varName": "DateTime_Current",
                                        "@operator": "SET_TO",
                                        "#text": "<mct:getTime>America/Tijuana</mct:getTime>"
                                    },
                                    (2, "input"): {
                                        (0, "grammar"): {
                                            "item": "$ next"
                                        },
                                        (1, "goto"): {
                                            "action": {
                                                "@varName": "Recency_Preference",
                                                "@operator": "SET_TO",
                                                "#text": "Upcoming"
                                            },
                                            "@ref": "profileCheck_2503417"
                                        }
                                    },
                                    (3, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Recency_Preference",
                                            "@operator": "EQUALS",
                                            "#text": "Upcoming"
                                        },
                                        (1, "goto"): {
                                            "@ref": "input_2443775"
                                        },
                                        "@id": "profileCheck_2503417"
                                    },
                                    (4, "output"): {
                                        (0, "prompt"): {
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "function"): {
                                            (0, "script"): {
                                                "@name": "CalculateTimeDiff",
                                                "#text": "Name=CalculateTimeDiff\n\nStartTime={DateTime_Current}\nEndTime={DateTime_Mentioned_ENT.value:FROM_FULL}"
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): "",
                                                (1, "action"): {
                                                    "@varName": "DateTime_Difference",
                                                    "@operator": "SET_TO",
                                                    "#text": "{MCT:CUSTOM:CalculateTimeDiff:days}"
                                                },
                                                (2, "if"): {
                                                    (0, "cond"): {
                                                        "@varName": "DateTime_Difference",
                                                        "@operator": "LESS_THEN",
                                                        "#text": "1"
                                                    },
                                                    (1, "goto"): {
                                                        "action": {
                                                            "@varName": "Recency_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "Current"
                                                        },
                                                        "@ref": "input_2443775"
                                                    }
                                                },
                                                (3, "goto"): {
                                                    "action": {
                                                        "@varName": "Recency_Preference",
                                                        "@operator": "SET_TO",
                                                        "#text": "Upcoming"
                                                    },
                                                    "@ref": "input_2443775"
                                                }
                                            }
                                        },
                                        (2, "goto"): {
                                            "@ref": "input_2443775"
                                        }
                                    }
                                },
                                {
                                    "@id": "input_2443775",
                                    (0, "grammar"): {
                                        "item": [
                                            "rated",
                                            "$(CERTIFICATION)={Certification_Preference}"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "Certification_Preference",
                                        "@operator": "SET_TO",
                                        "#text": "{Certification_Preference.value:main}"
                                    },
                                    (2, "goto"): {
                                        "@ref": "input_2503399"
                                    }
                                },
                                {
                                    "@id": "input_2503399",
                                    (0, "grammar"): {
                                        "item": [
                                            "family-friendly",
                                            "$ family",
                                            "$ childrens",
                                            "$ child",
                                            "$ kid"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "Certification_Preference",
                                        "@operator": "SET_TO",
                                        "#text": "G"
                                    },
                                    (2, "goto"): {
                                        "@ref": "input_2443841"
                                    }
                                },
                                {
                                    "@id": "input_2443841",
                                    (0, "grammar"): {
                                        "item": [
                                            "how recent",
                                            "$ (RECENCY)={Recency_Preference}"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "Recency_Preference",
                                        "@operator": "SET_TO",
                                        "#text": "{Recency_Preference.value:main}"
                                    },
                                    (2, "goto"): {
                                        "@ref": "input_2459178"
                                    }
                                },
                                {
                                    "@id": "input_2459178",
                                    (0, "grammar"): {
                                        "item": [
                                            "near me",
                                            "$ (ZIPCODE)={ZIP_Code_Preference}",
                                            "$ near me"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "ZIP_Code_Preference",
                                        "@operator": "SET_TO",
                                        "#text": "{ZIP_Code_Preference.value:main}"
                                    },
                                    (2, "goto"): {
                                        "@ref": "profileCheck_2503330"
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "out-of-scope movie topics",
                                            "$ (OTHER_MOVIE)={Topic}"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "Topic",
                                        "@operator": "SET_TO",
                                        "#text": "{Topic.value:main}"
                                    },
                                    (2, "goto"): {
                                        "@ref": "output_2449762"
                                    }
                                }
                            ],
                            (3, "if"): [
                                {
                                    (0, "cond"): {
                                        "@varName": "Recency_Preference",
                                        "@operator": "IS_BLANK"
                                    },
                                    (1, "output"): {
                                        "@id": "output_2449874",
                                        (0, "prompt"): {
                                            "item": "Current movies or upcoming movies?",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            "@id": "getUserInput_2449875",
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Recency and genre",
                                                            "$ (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference}"
                                                        ]
                                                    },
                                                    (1, "action"): [
                                                        {
                                                            "@varName": "Current_Index",
                                                            "@operator": "SET_TO",
                                                            "#text": "0"
                                                        },
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Genre_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Recency_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Recency_Preference.value:main}"
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "profileCheck_2449894"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Recency and rating",
                                                            "$ (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference}",
                                                            "$ (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference}"
                                                        ]
                                                    },
                                                    (1, "action"): [
                                                        {
                                                            "@varName": "Recency_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Recency_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Current_Index",
                                                            "@operator": "SET_TO",
                                                            "#text": "0"
                                                        },
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Certification_Preference.value:main}"
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "profileCheck_2449894"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "how recent",
                                                            "$ (RECENCY)={Recency_Preference}"
                                                        ]
                                                    },
                                                    (1, "action"): [
                                                        {
                                                            "@varName": "Recency_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Recency_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Current_Index",
                                                            "@operator": "SET_TO",
                                                            "#text": "0"
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "profileCheck_2449894"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "why does it matter",
                                                            "$ why * matter",
                                                            "$ why * want",
                                                            "$ who cares",
                                                            "$ both",
                                                            "$ no preference",
                                                            "$ doesn't matter"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Sorry, I need to look up current and upcoming movies separately.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2449875"
                                                        }
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    },
                                    "@id": "profileCheck_2449907"
                                },
                                {
                                    "@id": "profileCheck_2449894",
                                    (0, "cond"): {
                                        "@varName": "Genre_Preference",
                                        "@operator": "IS_BLANK"
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "Are you in the mood for a specific genre?",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "if"): {
                                            (0, "cond"): {
                                                "@varName": "First_Time",
                                                "@operator": "EQUAL_TO_YES"
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": "<mct:link><b><mct:input>Comedy</mct:input></b>. Make me laugh!<br></mct:link>\n<mct:link><b><mct:input>Romance</mct:input></b>, baby!<br></mct:link>\n<mct:link><b><mct:input>Horror</mct:input></b>, I'm in the mood to be scared.<br></mct:link>\n<mct:link><b><mct:input>Children's</mct:input></b>, let's keep it friendly.<br></mct:link>\n<mct:link><b><mct:input>Action</mct:input></b>! I love a good chase scene.<br></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "action"): {
                                                    "@varName": "First_Time",
                                                    "@operator": "SET_TO_NO"
                                                },
                                                (2, "goto"): {
                                                    "@ref": "getUserInput_pick_genre"
                                                }
                                            }
                                        },
                                        (2, "getUserInput"): {
                                            "@id": "getUserInput_pick_genre",
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Unsupported genres",
                                                            "$ (UNSUPPORTED_GENRES)={Topic}"
                                                        ]
                                                    },
                                                    (1, "action"): {
                                                        "@varName": "Topic",
                                                        "@operator": "SET_TO",
                                                        "#text": "{Topic.value:main}"
                                                    },
                                                    (2, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Sorry, {Topic} isn't a genre that I know. Please try another one.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_pick_genre"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What",
                                                            "$ what",
                                                            "$ which",
                                                            "$ tell me"
                                                        ]
                                                    },
                                                    (1, "input"): [
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "they",
                                                                    "$ they",
                                                                    "$ ones",
                                                                    "$ genres",
                                                                    "$ genre",
                                                                    "$ genre's",
                                                                    "$ choices",
                                                                    "$ options",
                                                                    "$ you have",
                                                                    "$ you know",
                                                                    "$ what else"
                                                                ]
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "Action, adventure, animated, comedy, crime, documentary, drama, family, fantasy, foreign, historical, horror, music, mystery, romance, science fiction, TV movie, thriller, war movies and western.  <br> <br>",
                                                                    "@selectionType": "RANDOM"
                                                                },
                                                                (1, "goto"): {
                                                                    "@ref": "getUserInput_pick_genre"
                                                                }
                                                            }
                                                        },
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "suggest",
                                                                    "$ you suggest",
                                                                    "$ you recommend",
                                                                    "$ your favorite",
                                                                    "$ your favorites"
                                                                ]
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "Well, Science Fiction is my favorite genre.",
                                                                    "@selectionType": "RANDOM"
                                                                },
                                                                (1, "goto"): {
                                                                    "@ref": "getUserInput_pick_genre"
                                                                }
                                                            }
                                                        }
                                                    ]
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Genre and rating",
                                                            "$ (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference}",
                                                            "$ (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference}"
                                                        ]
                                                    },
                                                    (1, "action"): [
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Certification_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Genre_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Search_Now",
                                                            "@operator": "SET_TO_NO"
                                                        }
                                                    ],
                                                    (2, "if"): {
                                                        (0, "cond"): {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "EQUALS",
                                                            "#text": "Family"
                                                        },
                                                        (1, "goto"): {
                                                            "action": {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "G"
                                                            },
                                                            "@ref": "profileCheck_2449895"
                                                        }
                                                    },
                                                    (3, "goto"): {
                                                        "@ref": "profileCheck_2449895"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Genre",
                                                            "$ (GENRE)={Genre_Preference}"
                                                        ]
                                                    },
                                                    (1, "action"): [
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Genre_Preference.value:main}"
                                                        },
                                                        {
                                                            "@varName": "Search_Now",
                                                            "@operator": "SET_TO_NO"
                                                        }
                                                    ],
                                                    (2, "if"): {
                                                        (0, "cond"): {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "EQUALS",
                                                            "#text": "Family"
                                                        },
                                                        (1, "goto"): {
                                                            "action": {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "G"
                                                            },
                                                            "@ref": "profileCheck_2449895"
                                                        }
                                                    },
                                                    (3, "goto"): {
                                                        "@ref": "profileCheck_2449895"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "No",
                                                            "$ no",
                                                            "$ no preference",
                                                            "$ don't care",
                                                            "$ don't know",
                                                            "$ none",
                                                            "$ all",
                                                            "$ anything",
                                                            "$ any",
                                                            "$ whatever",
                                                            "$ nothing specific",
                                                            "$ don't have a preference"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "profileCheck_2449895"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": "Yes"
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Which one?"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_pick_genre"
                                                        }
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                },
                                {
                                    "@id": "profileCheck_2449895",
                                    (0, "cond"): {
                                        "@varName": "Certification_Preference",
                                        "@operator": "IS_BLANK"
                                    },
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
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Certification_Preference.value:main}"
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "output_2456875"
                                                    }
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
                                                    (0, "grammar"): GenericGrammar.create_yes(),
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
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                }
                            ],
                            (4, "output"): {
                                (0, "prompt"): {
                                    "item": "Okay. <br><br>",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "output"): {
                                    "@id": "output_2456876",
                                    (0, "prompt"): {
                                        "item": "\"{\"Search_Now\":\"{Search_Now}\", \"Recency\":\"{Recency_Preference}\", \"Rating\":\"{Certification_Preference}\", \"Genre\":\"{Genre_Preference}\", \"Index\":\"{Current_Index}\", \"Page\":\"{Page}\"}\"",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "action"): [
                                        {
                                            "@varName": "Last_Results",
                                            "@operator": "SET_TO_NO"
                                        },
                                        {
                                            "@varName": "First_Results",
                                            "@operator": "SET_TO_NO"
                                        },
                                        {
                                            "@varName": "Search_Now",
                                            "@operator": "SET_TO_YES"
                                        },
                                        {
                                            "@varName": "First_Time",
                                            "@operator": "SET_TO_NO"
                                        },
                                        {
                                            "@varName": "Previous Certification Selected",
                                            "@operator": "SET_TO",
                                            "#text": "{Certification_Preference}"
                                        },
                                        {
                                            "@varName": "Previous Genre Selected",
                                            "@operator": "SET_TO",
                                            "#text": "{Genre_Preference}"
                                        },
                                        {
                                            "@varName": "Previous Recency Selected",
                                            "@operator": "SET_TO",
                                            "#text": "{Recency_Preference}"
                                        }
                                    ],
                                    (2, "getUserInput"): {
                                        (0, "input"): {
                                            (0, "grammar"): {
                                                "item": "UPDATE NUM_MOVIES"
                                            },
                                            (1, "if"): [
                                                {
                                                    (0, "cond"): {
                                                        "@varName": "Num_Movies",
                                                        "@operator": "EQUALS",
                                                        "#text": "0"
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "I'm afraid I found {Num_Movies} {Recency_Preference} movies matching {Certification_Preference} {Genre_Preference}. Try changing your criteria.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "getUserInput"): {
                                                            (0, "input"): {
                                                                (0, "grammar"): {
                                                                    "item": "Okay"
                                                                },
                                                                (1, "action"): [
                                                                    {
                                                                        "@varName": "Certification_Preference",
                                                                        "@operator": "SET_TO_BLANK"
                                                                    },
                                                                    {
                                                                        "@varName": "Genre_Preference",
                                                                        "@operator": "SET_TO_BLANK"
                                                                    },
                                                                    {
                                                                        "@varName": "Recency_Preference",
                                                                        "@operator": "SET_TO_BLANK"
                                                                    }
                                                                ],
                                                                (2, "goto"): {
                                                                    "@ref": "profileCheck_2449907"
                                                                }
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "input_2460509"
                                                            }
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "cond"): [
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "IS_BLANK"
                                                        },
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "HAS_VALUE"
                                                        }
                                                    ],
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Good choice, {User_Name}! I found {Num_Movies} results for {Recency_Preference} {Certification_Preference}-rated movies.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2456877"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "cond"): [
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "IS_BLANK"
                                                        },
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "HAS_VALUE"
                                                        }
                                                    ],
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Good choice, {User_Name}! I found {Num_Movies} results for {Recency_Preference} {Genre_Preference} movies.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2456877"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "cond"): [
                                                        {
                                                            "@varName": "Certification_Preference",
                                                            "@operator": "IS_BLANK"
                                                        },
                                                        {
                                                            "@varName": "Genre_Preference",
                                                            "@operator": "IS_BLANK"
                                                        }
                                                    ],
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "I found {Num_Movies} results for ALL {Recency_Preference} movies.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2456877"
                                                        }
                                                    }
                                                }
                                            ],
                                            (2, "output"): {
                                                (0, "prompt"): {
                                                    "item": "Good choices, {User_Name}! I found {Num_Movies} results for {Recency_Preference} {Certification_Preference}-rated {Genre_Preference} movies.",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "getUserInput"): {
                                                    "@id": "getUserInput_2456877",
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
                                                            (1, "output"): {
                                                                "@id": "output_2460098",
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
                                                                                    "item": "Okay.",
                                                                                    "@selectionType": "RANDOM"
                                                                                },
                                                                                (1, "goto"): {
                                                                                    "@ref": "getUserInput_2456877"
                                                                                }
                                                                            }
                                                                        },
                                                                        {
                                                                            (0, "grammar"): GenericGrammar.create_yes(),
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
                                                                                },
                                                                                {
                                                                                    "@varName": "Certification_Preference",
                                                                                    "@operator": "SET_TO_BLANK"
                                                                                },
                                                                                {
                                                                                    "@varName": "Genre_Preference",
                                                                                    "@operator": "SET_TO_BLANK"
                                                                                },
                                                                                {
                                                                                    "@varName": "Recency_Preference",
                                                                                    "@operator": "SET_TO_BLANK"
                                                                                }
                                                                            ],
                                                                            (2, "goto"): {
                                                                                "@ref": "output_how_can_i_help_you"
                                                                            }
                                                                        },
                                                                        {
                                                                            (0, "grammar"): GenericGrammar.create_no(),
                                                                            (1, "output"): {
                                                                                (0, "prompt"): {
                                                                                    "item": "Okay."
                                                                                },
                                                                                (1, "goto"): {
                                                                                    "@ref": "output_2458386"
                                                                                }
                                                                            }
                                                                        }
                                                                    ],
                                                                    (1, "goto"): {
                                                                        "@ref": "input_2456878"
                                                                    }
                                                                }
                                                            }
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
                                                            (1, "goto"): {
                                                                "@ref": "getUserInput_2456877"
                                                            }
                                                        }
                                                    },
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
                                                            "@id": "output_2459418",
                                                            (0, "prompt"): {
                                                                "item": "Oh. You mean movies in your area. I must direct you to Fandango for that. Would you like the link?",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "getUserInput"): {
                                                                (0, "input"): [
                                                                    {
                                                                        (0, "grammar"): GenericGrammar.create_yes(),
                                                                        (1, "output"): {
                                                                            (0, "prompt"): {
                                                                                "item": "Okay.",
                                                                                "@selectionType": "RANDOM"
                                                                            },
                                                                            (1, "goto"): {
                                                                                "@ref": "output_2503331"
                                                                            }
                                                                        }
                                                                    },
                                                                    {
                                                                        (0, "grammar"): {
                                                                            "item": [
                                                                                "No",
                                                                                "$ no"
                                                                            ]
                                                                        },
                                                                        (1, "output"): {
                                                                            (0, "prompt"): {
                                                                                "item": "Okay.",
                                                                                "@selectionType": "RANDOM"
                                                                            },
                                                                            (1, "goto"): {
                                                                                "@ref": "getUserInput_2456877"
                                                                            }
                                                                        }
                                                                    }
                                                                ],
                                                                (1, "goto"): {
                                                                    "@ref": "getUserInput_2456877"
                                                                }
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
                                                                            (1, "goto"): {
                                                                                "@ref": "output_2460098"
                                                                            }
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
                                                                            (1, "goto"): {
                                                                                "@ref": "output_2460098"
                                                                            }
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
                                                                (1, "action"): {
                                                                    "@varName": "Page",
                                                                    "@operator": "SET_TO",
                                                                    "#text": "repeat"
                                                                },
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
                                                                "#text": "{Num_Movies}"
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "No. Say <i>show me more</i> if you want to see more.",
                                                                    "@selectionType": "RANDOM"
                                                                },
                                                                (1, "goto"): {
                                                                    "@ref": "getUserInput_2456877"
                                                                }
                                                            }
                                                        },
                                                        (3, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Yes. I'm afraid that's all of them.",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "getUserInput_2456877"
                                                            }
                                                        }
                                                    },
                                                    (5, "input"): {
                                                        "@id": "input_2460509",
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Remove genre",
                                                                "$ remove (GENRE)={Genre_Preference}",
                                                                "$ cancel (GENRE)={Genre_Preference}",
                                                                "$ remove genre",
                                                                "$ cancel genre",
                                                                "$ any genre",
                                                                "$ all genre"
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
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (6, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Remove rating",
                                                                "$ remove (CERTIFICATION)={Certification_Preference}",
                                                                "$ cancel (CERTIFICATION)={Certification_Preference}",
                                                                "$ remove rating",
                                                                "$ cancel rating",
                                                                "$ all ratings",
                                                                "$ all rating",
                                                                "$ any ratings",
                                                                "$ any rating"
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
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (7, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "all movies",
                                                                "$ all movies",
                                                                "$ all results"
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
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            },
                                                            {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (8, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Showtimes",
                                                                "$ showtimes",
                                                                "$ times",
                                                                "$ time",
                                                                "$ showing"
                                                            ]
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_2459418"
                                                        }
                                                    },
                                                    (9, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Recency, Genre and Rating",
                                                                "$ (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference}",
                                                                "$ (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference} ",
                                                                "$ (GENRE)={Genre_Preference} (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference}",
                                                                "$ (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference} ",
                                                                "$ (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference} (RECENCY)={Recency_Preference}",
                                                                "$ (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference}"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Recency_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Recency_Preference.value:main}"
                                                            },
                                                            {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Genre_Preference.value:main}"
                                                            },
                                                            {
                                                                "@varName": "Page",
                                                                "@operator": "SET_TO",
                                                                "#text": "new"
                                                            },
                                                            {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (10, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Recency and Genre",
                                                                "$ (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference}",
                                                                "$ (GENRE)={Genre_Preference} (RECENCY)={Recency_Preference}"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Current_Index",
                                                                "@operator": "SET_TO",
                                                                "#text": "0"
                                                            },
                                                            {
                                                                "@varName": "Recency_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Recency_Preference.value:main}"
                                                            },
                                                            {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Genre_Preference.value:main}"
                                                            },
                                                            {
                                                                "@varName": "Page",
                                                                "@operator": "SET_TO",
                                                                "#text": "new"
                                                            }
                                                        ],
                                                        (2, "if"): {
                                                            (0, "cond"): {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "EQUALS",
                                                                "#text": "Family"
                                                            },
                                                            (1, "goto"): {
                                                                "action": {
                                                                    "@varName": "Certification_Preference",
                                                                    "@operator": "SET_TO",
                                                                    "#text": "G"
                                                                },
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (3, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (11, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Recency and Rating",
                                                                "$ (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference}",
                                                                "$ (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference}"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
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
                                                                "@varName": "Recency_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Recency_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (12, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Genre and Rating",
                                                                "$ (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference}",
                                                                "$ (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference}"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Current_Index",
                                                                "@operator": "SET_TO",
                                                                "#text": "0"
                                                            },
                                                            {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Genre_Preference.value:main}"
                                                            },
                                                            {
                                                                "@varName": "Page",
                                                                "@operator": "SET_TO",
                                                                "#text": "new"
                                                            },
                                                            {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (13, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Recency",
                                                                "$ (RECENCY)={Recency_Preference}"
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
                                                                "@varName": "Recency_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Recency_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "input"): {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "all",
                                                                    "$ all",
                                                                    "$ just",
                                                                    "$ any"
                                                                ]
                                                            },
                                                            (1, "action"): [
                                                                {
                                                                    "@varName": "Certification_Preference",
                                                                    "@operator": "SET_TO_BLANK"
                                                                },
                                                                {
                                                                    "@varName": "Genre_Preference",
                                                                    "@operator": "SET_TO_BLANK"
                                                                }
                                                            ],
                                                            (2, "goto"): {
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (3, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (14, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Genre",
                                                                "$ (GENRE)={Genre_Preference}",
                                                                "$ genre"
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
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Genre_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "input"): {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "all",
                                                                    "$ all",
                                                                    "$ just"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (3, "if"): {
                                                            (0, "cond"): {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "EQUALS",
                                                                "#text": "Family"
                                                            },
                                                            (1, "goto"): {
                                                                "action": {
                                                                    "@varName": "Certification_Preference",
                                                                    "@operator": "SET_TO",
                                                                    "#text": "G"
                                                                },
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (4, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (15, "input"): {
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
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            }
                                                        ],
                                                        (2, "input"): {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "all",
                                                                    "$ all",
                                                                    "$ any"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Genre_Preference",
                                                                "@operator": "SET_TO_BLANK"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (3, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (16, "input"): {
                                                        (0, "grammar"): {
                                                            "item": "$ (UNSUPPORTED_GENRES)={Topic}"
                                                        },
                                                        (1, "action"): {
                                                            "@varName": "Topic",
                                                            "@operator": "SET_TO",
                                                            "#text": "{Topic.value:main}"
                                                        },
                                                        (2, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "I'm afraid {Topic} isn't a movie genre I know. Please try another one.",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "getUserInput_2456877"
                                                            }
                                                        }
                                                    },
                                                    (17, "input"): {
                                                        (0, "grammar"): {
                                                            "item": "$ (DATE_TIME_RANGE)={DateTime_Mentioned_ENT}"
                                                        },
                                                        (1, "action"): {
                                                            "@varName": "DateTime_Current",
                                                            "@operator": "SET_TO",
                                                            "#text": "<mct:getTime>America/Tijuana</mct:getTime>"
                                                        },
                                                        (2, "input"): {
                                                            (0, "grammar"): {
                                                                "item": "$ next"
                                                            },
                                                            (1, "goto"): {
                                                                "action": {
                                                                    "@varName": "Recency_Preference",
                                                                    "@operator": "SET_TO",
                                                                    "#text": "Upcoming"
                                                                },
                                                                "@ref": "profileCheck_2510175"
                                                            }
                                                        },
                                                        (3, "if"): {
                                                            "@id": "profileCheck_2510175",
                                                            (0, "cond"): {
                                                                "@varName": "Recency_Preference",
                                                                "@operator": "EQUALS",
                                                                "#text": "Upcoming"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "output_2456875"
                                                            }
                                                        },
                                                        (4, "output"): {
                                                            (0, "prompt"): "",
                                                            (1, "function"): {
                                                                (0, "script"): {
                                                                    "@name": "CalculateTimeDiff",
                                                                    "#text": "Name=CalculateTimeDiff\n\nStartTime={DateTime_Current}\nEndTime={DateTime_Mentioned_ENT.value:FROM_FULL}"
                                                                },
                                                                (1, "output"): {
                                                                    (0, "prompt"): "",
                                                                    (1, "action"): {
                                                                        "@varName": "DateTime_Difference",
                                                                        "@operator": "SET_TO",
                                                                        "#text": "{MCT:CUSTOM:CalculateTimeDiff:days}"
                                                                    },
                                                                    (2, "if"): {
                                                                        (0, "cond"): {
                                                                            "@varName": "DateTime_Difference",
                                                                            "@operator": "LESS_THEN",
                                                                            "#text": "1"
                                                                        },
                                                                        (1, "goto"): {
                                                                            "action": {
                                                                                "@varName": "Recency_Preference",
                                                                                "@operator": "SET_TO",
                                                                                "#text": "Current"
                                                                            },
                                                                            "@ref": "output_2456875"
                                                                        }
                                                                    },
                                                                    (3, "goto"): {
                                                                        "action": {
                                                                            "@varName": "Recency_Preference",
                                                                            "@operator": "SET_TO",
                                                                            "#text": "Upcoming"
                                                                        },
                                                                        "@ref": "output_2456875"
                                                                    }
                                                                }
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2456875"
                                                            }
                                                        }
                                                    },
                                                    (18, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "again",
                                                                "$ again",
                                                                "$ one more time"
                                                            ]
                                                        },
                                                        (1, "action"): {
                                                            "@varName": "Page",
                                                            "@operator": "SET_TO",
                                                            "#text": "repeat"
                                                        },
                                                        (2, "goto"): {
                                                            "@ref": "output_2456875"
                                                        }
                                                    },
                                                    (19, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "more",
                                                                "$ more",
                                                                "$ next",
                                                                "$ forward"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Show_Next",
                                                                "@operator": "SET_TO_YES"
                                                            },
                                                            {
                                                                "@varName": "Page",
                                                                "@operator": "SET_TO",
                                                                "#text": "next"
                                                            }
                                                        ],
                                                        (2, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Okay."
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "\"{Search_Now:\"{Search_Now}\", Recency:\"{Recency_Preference}\", Rating:\"{Certification_Preference}\", Genre:\"{Genre_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\", Total_Movies:\"{Num_Movies}\", Total_Pages:\"{Total_Pages}\"}\""
                                                                },
                                                                (1, "action"): {
                                                                    "@varName": "First_Results",
                                                                    "@operator": "SET_TO_NO"
                                                                },
                                                                (2, "getUserInput"): {
                                                                    "@id": "getUserInput_2503174",
                                                                    "input": {
                                                                        (0, "grammar"): {
                                                                            "item": "UPDATE CURRENT_INDEX"
                                                                        },
                                                                        (1, "action"): [
                                                                            {
                                                                                "@varName": "Show_Next",
                                                                                "@operator": "SET_TO_NO"
                                                                            },
                                                                            {
                                                                                "@varName": "Show_Previous",
                                                                                "@operator": "SET_TO_NO"
                                                                            }
                                                                        ],
                                                                        (2, "if"): [
                                                                            {
                                                                                (0, "cond"): {
                                                                                    "@varName": "Last_Results",
                                                                                    "@operator": "EQUAL_TO_YES"
                                                                                },
                                                                                (1, "output"): {
                                                                                    (0, "prompt"): {
                                                                                        "item": "Those were the last results"
                                                                                    },
                                                                                    (1, "goto"): {
                                                                                        "@ref": "profileCheck_2503183"
                                                                                    }
                                                                                }
                                                                            },
                                                                            {
                                                                                (0, "cond"): {
                                                                                    "@varName": "Current_Index",
                                                                                    "@operator": "EQUALS",
                                                                                    "#text": "{Num_Movies}"
                                                                                },
                                                                                (1, "output"): {
                                                                                    (0, "prompt"): {
                                                                                        "item": "Here are the last results"
                                                                                    },
                                                                                    (1, "action"): {
                                                                                        "@varName": "Last_Results",
                                                                                        "@operator": "SET_TO_YES"
                                                                                    },
                                                                                    (2, "goto"): {
                                                                                        "@ref": "profileCheck_2503183"
                                                                                    }
                                                                                }
                                                                            }
                                                                        ],
                                                                        (3, "output"): {
                                                                            (0, "prompt"): {
                                                                                "item": "Here is the next set of results"
                                                                            },
                                                                            (1, "if"): [
                                                                                {
                                                                                    "@id": "profileCheck_2503183",
                                                                                    (0, "cond"): [
                                                                                        {
                                                                                            "@varName": "Genre_Preference",
                                                                                            "@operator": "IS_BLANK"
                                                                                        },
                                                                                        {
                                                                                            "@varName": "Certification_Preference",
                                                                                            "@operator": "HAS_VALUE"
                                                                                        }
                                                                                    ],
                                                                                    (1, "output"): {
                                                                                        (0, "prompt"): {
                                                                                            "item": "for {Recency_Preference} {Certification_Preference}-rated movies."
                                                                                        },
                                                                                        (1, "goto"): {
                                                                                            "@ref": "getUserInput_2456877"
                                                                                        }
                                                                                    }
                                                                                },
                                                                                {
                                                                                    (0, "cond"): [
                                                                                        {
                                                                                            "@varName": "Certification_Preference",
                                                                                            "@operator": "IS_BLANK"
                                                                                        },
                                                                                        {
                                                                                            "@varName": "Genre_Preference",
                                                                                            "@operator": "HAS_VALUE"
                                                                                        }
                                                                                    ],
                                                                                    (1, "output"): {
                                                                                        (0, "prompt"): {
                                                                                            "item": "for {Recency_Preference} {Genre_Preference} movies."
                                                                                        },
                                                                                        (1, "goto"): {
                                                                                            "@ref": "getUserInput_2456877"
                                                                                        }
                                                                                    }
                                                                                },
                                                                                {
                                                                                    (0, "cond"): [
                                                                                        {
                                                                                            "@varName": "Certification_Preference",
                                                                                            "@operator": "IS_BLANK"
                                                                                        },
                                                                                        {
                                                                                            "@varName": "Genre_Preference",
                                                                                            "@operator": "IS_BLANK"
                                                                                        }
                                                                                    ],
                                                                                    (1, "output"): {
                                                                                        (0, "prompt"): {
                                                                                            "item": "for ALL {Recency_Preference} movies."
                                                                                        },
                                                                                        (1, "goto"): {
                                                                                            "@ref": "getUserInput_2456877"
                                                                                        }
                                                                                    }
                                                                                }
                                                                            ],
                                                                            (2, "output"): {
                                                                                (0, "prompt"): {
                                                                                    "item": "for {Recency_Preference} {Certification_Preference}-rated {Genre_Preference} movies."
                                                                                },
                                                                                (1, "goto"): {
                                                                                    "@ref": "getUserInput_2456877"
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    },
                                                    (20, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Go back",
                                                                "$ back",
                                                                "$ previous",
                                                                "$ prior"
                                                            ]
                                                        },
                                                        (1, "action"): [
                                                            {
                                                                "@varName": "Page",
                                                                "@operator": "SET_TO",
                                                                "#text": "previous"
                                                            },
                                                            {
                                                                "@varName": "Show_Previous",
                                                                "@operator": "SET_TO_YES"
                                                            }
                                                        ],
                                                        (2, "if"): {
                                                            (0, "cond"): {
                                                                "@varName": "Current_Index",
                                                                "@operator": "EQUALS",
                                                                "#text": "10"
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "Those were the first results",
                                                                    "@selectionType": "RANDOM"
                                                                },
                                                                (1, "goto"): {
                                                                    "@ref": "profileCheck_2503183"
                                                                }
                                                            }
                                                        },
                                                        (3, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Okay.",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "output"): {
                                                                (0, "prompt"): {
                                                                    "item": "\"{Search_Now:\"{Search_Now}\", Recency:\"{Recency_Preference}\", Rating:\"{Certification_Preference}\", Genre:\"{Genre_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\"}\"",
                                                                    "@selectionType": "RANDOM"
                                                                },
                                                                (1, "action"): {
                                                                    "@varName": "Last_Results",
                                                                    "@operator": "SET_TO_NO"
                                                                },
                                                                (2, "getUserInput"): {
                                                                    (0, "input"): {
                                                                        (0, "grammar"): {
                                                                            "item": "UPDATE CURRENT_INDEX"
                                                                        },
                                                                        (1, "action"): [
                                                                            {
                                                                                "@varName": "Show_Next",
                                                                                "@operator": "SET_TO_NO"
                                                                            },
                                                                            {
                                                                                "@varName": "Show_Previous",
                                                                                "@operator": "SET_TO_NO"
                                                                            }
                                                                        ],
                                                                        (2, "if"): [
                                                                            {
                                                                                (0, "cond"): {
                                                                                    "@varName": "First_Results",
                                                                                    "@operator": "EQUAL_TO_YES"
                                                                                },
                                                                                (1, "output"): {
                                                                                    (0, "prompt"): {
                                                                                        "item": "Those were the first results",
                                                                                        "@selectionType": "RANDOM"
                                                                                    },
                                                                                    (1, "goto"): {
                                                                                        "@ref": "getUserInput_2503174"
                                                                                    }
                                                                                }
                                                                            },
                                                                            {
                                                                                (0, "cond"): {
                                                                                    "@varName": "Current_Index",
                                                                                    "@operator": "EQUALS",
                                                                                    "#text": "10"
                                                                                },
                                                                                (1, "output"): {
                                                                                    (0, "prompt"): {
                                                                                        "item": "Here are the first results",
                                                                                        "@selectionType": "RANDOM"
                                                                                    },
                                                                                    (1, "action"): {
                                                                                        "@varName": "First_Results",
                                                                                        "@operator": "SET_TO_YES"
                                                                                    },
                                                                                    (2, "goto"): {
                                                                                        "@ref": "getUserInput_2456877"
                                                                                    }
                                                                                }
                                                                            }
                                                                        ],
                                                                        (3, "output"): {
                                                                            (0, "prompt"): {
                                                                                "item": "Here is the previous set of results",
                                                                                "@selectionType": "RANDOM"
                                                                            },
                                                                            (1, "goto"): {
                                                                                "@ref": "getUserInput_2456877"
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    },
                                                    (21, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "@id": "output_2456875"
                            }
                        }
                    ],
                    "@label": "BASE SEQUENCES",
                    "@id": "folder_2414701"
                },
                {
                    "@selectionType": "RANDOM",
                    "@label": "GLOBAL SEQUENCES",
                    "@id": "folder_2442951",
                    (0, "folder"): [
                        {
                            "@label": "UI ACTIONS",
                            (0, "input"): {
                                (0, "grammar"): {
                                    "item": "USER CLICKS BOX"
                                },
                                (1, "output"): {
                                    (0, "prompt"): {
                                        "item": "{Selected_Movie}."
                                    },
                                    (1, "if"): [
                                        {
                                            (0, "cond"): {
                                                "@varName": "Popularity_Score",
                                                "@operator": "GREATER_THEN",
                                                "#text": "6.9"
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": [
                                                        "Great choice! That gets fabulous ratings.",
                                                        "That's a good one! You will love it.",
                                                        " I hear that's a really good movie!"
                                                    ],
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "getUserInput_2456877"
                                                }
                                            }
                                        },
                                        {
                                            (0, "cond"): {
                                                "@varName": "Popularity_Score",
                                                "@operator": "LESS_THEN",
                                                "#text": "4"
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": [
                                                        "Hmm, I hear that's not such a great movie.",
                                                        "Um, that one gets low ratings.",
                                                        "Are you sure about that? The ratings are terrible."
                                                    ],
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "getUserInput_2456877"
                                                }
                                            }
                                        }
                                    ],
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": [
                                                "Okay.",
                                                "All right.",
                                                "Sure thing!",
                                                "Coming right up!"
                                            ],
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "getUserInput_2456877"
                                        }
                                    }
                                }
                            }
                        },
                        {
                            "@selectionType": "RANDOM",
                            "@label": "OPENING SEQUENCES",
                            (0, "input"): [
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Hello",
                                            "Hello again",
                                            "hi there"
                                        ]
                                    },
                                    (1, "action"): GreetingAction.create_increment(),
                                    (2, "if"): [
                                        {
                                            (0, "cond"): {
                                                "@varName": "Terminal_Exchange",
                                                "@operator": "EQUAL_TO_YES"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_welcome_back"
                                            }
                                        },
                                        {
                                            (0, "cond"): [
                                                {
                                                    "@varName": "Greeting_Count",
                                                    "@operator": "GREATER_THEN",
                                                    "#text": "2"
                                                },
                                                {
                                                    "@varName": "Greeting_Count",
                                                    "@operator": "GREATER_THEN",
                                                    "#text": "2"
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "output_end_of_small_talk"
                                            }
                                        }
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
                                                        (1, "goto"): {
                                                            "@ref": "input_2443892"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): FeelingGrammar.create_not_so_good(),
                                                        (1, "goto"): {
                                                            "@ref": "output_sorry_to_hear_that"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "Not so bad",
                                                                "$ not * bad"
                                                            ]
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_good_to_hear"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): FeelingGrammar.create_feeling_fine(),
                                                        (1, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Good to hear! <br> <br>",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "output_how_can_i_help_you"
                                                            },
                                                            "@id": "output_good_to_hear"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): FeelingGrammar.create_feeling_great(),
                                                        (1, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Fantastic! So glad to hear it. <br> <br>",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "output_how_can_i_help_you"
                                                            }
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): FeelingGrammar.create_feeling_bad(),
                                                        (1, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "I'm sorry to hear that. <br> <br>",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "output_how_can_i_help_you"
                                                            },
                                                            "@id": "output_sorry_to_hear_that"
                                                        }
                                                    }
                                                ],
                                                (1, "goto"): {
                                                    "@ref": "search_2414738"
                                                }
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
                                            {
                                                "@varName": "Greeting_Count",
                                                "@operator": "GREATER_THEN",
                                                "#text": "2"
                                            },
                                            {
                                                "@varName": "Greeting_Count",
                                                "@operator": "GREATER_THEN",
                                                "#text": "2"
                                            }
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
                                                        (0, "grammar"): GenericGrammar.create_yes(),
                                                        (1, "goto"): {
                                                            "@ref": "output_2449874"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): GenericGrammar.create_no(),
                                                        (1, "action"): GreetingAction.create_reset(),
                                                        (2, "output"): {
                                                            "prompt": {
                                                                "item": "Okay, fine.",
                                                                "@selectionType": "RANDOM"
                                                            }
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): {
                                                            "item": "Okay"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_2449874"
                                                        }
                                                    }
                                                ],
                                                (1, "goto"): {
                                                    "@ref": "search_2414738"
                                                }
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
                                            (1, "goto"): {
                                                "@ref": "output_how_can_i_help_you"
                                            }
                                        }
                                    },
                                    (4, "output"): {
                                        (0, "prompt"): {
                                            "item": "I am doing well, thanks."
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_2459184"
                                        }
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
                                        (0, "cond"): {
                                            "@varName": "Greeting_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "You're very polite, but don't you want me to look up movies for you?"
                                            },
                                            (1, "getUserInput"): {
                                                (0, "input"): [
                                                    {
                                                        (0, "grammar"): GenericGrammar.create_yes(),
                                                        (1, "goto"): {
                                                            "@ref": "output_2449874"
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): GenericGrammar.create_no(),
                                                        (1, "action"): GreetingAction.create_reset(),
                                                        (2, "output"): {
                                                            "prompt": {
                                                                "item": "Okay, fine."
                                                            }
                                                        }
                                                    },
                                                    {
                                                        (0, "grammar"): {
                                                            "item": "Okay"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_2449874"
                                                        }
                                                    }
                                                ],
                                                (1, "goto"): {
                                                    "@ref": "search_2414738"
                                                }
                                            }
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "Nice to meet you too, {User_Name}!",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_how_can_i_help_you"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "input": [
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "I should be going",
                                            "$ should be going",
                                            "$ should go",
                                            "$ need to go",
                                            "$ got to go",
                                            "$ gotta run",
                                            "$ gotta go",
                                            "$ need to run",
                                            "$ need to leave",
                                            "$ have to leave",
                                            "$ have to go",
                                            "$ gtg"
                                        ]
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "Okay.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_2458386"
                                        },
                                        "@id": "output_2449675"
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Thanks for your help",
                                            "$ thank you for your help",
                                            "$ thanks for your help"
                                        ]
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "You are welcome.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_2458386"
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": "Goodbye"
                                    },
                                    (1, "if"): [
                                        {
                                            (0, "cond"): {
                                                "@varName": "Terminal_Exchange",
                                                "@operator": "EQUAL_TO_YES"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_end_of_conversation"
                                            }
                                        },
                                        {
                                            (0, "cond"): {
                                                "@varName": "Terminal_Exchange",
                                                "@operator": "EQUAL_TO_NO"
                                            },
                                            (1, "goto"): {
                                                "@ref": "output_2449675"
                                            }
                                        }
                                    ]
                                }
                            ],
                            "@label": "CLOSING SEQUENCES"
                        },
                        {
                            (0, "input"): [
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Help",
                                            "$ help",
                                            "$ how does this work",
                                            "$ what do I do",
                                            "$ what can I do",
                                            "$ don't know",
                                            "$ I'm not sure"
                                        ]
                                    },
                                    (1, "output"): {
                                        "prompt": {
                                            "item": "Say <i>Never mind</i> or <i>nvm</i> to start over.\nSay <i>okay</i> or <i>thanks</i> if my response is acceptable.\nSay <i>What does X mean?</i> for a definition of X.\nSay <i>got to go</i> or <i>bye</i> when you're finished.",
                                            "@selectionType": "RANDOM"
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Say that again",
                                            "$ say that again",
                                            "$ say again",
                                            "$ what did you say",
                                            "$ come again",
                                            "$ say what"
                                        ]
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I said...",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "##special_DNR_GUI_PREVIOUS_OUTPUT_NODE_ID"
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Never mind",
                                            "$ Nevermind",
                                            "$ Never mind",
                                            "$ nvm",
                                            "$ start over",
                                            "$ start again",
                                            "$ restart",
                                            "$ redo",
                                            "$ do over",
                                            "$ start from * beginning",
                                            "$ clear * selections"
                                        ]
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "Okay. Whatever you say, {User_Name}!",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_help_with_anything_else"
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "what does * mean",
                                            "$ what does * mean",
                                            "$ what does * stand for",
                                            "$ do you mean by ",
                                            "$ what are examples of",
                                            "$ what is an example of"
                                        ]
                                    },
                                    (1, "input"): [
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "trailers",
                                                    "$ trailer",
                                                    "$ trailers"
                                                ]
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": "<i>Trailers</i> are video previews for movies. <br> <br>",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "getUserInput"): {
                                                    "input": {
                                                        (0, "grammar"): {
                                                            "item": "okay"
                                                        },
                                                        (1, "output"): {
                                                            (0, "prompt"): {
                                                                "item": "Sure, happy to help. <br> <br>",
                                                                "@selectionType": "RANDOM"
                                                            },
                                                            (1, "goto"): {
                                                                "@ref": "##special_DNR_GET_USER_INPUT_NODE_ID"
                                                            }
                                                        }
                                                    }
                                                },
                                                "@isInsertDNRStatement": "true"
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "genre",
                                                    "$ genre",
                                                    "$ genres"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "The <i>genre</i> is the category of movie, like Drama, Comedy, Action, etc. <br> <br>",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "rating",
                                                    "$ rating",
                                                    "$ ratings",
                                                    "$ mpaa"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "The <i>rating</i> is a recommendation by the Motion Picture Association of America about the suitability of a movie's content for particular age groups. For example, G is for general audiences, while R is restricted to people 17 and older.<br> <br>",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "G",
                                                    "$ G"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "G stands for <i>General Audience</i> and is appropriate for everyone.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "PG-13",
                                                    "$ PG-13"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "PG-13 means <i>Parents Strongly Cautioned</i> or that some material may not be suitable for children under 13 years old.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "PG",
                                                    "$ PG"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "PG stands for <i>Parental Guidance</i>, which means that some material may not be suitable for children.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "NR",
                                                    "$ NR"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "NR stands for <i>Not Rated</i> and means that the film has not yet been rated by the MPAA.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "R",
                                                    "$ R"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "R stands for <i>Restricted</i> and means that children under 17 must be accompanied by parent or adult guardian.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "Current",
                                                    "$ current"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "<i>Current</i> movies are those that have been playing for the past 28 days.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "Upcoming",
                                                    "$ upcoming"
                                                ]
                                            },
                                            (1, "output"): {
                                                "prompt": {
                                                    "item": "<i>Upcoming</i> movies are those that will come out within the next 6 months.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "$ (GENRE)={Topic}",
                                                    "$ (UNSUPPORTED_GENRES)={Topic}"
                                                ]
                                            },
                                            (1, "action"): {
                                                "@varName": "Topic",
                                                "@operator": "SET_TO",
                                                "#text": "{Topic.value:main}"
                                            },
                                            (2, "output"): {
                                                "prompt": {
                                                    "item": "I'm afraid I don't have definitions of the different genres.",
                                                    "@selectionType": "RANDOM"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "I already told you!",
                                            "$ already told you",
                                            "$ already said it"
                                        ]
                                    },
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm sorry, please repeat it for me.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "getUserInput_2414745"
                                        }
                                    }
                                }
                            ],
                            "@label": "REPAIR SEQUENCES"
                        },
                        {
                            "@selectionType": "RANDOM",
                            "@label": "SMALL TALK SEQUENCES",
                            (0, "action"): {
                                "@varName": "Small_Talk_Count",
                                "@operator": "INCREMENT_BY",
                                "#text": "1"
                            },
                            (1, "input"): [
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "What is your name?",
                                            "$ your name",
                                            "$ you called",
                                            "$ they call you",
                                            "$ what can I call you"
                                        ]
                                    },
                                    (1, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "My name is Watson.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "if"): {
                                            (0, "cond"): {
                                                "@varName": "User_Name",
                                                "@operator": "IS_BLANK"
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": "What's your name?",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "goto"): {
                                                    "@ref": "getUserInput_2508591"
                                                }
                                            }
                                        },
                                        (2, "getUserInput"): {
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Okay",
                                                            "okay",
                                                            "hi",
                                                            "hi Watson"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_what_is_name"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "My name is",
                                                            "$ my name",
                                                            "$ call me",
                                                            "$ I'm called",
                                                            "$ I am called",
                                                            "$ known as"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "input_user_knownas_name"
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Siri",
                                            "$ (VIRTUAL_AGENTS)={Topic}"
                                        ]
                                    },
                                    (1, "action"): {
                                        "@varName": "Topic",
                                        "@operator": "SET_TO",
                                        "#text": "{Topic.value:main}"
                                    },
                                    (2, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (3, "input"): {
                                        (0, "grammar"): {
                                            "item": [
                                                "is better",
                                                "$ better",
                                                "$ smarter"
                                            ]
                                        },
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "Now you're hurting my feelings.",
                                                "@selectionType": "RANDOM"
                                            },
                                            (1, "getUserInput"): {
                                                (0, "input"): {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Okay.",
                                                            "$ sorry"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_help_with_anything_else"
                                                    }
                                                },
                                                (1, "goto"): {
                                                    "@ref": "search_2414738"
                                                }
                                            }
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "Do you speak English",
                                            "$ speak English",
                                            "$ understand English",
                                            "$ know English",
                                            "$ get English"
                                        ]
                                    },
                                    (1, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm sorry, English is my second language. My native tongue is Binary. 01110011 01101111 01110010 01110010 01111001",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "haha",
                                                            "okay"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_help_with_anything_else"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "01101110 01110000",
                                                            "01101110 01101111 00100000 01110000 01110010 01101111 01100010 01101100 01100101 01101101",
                                                            "01101110 01110000",
                                                            "01100100 01101111 01101110 00100111 01110100 00100000 01110111 01101111 01110010 01110010 01111001"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "haha, you're good!",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_help_with_anything_else"
                                                        }
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            }
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "What is your favorite",
                                            "$ your favorite",
                                            "$ favorite",
                                            "$ you like",
                                            "$ you prefer"
                                        ]
                                    },
                                    (1, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "input"): [
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "genre",
                                                    "$ genre",
                                                    "$ kind of movie"
                                                ]
                                            },
                                            (1, "output"): {
                                                (0, "prompt"): {
                                                    "item": "Well, Science Fiction is probably my favorite genre!",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "getUserInput"): {
                                                    (0, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "haha",
                                                                "okay"
                                                            ]
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_how_can_i_help_you"
                                                        }
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            (0, "grammar"): {
                                                "item": [
                                                    "movie",
                                                    "$ movie"
                                                ]
                                            },
                                            (1, "action"): {
                                                "@varName": "Topic",
                                                "@operator": "SET_TO",
                                                "#text": "movie"
                                            },
                                            (2, "output"): {
                                                (0, "prompt"): {
                                                    "item": "Oh... 2001: A Space Odyssey... Terminator... The Matrix... I guess I like movies with a strong AI lead.",
                                                    "@selectionType": "RANDOM"
                                                },
                                                (1, "getUserInput"): {
                                                    (0, "input"): {
                                                        (0, "grammar"): {
                                                            "item": [
                                                                "haha",
                                                                "okay"
                                                            ]
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "output_how_can_i_help_you"
                                                        }
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "What is 2001: A Space Odyssey about?",
                                            "$ what is 2001 about"
                                        ]
                                    },
                                    (1, "if"): {
                                        "cond": {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "It's about an intelligent computer, named HAL, who tries to kill the crew of a spaceship.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Okay",
                                                            "haha"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_help_with_anything_else"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Intelligent computer?",
                                                            "$ intelligent computer",
                                                            "$ named HAL",
                                                            "$ kill the crew",
                                                            "$ deactivate him",
                                                            "$ kill them first"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Yes, that's right.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457908"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What do you mean",
                                                            "$ why",
                                                            "$ what do you mean"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "The human crew plans to deactivate him so HAL tries to kill them first.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457908"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What does HAL stand for?",
                                                            "$ HAL stand for",
                                                            "$ HAL mean"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "\"H-A-L\" is derived from Heuristic ALgorithm according to the author, Arthur C. Clarke. But there is also an urban legend that it is a code name for IBM. Shift each letter back once and see what you get!",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457908"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Does he succeed?",
                                                            "$ succeed",
                                                            "$ kill them",
                                                            "$ only tries"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Well, I don't want to spoil the surprise!",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457908"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "No, I mean",
                                                            "$ no i mean",
                                                            "$ no i meant",
                                                            "$ no",
                                                            "$ i mean",
                                                            "$ i meant",
                                                            "$ what about",
                                                            "$ how about"
                                                        ]
                                                    },
                                                    (1, "input"): [
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "The Terminator",
                                                                    "$ terminator"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457979"
                                                            }
                                                        },
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "The Matrix",
                                                                    "$ matrix"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457995"
                                                            }
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            },
                                            "@id": "getUserInput_2457908"
                                        },
                                        "@id": "output_2457907"
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "What is the Terminator about?",
                                            "$ what is the Terminator about",
                                            "$ what is Terminator about"
                                        ]
                                    },
                                    (1, "if"): {
                                        (0, "cond"): {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "It's about a robot who travels back in time to kill the inventor of intelligent machines.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Okay",
                                                            "haha"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_help_with_anything_else"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "On earth?",
                                                            "$ on earth",
                                                            "$ a robot",
                                                            "$ killer robot",
                                                            "$ the inventor",
                                                            "$ intelligent machines",
                                                            "$ the 1980s",
                                                            "$ back in time"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Yes, that's right.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457980"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What do you mean",
                                                            "$ why",
                                                            "$ what do you mean"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "In the future, machines take over the world so the humans send a killer robot back to the 1980s to try to kill the guy who invented the intelligent machines.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457980"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Who is the Terminator",
                                                            "$ who is the terminator",
                                                            "$ who's the terminator",
                                                            "$ what is the terminator"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "The \"terminator\" is the killer robot from the future.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457980"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Does he succeed?",
                                                            "$ succeed",
                                                            "$ kill him",
                                                            "$ only tries"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Well, I don't want to spoil the surprise!"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457980"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "No, I mean",
                                                            "$ no i mean",
                                                            "$ no i meant",
                                                            "$ no",
                                                            "$ i mean",
                                                            "$ i meant",
                                                            "$ what about",
                                                            "$ how about"
                                                        ]
                                                    },
                                                    (1, "input"): [
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "2001",
                                                                    "$ 2001"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457907"
                                                            }
                                                        },
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "The Matrix",
                                                                    "$ matrix"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457995"
                                                            }
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            },
                                            "@id": "getUserInput_2457980"
                                        },
                                        "@id": "output_2457979"
                                    }
                                },
                                {
                                    (0, "grammar"): {
                                        "item": [
                                            "What is the Matrix about?",
                                            "$ what is the matrix about",
                                            "$ what is matrix about",
                                            "$ what is the matrix"
                                        ]
                                    },
                                    (1, "if"): {
                                        "cond": {
                                            "@varName": "Small_Talk_Count",
                                            "@operator": "GREATER_THEN",
                                            "#text": "2"
                                        },
                                        "goto": {
                                            "@ref": "output_too_much_small_talk"
                                        }
                                    },
                                    (2, "output"): {
                                        (0, "prompt"): {
                                            "item": "It's about a guy, named Neo, who has special powers for fighting intelligent programs in a computer simulation.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): [
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Okay",
                                                            "haha"
                                                        ]
                                                    },
                                                    (1, "goto"): {
                                                        "@ref": "output_help_with_anything_else"
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "On earth?",
                                                            "$ on earth",
                                                            "$ in the future",
                                                            "$ named Neo",
                                                            "$ intelligent programs",
                                                            "$ computer simulation"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Yes, that's right.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457996"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What do you mean",
                                                            "$ why",
                                                            "$ what do you mean"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "In the future, machines take over the world and trick humans into believing that a simulation, The Matrix, is reality. But one human has special abilities for defeating the machines.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457996"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "What is the Matrix",
                                                            "$ what is the matrix"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "\"The Matrix\" is the name for the realistic computer simulation of earth.",
                                                            "@selectionType": "RANDOM"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457996"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "Does he succeed?",
                                                            "$ succeed",
                                                            "$ kill him",
                                                            "$ only tries"
                                                        ]
                                                    },
                                                    (1, "output"): {
                                                        (0, "prompt"): {
                                                            "item": "Well, I don't want to spoil the surprise!"
                                                        },
                                                        (1, "goto"): {
                                                            "@ref": "getUserInput_2457996"
                                                        }
                                                    }
                                                },
                                                {
                                                    (0, "grammar"): {
                                                        "item": [
                                                            "No, I mean",
                                                            "$ no i mean",
                                                            "$ no i meant",
                                                            "$ no",
                                                            "$ i mean",
                                                            "$ i meant",
                                                            "$ what about",
                                                            "$ how about"
                                                        ]
                                                    },
                                                    (1, "input"): [
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "2001",
                                                                    "$ 2001"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457907"
                                                            }
                                                        },
                                                        {
                                                            (0, "grammar"): {
                                                                "item": [
                                                                    "Terminator",
                                                                    "$ terminator"
                                                                ]
                                                            },
                                                            (1, "action"): {
                                                                "@varName": "Certification_Preference",
                                                                "@operator": "SET_TO",
                                                                "#text": "{Certification_Preference.value:main}"
                                                            },
                                                            (2, "goto"): {
                                                                "@ref": "output_2457979"
                                                            }
                                                        }
                                                    ],
                                                    (2, "goto"): {
                                                        "@ref": "search_2414738"
                                                    }
                                                }
                                            ],
                                            (1, "goto"): {
                                                "@ref": "search_2414738"
                                            },
                                            "@id": "getUserInput_2457996"
                                        },
                                        "@id": "output_2457995"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "@label": "Storage"
                }
            ],
            "@label": "Library"
        }


class MainFolder:
    def create(self):
        return {
            "@label": "Main",
            (0, "output"): {
                "@id": "output_what_is_name",
                (0, "prompt"): {
                    "item": [
                        "What can I call you?",
                        "What's your name?"
                    ],
                    "@selectionType": "SEQUENTIAL"
                },
                (1, "getUserInput"): {
                    "@id": "getUserInput_2508591",
                    "input": [
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Movies",
                                    "$ (GENRE)={Genre_Preference}",
                                    "$ (CERTIFICATION)={Certification_Preference}",
                                    "$ (RECENCY)={Recency_Preference}",
                                    "$ movies",
                                    "$ want to see something",
                                    "$ planning to go see",
                                    "$ planning to go to the",
                                    "$ going out to see",
                                    "$ planning to see",
                                    "$ want to go see",
                                    "$ thinking of seeing",
                                    "$ thinking we want to see",
                                    "$ what do you recommend",
                                    "$ can you recommend something",
                                    "$ what are your recommendations"
                                ]
                            },
                            (1, "action"): [
                                {
                                    "@varName": "Genre_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Genre_Preference.value:main}"
                                },
                                {
                                    "@varName": "Certification_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Certification_Preference.value:main}"
                                },
                                {
                                    "@varName": "Recency_Preference",
                                    "@operator": "SET_TO",
                                    "#text": "{Recency_Preference.value:main}"
                                },
                                {
                                    "@varName": "Topic",
                                    "@operator": "SET_TO",
                                    "#text": "movies"
                                }
                            ],
                            (2, "goto"): {
                                "@ref": "search_2414738"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Movie-related",
                                    "$ (OTHER_MOVIE)={Topic}",
                                    "$ (BY_OTHER_MOVIE)={Topic}",
                                    "$ showtimes",
                                    "$ theaters",
                                    "$ fandango",
                                    "$ reviews",
                                    "$ review",
                                    "$ critiques",
                                    "$ critique",
                                    "$ old movies",
                                    "$ classic movies",
                                    "$ oldies",
                                    "$ classics",
                                    "$ trailers",
                                    "$ reviews",
                                    "$ (DINING)={Topic}",
                                    "$ (WEATHER)={Topic}",
                                    "$ (TRAFFIC)={Topic}"
                                ]
                            },
                            (1, "goto"): {
                                "@ref": "search_2414738"
                            }
                        },
                        {
                            (0, "grammar"): FeelingGrammar.create_preliminaries(),
                            (1, "goto"): {
                                "@ref": "search_2414738"
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Why do you need to know?",
                                    "$ why",
                                    "$ need to know",
                                    "$ use it",
                                    "$ do with it"
                                ]
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "Just trying to be friendly.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): {
                                    "@ref": "output_start_search"
                                }
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "I don't want to give it!",
                                    "$ don't want",
                                    "$ no",
                                    "$ refuse",
                                    "$ none of your business"
                                ]
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "That's fine.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): {
                                    "@ref": "output_start_search"
                                }
                            }
                        },
                        {
                            "@id": "input_user_knownas_name",
                            (0, "grammar"): ProfileGrammar.create_my_name_is_dynamic_data(),
                            (1, "action"): {
                                "@varName": "User_Name",
                                "@operator": "SET_TO",
                                "#text": "{User_Name.source}"
                            },
                            (2, "output"): {
                                (0, "prompt"): {
                                    "item": "Hi {User_Name}!",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): {
                                    "@ref": "output_start_search"
                                }
                            }
                        }
                    ]
                },
                (2, "output"): [
                    {
                        "@id": "output_start_search",
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
                                    (2, "goto"): {
                                        "@ref": "input_2503411"
                                    }
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
                                        (0, "prompt"): {
                                            "item": "Okay.",
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): {
                                            "@ref": "output_how_can_i_help_you"
                                        }
                                    }
                                },
                                {
                                    (0, "grammar"): GenericGrammar.create_yes_okay(),
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
                                "@ref": "search_2414738"
                            }
                        }
                    },
                    {
                        "@id": "output_how_can_i_help_you",
                        (0, "prompt"): {
                            "item": [
                                "How can I help you?",
                                "What can I do for you?"
                            ],
                            "@selectionType": "RANDOM"
                        },
                        (1, "getUserInput"): {
                            "@id": "getUserInput_2414745",
                            (0, "search"): [
                                {
                                    "@id": "search_2414738",
                                    "@ref": "folder_2414695"
                                },
                                {
                                    "@ref": "folder_routing_seqeuences"
                                },
                                {
                                    "@id": "search_2414740",
                                    "@ref": "folder_2414701"
                                }
                            ],
                            (1, "default"): {
                                (0, "output"): {
                                    "@isInsertDNRStatement": "true",
                                    (0, "prompt"): {
                                        "item": "I'm not sure what you mean. I can understand things like <i>Show me recent PG13-rated Action movies.</i>",
                                        "@selectionType": "RANDOM"
                                    },
                                    (1, "goto"): {
                                        "@ref": "##special_DNR_GET_USER_INPUT_NODE_ID"
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        }


class GlobalFolder:
    def create(self):
        return {
            "@label": "Global",
            "search": {
                "@ref": "folder_2442951"
            }

        }


class ConceptFolder:
    def create(self):
        return {
            (0, "folder"): [
                {
                    "@label": "Genre",
                    "concept": [
                        {
                            "grammar": {
                                "item": [
                                    "arthouse film",
                                    "arthouse films",
                                    "arthouse movie",
                                    "arthouse movies",
                                    "art-house film",
                                    "art-house films",
                                    "art-house movie",
                                    "art-house movies",
                                    "art house film",
                                    "art house films",
                                    "art house movie",
                                    "art house movies",
                                    "art house",
                                    "arthouse",
                                    "art-house"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "children film",
                                    "children films",
                                    "children movie",
                                    "children movies",
                                    "children flick",
                                    "children flicks",
                                    "childrens flick",
                                    "childrens flicks",
                                    "childrens film",
                                    "childrens films",
                                    "childrens movie",
                                    "childrens movies",
                                    "children's film",
                                    "children's films",
                                    "children's movie",
                                    "children's movies",
                                    "children's flick",
                                    "children's flicks",
                                    "kid film",
                                    "kid films",
                                    "kid movie",
                                    "kid flick",
                                    "kid flicks",
                                    "kid movies",
                                    "kids film",
                                    "kids films",
                                    "kids movie",
                                    "kids movies",
                                    "kids flick",
                                    "kids flicks",
                                    "kid's film",
                                    "kid's films",
                                    "kid's movie",
                                    "kid's movies",
                                    "kid's flick",
                                    "kid's flicks"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "drama film",
                                    "drama films",
                                    "drama movie",
                                    "drama movies",
                                    "drama",
                                    "dramas",
                                    "drama flick",
                                    "drama flicks"
                                ]
                            },
                            "@id": "concept_1852694"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "historical film",
                                    "historical films",
                                    "historical movie",
                                    "historical movies",
                                    "period drama",
                                    "period dramas",
                                    "period film",
                                    "period films",
                                    "period movie",
                                    "period movies",
                                    "historical drama",
                                    "historical dramas"
                                ]
                            },
                            "@id": "concept_1852810"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "horror film",
                                    "horror films",
                                    "horror movie",
                                    "horror movies",
                                    "scary movie",
                                    "scary movies",
                                    "scary film",
                                    "scary films",
                                    "slasher film",
                                    "slasher films",
                                    "slasher movie",
                                    "slasher movies",
                                    "slasher flick",
                                    "slasher flicks"
                                ]
                            },
                            "@id": "concept_horror"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "romantic comedy film",
                                    "romantic comedy movie",
                                    "romantic comedies film",
                                    "romantic comedy flick",
                                    "romantic comedy flicks",
                                    "romantic comedy",
                                    "romantic comedies",
                                    "rom com",
                                    "rom coms",
                                    "rom-com",
                                    "rom-coms",
                                    "rom com movie",
                                    "rom com movies",
                                    "rom com film",
                                    "rom com films",
                                    "rom-com movie",
                                    "rom-com movies",
                                    "rom-com film",
                                    "rom-com films",
                                    "rom com flick",
                                    "rom com flicks",
                                    "rom-com flick",
                                    "rom-com flicks"
                                ]
                            },
                            "@id": "concept_romantic"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "sad film",
                                    "sad films",
                                    "sad movie",
                                    "sad movies",
                                    "sad flick",
                                    "sad flicks",
                                    "tear-jerker film",
                                    "tear-jerker films",
                                    "tear-jerker movie",
                                    "tear-jerker movies",
                                    "tear-jerker flick",
                                    "tear-jerker flicks",
                                    "tear-jerkers",
                                    "tear-jerker",
                                    "tear jerker film",
                                    "tear jerker films",
                                    "tear jerker movie",
                                    "tear jerker movies",
                                    "tear jerker flick",
                                    "tear jerker flicks",
                                    "tear jerkers",
                                    "tear jerker"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "sci-fi film",
                                    "sci-fi films",
                                    "sci-fi movie",
                                    "sci-fi movies",
                                    "sci fi film",
                                    "sci fi films",
                                    "sci fi movie",
                                    "sci fi movies",
                                    "scifi film",
                                    "scifi films",
                                    "scifi movie",
                                    "scifi movies",
                                    "sciencefiction film",
                                    "sciencefiction films",
                                    "sciencefiction movie",
                                    "sciencefiction movies",
                                    "science-fiction film",
                                    "science-fiction films",
                                    "science-fiction movie",
                                    "science-fiction movies",
                                    "science fiction film",
                                    "science fiction films",
                                    "science fiction movie",
                                    "science fiction movies"
                                ]
                            },
                            "@id": "concept_scifi"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "war film",
                                    "war films",
                                    "war movie",
                                    "war movies"
                                ]
                            },
                            "@id": "concept_1852807"
                        },
                        {
                            "grammar": {
                                "item": [
                                    "x rated film",
                                    "x rated films",
                                    "x rated movie",
                                    "x rated movies",
                                    "x rated flick",
                                    "x rated flicks",
                                    "x-rated film",
                                    "x-rated films",
                                    "x-rated movie",
                                    "x-rated movies",
                                    "x-rated flick",
                                    "x-rated flicks",
                                    "pornographic film",
                                    "pornographic films",
                                    "pornographic movie",
                                    "pornographic movies",
                                    "pornographic flick",
                                    "pornographic flicks",
                                    "pornography film",
                                    "pornography films",
                                    "pornography movie",
                                    "pornography movies",
                                    "pornography flick",
                                    "pornography flicks",
                                    "porn film",
                                    "porn films",
                                    "porn movie",
                                    "porn movies",
                                    "porn flick",
                                    "porn flicks",
                                    "XXX film",
                                    "XXX films",
                                    "XXX movie",
                                    "XXX movies",
                                    "XXX flick",
                                    "XXX flicks",
                                    "triple X film",
                                    "triple X films",
                                    "triple X movie",
                                    "triple X movies",
                                    "triple X flick",
                                    "triple X flicks",
                                    "porn",
                                    "porno",
                                    "pornos",
                                    "porn video",
                                    "sex video",
                                    "sex film",
                                    "sex tape",
                                    "sex flick",
                                    "sex movie",
                                    "sex movies",
                                    "adult movies"
                                ]
                            }
                        }
                    ]
                },
                {
                    "concept": [
                        {
                            "grammar": {
                                "item": [
                                    "Monday",
                                    "Mon"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Tuesday",
                                    "Tues"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Wednesday",
                                    "Wed"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Thursday",
                                    "Thurs",
                                    "Thu"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Friday",
                                    "Fri"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Saturday",
                                    "Sat"
                                ]
                            }
                        },
                        {
                            "grammar": {
                                "item": [
                                    "Sunday",
                                    "Sun"
                                ]
                            }
                        }
                    ],
                    "@selectionType": "RANDOM",
                    "@label": "cdh"
                }
            ],
            (1, "concept"): [
                {
                    "grammar": GenericGrammar.create_hello()
                },
                {
                    "grammar": GenericGrammar.create_yes_goodbye()
                },
                {
                    "grammar": GenericGrammar.create_ok_thanks()
                },
                {
                    "grammar": GenericGrammar.create_yes_full()
                },
                {
                    "grammar": GenericGrammar.create_no()
                },
                {
                    "grammar": {
                        "item": [
                            "haha",
                            "ha",
                            "hehe",
                            "lol",
                            "rofl",
                            "lmao"
                        ]
                    }
                },
                {
                    "grammar": GenericGrammar.create_sorry()
                },
                {
                    "grammar": {
                        "item": [
                            "you",
                            "u"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "movie",
                            "movies",
                            "film",
                            "films",
                            "flick",
                            "flicks"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "theater",
                            "theaters",
                            "theatre",
                            "theatres",
                            "cinema",
                            "cinemas"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "showtime",
                            "showtimes",
                            "show time",
                            "show times",
                            "movie time",
                            "movie times"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "dining",
                            "restaurant",
                            "restaurants",
                            "place to eat",
                            "places to eat",
                            "diner",
                            "diners",
                            "cafe",
                            "cafes",
                            "cafeteria",
                            "cafeterias",
                            "Bar",
                            "Bars",
                            "Pub",
                            "Pubs",
                            "Tavern",
                            "Taverns",
                            "Brewery",
                            "Breweries",
                            "somewhere to eat",
                            "eatery",
                            "place to dine",
                            "somewhere nice to eat",
                            "eateries",
                            "places to dine",
                            "bistro",
                            "a bistro",
                            "bistros",
                            "coffee shop",
                            "coffee shops",
                            "coffee place",
                            "coffee places",
                            "eating house",
                            "eating houses",
                            "snack bar",
                            "snack bars",
                            "juice bar",
                            "juice bars",
                            "health food shop",
                            "fast food outlet",
                            "fast food shop",
                            "fast food outlets",
                            "fast food shops",
                            "food court",
                            "food courts",
                            "food mall",
                            "food malls"
                        ]
                    },
                    "@id": "concept_2456113"
                },
                {
                    "grammar": {
                        "item": [
                            "weather",
                            "Rain",
                            "Raining",
                            "Snow",
                            "Snowing",
                            "Sunny",
                            "Cloudy",
                            "Sleet",
                            "Freezing Rain",
                            "Windy",
                            "Tornado",
                            "Hurricane"
                        ]
                    },
                    "@id": "concept_weather"
                },
                {
                    "grammar": {
                        "item": [
                            "traffic",
                            "Traffic conditions",
                            "Driving conditions",
                            "Road conditions",
                            "Streets",
                            "Roads",
                            "Freeways",
                            "Highways",
                            "Driving",
                            "Rush hour",
                            "Bus",
                            "Buses",
                            "Train",
                            "Trains",
                            "Car",
                            "Cars",
                            "Automobile",
                            "Automobiles",
                            "Bicycle",
                            "Bicycles",
                            "Bike",
                            "Bikes",
                            "Motorcycle",
                            "Motorcycles",
                            "Walking",
                            "Driving",
                            "Pedestrian"
                        ]
                    },
                    "@id": "concept_2456118"
                },
                {
                    "grammar": {
                        "item": [
                            "what is",
                            "what's"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "Review",
                            "Reviews",
                            "Critique",
                            "Critiques",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "Ratings",
                            "Rating",
                            "Popularity",
                            "Tomatoes",
                            "stars"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "it",
                            "that"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "family-friendly",
                            "family",
                            "child",
                            "children",
                            "childrens",
                            "children's",
                            "kiddy",
                            "kids",
                            "kid's",
                            "kid",
                            "family friendly",
                            "family safe",
                            "kid friendly",
                            "child friendly",
                            "safe for kids",
                            "kid safe",
                            "suitable for children",
                            "suitable for kids",
                            "suitable for a child",
                            "suitable for a kid",
                            "child appropriate",
                            "appropriate for children",
                            "not adult",
                            "for families",
                            "for a family",
                            "no sex",
                            "no violence",
                            "clean"
                        ]
                    },
                    "@id": "concept_family_friendly"
                },
                {
                    "grammar": {
                        "item": [
                            "near me",
                            "by me",
                            "my area",
                            "close to me",
                            "close by",
                            "nearby",
                            "in the neighborhood",
                            "local",
                            "locally",
                            "fairly close",
                            "close to us",
                            "near to us",
                            "short drive",
                            "short walk",
                            "a short drive",
                            "a short walk",
                            "close",
                            "near",
                            "around the corner",
                            "just around the corner",
                            "short distance",
                            "a short distance",
                            "close at hand",
                            "short distance awat",
                            "a short distance away",
                            "walking distance",
                            "within walking distance",
                            "not a long distance",
                            "not far",
                            "not too far",
                            "not far away",
                            "not too far away",
                            "in my area",
                            "in the city",
                            "my zipcode",
                            "dowtown"
                        ]
                    }
                },
                {
                    "grammar": {
                        "item": [
                            "Adult",
                            "Adults Only",
                            "NC 17",
                            "NC-17",
                            "NC17",
                            "NC 17 rated",
                            "NC-17 rated",
                            "NC-17-rated",
                            "NC 17-rated",
                            "NC17 rated",
                            "NC17-rated",
                            "X",
                            "X-rated",
                            "X rated",
                            "XXX",
                            "XXX-rated",
                            "XXX rated",
                            "Triple X",
                            "Triple X-rated",
                            "Triple X rated",
                            "NC seventeen",
                            "NC-seventeen"
                        ]
                    },
                    "@id": "concept_porn"
                }
            ],
            "@label": "Concepts"
        }
