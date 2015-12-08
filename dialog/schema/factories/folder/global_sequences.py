from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar, FeelingGrammar

__author__ = 'robdefeo'


class GlobalSequences:
    @staticmethod
    def create():
        return {
            "@selectionType": "RANDOM",
            "@label": "GLOBAL SEQUENCES",
            "@id": "folder_global_sequences",
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
                                                    "@ref": "output_ask_for_recency"
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
                                                    "@ref": "output_ask_for_recency"
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
                                                    "@ref": "output_ask_for_recency"
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
                                                    "@ref": "output_ask_for_recency"
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
                                    "@ref": "output_did_find_what_looking_for"
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
                                    "@ref": "output_did_find_what_looking_for"
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
                    (0, "action"): SmallTalkAction.create_increment(),
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
        }
