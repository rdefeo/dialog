from dialog.schema.factories.grammar import FeelingGrammar, ProfileGrammar, GenericGrammar


class MainFolder:
    @staticmethod
    def create():
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
                                    "@ref": "folder_preliminary_sequences"
                                },
                                {
                                    "@ref": "folder_routing_sequences"
                                },
                                {
                                    "@id": "search_2414740",
                                    "@ref": "folder_base_sequences"
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
