from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, RecencyPreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs import FavoritesInput, DetailsInput, ShowtimesInput
from dialog.schema.factories.profile_checks import GenrePreferenceProfileCheck, CertificationPreferenceProfileCheck, \
    RecencyPreferenceProfileCheck

__author__ = 'robdefeo'


class BaseSequences:
    @staticmethod
    def create():
        return {
            "@label": "BASE SEQUENCES",
            "@id": "folder_base_sequences",
            (0, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.create_reset()
            ],
            (1, "input"): [
                FavoritesInput.create(),
                DetailsInput.create(),
                ShowtimesInput.create(),
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
                        SmallTalkAction.create_reset(),
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
                        RecencyPreferenceAction.create_set_to_value()
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
                                    "action": RecencyPreferenceAction.create_set_to_upcoming(),
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
                                                "action": RecencyPreferenceAction().create_set_to_current(),
                                                "@ref": "input_2443775"
                                            }
                                        },
                                        (3, "goto"): {
                                            "action": RecencyPreferenceAction().create_set_to_upcoming(),
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
                            (1, "action"): RecencyPreferenceAction.create_set_to_value(),
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
                        RecencyPreferenceProfileCheck.create(),
                        GenrePreferenceProfileCheck.create(),
                        CertificationPreferenceProfileCheck.create(),
                    ],
                    (4, "output"): {
                        "@id": "output_2456875",
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
                                                            RecencyPreferenceAction.create_reset()
                                                        ],
                                                        (2, "goto"): {
                                                            "@ref": "profileCheck_recency_preference"
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
                                                                        RecencyPreferenceAction.create_reset()
                                                                    ],
                                                                    (2, "goto"): Goto(ref="output_how_can_i_help_you")
                                                                },
                                                                {
                                                                    (0, "grammar"): GenericGrammar.create_no(),
                                                                    (1, "output"): {
                                                                        (0, "prompt"): GenericGrammar.create_ok(),
                                                                        (1, "goto"): Goto(ref="output_did_find_what_looking_for")
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
                                                    RecencyPreferenceAction.create_set_to_value(),
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
                                                    RecencyPreferenceAction.create_set_to_value(),
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
                                                    RecencyPreferenceAction.create_set_to_value()
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
                                                    RecencyPreferenceAction.create_set_to_value()
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
                                                        "action": RecencyPreferenceAction.create_set_to_upcoming(),
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
                                                                    "action": RecencyPreferenceAction.create_set_to_current(),
                                                                    "@ref": "output_2456875"
                                                                }
                                                            },
                                                            (3, "goto"): {
                                                                "action": RecencyPreferenceAction.create_set_to_upcoming(),
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
                                                "@ref": "search_preliminary_sequences"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            ]
        }
