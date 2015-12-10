from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, RecencyPreferenceAction, \
    CertificationPreferenceAction, GenrePreferenceAction
from dialog.schema.factories.conditions.certification import CertificationsConditions
from dialog.schema.factories.conditions.genre import GenreConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs import DateTimeInput, CertificationPreferenceInput, FamilyFriendlyInput, \
    RecencyPreferenceInput, ZipcodeInput, RemoveGenreInput, RemoveRatingInput, RemoveAllSearchCriteriaInput
from dialog.schema.factories.outputs.anything_else_can_help_with import AnythingElseCanHelpWith
from dialog.schema.factories.profile_checks import GenrePreferenceProfileCheck, CertificationPreferenceProfileCheck, \
    RecencyPreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt

__author__ = 'robdefeo'


class MainSearchCriteriaInput:
    @staticmethod
    def create():
        return {
            "@id": "input_main_search_criteria",
            (0, "grammar"): {
                "item": [
                    "Movies",
                    "blobbly",
                    "$ (GENRE)={Genre_Preference}",
                    "$ (CERTIFICATION)={Certification_Preference}",
                    "$ (RECENCY)={Recency_Preference}",
                    # "$ movies"
                ]
            },
            # (0.5, "output"): {
            #     (0, "prompt"): {
            #         "item": "Totall cool man",
            #         "@selectionType": "RANDOM"
            #     },
            #     (1, "goto"): Goto(ref="getUserInput_2456877")
            # },
            # Reset variables
            (1, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.set_to_zero(),
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
                GenrePreferenceAction.set_to_value(),
                {
                    "@varName": "Topic",
                    "@operator": "SET_TO",
                    "#text": "movies"
                },
                CertificationPreferenceAction.set_to_value(),
                RecencyPreferenceAction.create_set_to_value()
            ],
            (2, "input"): [
                DateTimeInput.create(),
                CertificationPreferenceInput.create(),
                FamilyFriendlyInput.create(),
                RecencyPreferenceInput.create(),
                ZipcodeInput.create(),
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
                    (2, "goto"): Goto(ref="output_no_topic_lookup")
                }
            ],
            (3, "if"): [
                RecencyPreferenceProfileCheck.create(),
                GenrePreferenceProfileCheck.create(),
                CertificationPreferenceProfileCheck.create(),
            ],
            (4, "output"): {
                "@id": "output_ok_do_search",
                (0, "prompt"): GenericPrompt.ok(),
                (1, "output"): {
                    "@id": "output_2456876",
                    (0, "prompt"): {
                        "item": "\"{\"Search_Now\":\"{Search_Now}\", \"Recency\":\"{Recency_Preference}\", \"Rating\":\"{Certification_Preference}\", \"Genre\":\"{Genre_Preference}\", \"Index\":\"{Current_Index}\", \"Page\":\"{Page}\"}\"",
                        "@selectionType": "RANDOM"
                    },
                    (1, "action"): SetVariablesNewSearchAction.create(),
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
                                                (0, "grammar"): GenericGrammar.ok(),
                                                (1, "action"): [
                                                    CertificationPreferenceAction.set_to_blank(),
                                                    GenrePreferenceAction.set_to_blank(),
                                                    RecencyPreferenceAction.set_to_blank()
                                                ],
                                                (2, "goto"): {
                                                    "@ref": "profileCheck_recency_preference"
                                                }
                                            },
                                            (1, "goto"): RemoveGenreInput.goto()
                                        }
                                    }
                                },
                                {
                                    (0, "cond"): [
                                        GenreConditions.is_blank(),
                                        CertificationsConditions.has_value()
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
                                        CertificationsConditions.is_blank(),
                                        GenreConditions.has_value()
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
                                        CertificationsConditions.is_blank(),
                                        GenreConditions.is_blank()
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
                                    (5, "input"): RemoveGenreInput.create(),
                                    (6, "input"): RemoveRatingInput.create(),
                                    (7, "input"): RemoveAllSearchCriteriaInput.create(),
                                    (8, "input"): Showtimes.create(),
                                    (9, "input"): RecencyGenreRatingPreference.create(),
                                    (10, "input"): RecencyGenrePreference.create(),
                                    (11, "input"): RecencyRatingPreference.create(),
                                    (12, "input"): GenreRecencyPreference.create(),
                                    (13, "input"): RecencyPreference.create(),
                                    (14, "input"): GenrePreference.create(),
                                    (15, "input"): CertificationPreference.create(),
                                    (16, "input"): UnsupportedGenre.create(),
                                    (17, "input"): DateTimePreference.create(),
                                    (18, "input"): AgainOption.create(),
                                    (19, "input"): MoreOption.create(),
                                    (20, "input"): GoBackOption.create(),
                                    (21, "goto"): Goto(ref="search_preliminary_sequences")
                                }
                            }
                        }
                    }
                }
            }
        }


