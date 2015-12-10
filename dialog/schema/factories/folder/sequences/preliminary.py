from dialog.schema.factories.action import GreetingAction, SmallTalkAction, GenrePreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYou
from dialog.schema.factories.prompts.generic import GenericPrompt

__author__ = 'robdefeo'


class PreliminarySequences:
    @staticmethod
    def create():
        return {
            "@label": "PRELIMINARY SEQUENCES",
            "@id": "folder_preliminary_sequences",
            (0, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.set_to_zero()
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
                    SmallTalkAction.set_to_zero()
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
                                "@ref": "output_no_topic_lookup"
                            }
                        },
                        (3, "output"): {
                            (0, "prompt"): {
                                "item": "No.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "output"): {
                                "@id": "output_no_topic_lookup",
                                (0, "prompt"): {
                                    "item": "I'm afraid I can't look up movies by {Topic}, only by Genre or MPAA Rating.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
                                    }
                                }
                            }
                        }
                    },
                    {
                        (0, "grammar"): {
                            "item": "$ (GENRE)={Genre_Preference}"
                        },
                        (1, "action"): GenrePreferenceAction.set_to_value(),
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
                                    (1, "goto"): HowCanHelpYou.goto()
                                },
                                (1, "goto"): {
                                    "@ref": "search_preliminary_sequences"
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
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                "@ref": "output_what_jemboo_knows"
                            }
                        },
                        (3, "output"): {
                            (0, "prompt"): {
                                "item": "Yes.",
                                "@selectionType": "RANDOM"
                            },
                            (1, "output"): {
                                "@id": "output_what_jemboo_knows",
                                (0, "prompt"): {
                                    "item": "I can look up current and upcoming movies by Genre or MPAA Rating and show you trailers for them. But I'm afraid I cannot search by number of stars or by movie titles or actor and director names at this time.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): {
                                    (0, "input"): {
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (0, "grammar"): GenericGrammar.ok(),
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                            (0, "grammar"): GenericGrammar.yes(),
                                            (1, "goto"): {
                                                "@ref": "output_ask_for_recency"
                                            }
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
                                            (1, "goto"): {
                                                "@ref": "output_ask_for_recency"
                                            }
                                        }
                                    ],
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
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
                                        (1, "goto"): HowCanHelpYou.goto()
                                    },
                                    (1, "goto"): {
                                        "@ref": "search_preliminary_sequences"
                                    }
                                },
                                "@id": "output_2497989"
                            }
                        }
                    }
                ],
                (3, "goto"): {
                    "@ref": "output_what_jemboo_knows"
                }
            }
        }
