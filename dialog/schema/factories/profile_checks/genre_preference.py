from dialog.schema.elements import Goto
from dialog.schema.factories.action import CertificationPreferenceAction, GenrePreferenceAction
from dialog.schema.factories.conditions.genre import GenreConditions
from dialog.schema.factories.grammar import GenericGrammar


class GenrePreferenceProfileCheck:
    @staticmethod
    def goto():
        return Goto(ref=GenrePreferenceProfileCheck.__id())

    @staticmethod
    def __id():
        return "profileCheck_genre_preference"

    @staticmethod
    def create():
        return {
            "@id": GenrePreferenceProfileCheck.__id(),
            (0, "cond"): GenreConditions.is_blank(),
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
                                CertificationPreferenceAction.set_to_value(),
                                GenrePreferenceAction.set_to_value(),
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
                                GenrePreferenceAction.set_to_value(),
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
                            (0, "grammar"): GenericGrammar.create_no_preference(),
                            (1, "goto"): Goto(ref="profileCheck_certification_preference")
                        },
                        {
                            (0, "grammar"): {
                                "item": GenericGrammar.yes()
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
