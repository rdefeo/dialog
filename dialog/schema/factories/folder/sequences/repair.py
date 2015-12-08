__author__ = 'robdefeo'


class RepairSequences:
    @staticmethod
    def create():
        return {
            "@label": "REPAIR SEQUENCES",
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
            ]
        }
