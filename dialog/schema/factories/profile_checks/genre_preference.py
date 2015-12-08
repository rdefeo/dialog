from dialog.schema.elements import Goto


class GenrePreferenceProfileCheck:
    @staticmethod
    def create():
        return {
            "@id": "profileCheck_genre_preference",
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
                                    "@ref": "profileCheck_certification_preference"
                                }
                            },
                            (3, "goto"): Goto(ref="profileCheck_certification_preference")
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
                                    "@ref": "profileCheck_certification_preference"
                                }
                            },
                            (3, "goto"): Goto(ref="profileCheck_certification_preference")
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
                            (1, "goto"): Goto(ref="profileCheck_certification_preference")
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
                        "@ref": "search_preliminary_sequences"
                    }
                }
            }
        }