class Showtimes:
    @staticmethod
    def create():
        return {
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
                "@ref": "output_ask_search_for_movies_in_area"
            }
        }


class GenrePreference:
    @staticmethod
    def create():
        return {
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
                GenrePreferenceAction.set_to_value()
            ],
            (2, "input"): {
                (0, "grammar"): {
                    "item": [
                        "all",
                        "$ all",
                        "$ just"
                    ]
                },
                (1, "action"): CertificationPreferenceAction.set_to_blank(),
                (2, "goto"): Goto(ref="output_ok_do_search")
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
                    "@ref": "output_ok_do_search"
                }
            },
            (4, "goto"): Goto(ref="output_ok_do_search")
        }


class AgainOption:
    @staticmethod
    def create():
        return {
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
            (2, "goto"): Goto(ref="output_ok_do_search")
        }


class GoBackOption:
    @staticmethod
    def create():
        return {
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
                (0, "prompt"): GenericPrompt.ok(),
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
        }


class GenreRecencyPreference:
    @staticmethod
    def create():
        return {
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
                GenrePreferenceAction.set_to_value(),
                {
                    "@varName": "Page",
                    "@operator": "SET_TO",
                    "#text": "new"
                },
                CertificationPreferenceAction.set_to_value()
            ],
            (2, "goto"): Goto(ref="output_ok_do_search")
        }


class RecencyRatingPreference:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "Recency and Rating",
                    "$ (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference}",
                    "$ (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference}"
                ]
            },
            (1, "action"): [
                CertificationPreferenceAction.set_to_value(),
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
            (2, "goto"): Goto(ref="output_ok_do_search")
        }


class MoreOption:
    @staticmethod
    def create():
        return {
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
                                            GenreConditions.is_blank(),
                                            CertificationsConditions.has_value()
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
                                            CertificationsConditions.is_blank(),
                                            GenreConditions.has_value()
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
                                            CertificationsConditions.is_blank(),
                                            GenreConditions.is_blank()
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
        }


class RecencyGenrePreference:
    @staticmethod
    def create():
        return {
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
                GenrePreferenceAction.set_to_value(),
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
                    "@ref": "output_ok_do_search"
                }
            },
            (3, "goto"): Goto(ref="output_ok_do_search")
        }


class RecencyGenreRatingPreference:
    @staticmethod
    def create():
        return {
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
                GenrePreferenceAction.set_to_value(),
                {
                    "@varName": "Page",
                    "@operator": "SET_TO",
                    "#text": "new"
                },
                CertificationPreferenceAction.set_to_value()
            ],
            (2, "goto"): Goto(ref="output_ok_do_search")
        }


class UnsupportedGenre:
    @staticmethod
    def create():
        return {
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
        }


class DateTimePreference:
    @staticmethod
    def create():
        return {
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
                (1, "goto"): Goto(ref="output_ok_do_search")
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
                                "action": RecencyPreferenceAction.set_to_current(),
                                "@ref": "output_ok_do_search"
                            }
                        },
                        (3, "goto"): {
                            "action": RecencyPreferenceAction.create_set_to_upcoming(),
                            "@ref": "output_ok_do_search"
                        }
                    }
                },
                (2, "goto"): Goto(ref="output_ok_do_search")
            }
        }


class CertificationPreference:
    @staticmethod
    def create():
        return {
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
                CertificationPreferenceAction.set_to_value()
            ],
            (2, "input"): {
                (0, "grammar"): {
                    "item": [
                        "all",
                        "$ all",
                        "$ any"
                    ]
                },
                (1, "action"): GenrePreferenceAction.set_to_blank(),
                (2, "goto"): Goto(ref="output_ok_do_search")
            },
            (3, "goto"): Goto(ref="output_ok_do_search")
        }


class RecencyPreference:
    @staticmethod
    def create():
        return {
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
                    CertificationPreferenceAction.set_to_blank(),
                    {
                        "@varName": "Genre_Preference",
                        "@operator": "SET_TO_BLANK"
                    }
                ],
                (2, "goto"): Goto(ref="output_ok_do_search")
            },
            (3, "goto"): Goto(ref="output_ok_do_search")
        }


class SetVariablesNewSearchAction:
    @staticmethod
    def create():
        return [
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
        ]
