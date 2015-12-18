from dialog.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, RecencyPreferenceAction, \
    CertificationPreferenceAction, StylePreferenceAction, ColorPreferenceAction, PageAction
from dialog.schema.factories.conditions import ColorConditions, StyleConditions
# from dialog.schema.factories.conditions.certification import CertificationsConditions
from dialog.schema.factories.conditions.results_count import ResultsCountConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs import \
    RemoveGenreInput, RemoveRatingInput, RemoveAllSearchCriteriaInput
from dialog.schema.factories.inputs.after_search_results import AfterSearchResults
from dialog.schema.factories.inputs.color import ColorPreferenceInput
from dialog.schema.factories.inputs.style import StylePreferenceInput
from dialog.schema.factories.inputs.zipcode import ZipcodeInput
from dialog.schema.factories.outputs.anything_else_can_help_with import AnythingElseCanHelpWith
from dialog.schema.factories.profile_checks import StylePreferenceProfileCheck, ColorPreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch
from dialog.schema.factories.variables import NAME_RESULTS_COUNT


class MainSearchCriteriaInput:
    @staticmethod
    def create():
        return {
            "@id": "input_main_search_criteria",
            (0, "grammar"): {
                "item": [
                    "Movies",
                    "blobbly",
                    "$ (COLOR)={Color_Preference}",
                    "$ (STYLE)={Style_Preference}",
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
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                {
                    "@varName": "Current_Index",
                    "@operator": "SET_TO",
                    "#text": "0"
                },
                PageAction.set_to_new(),
                {
                    "@varName": "Topic",
                    "@operator": "SET_TO",
                    "#text": "movies"
                },
                CertificationPreferenceAction.set_to_value(),
                StylePreferenceAction.set_to_value()
            ],
            (2, "input"): [
                # DateTimeInput.create(),
                # CertificationPreferenceInput.create(),
                # FamilyFriendlyInput.create(),
                ColorPreferenceInput.create(StylePreferenceInput.goto()),
                StylePreferenceInput.create(Goto(ref="input_zipcode")),
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
                StylePreferenceProfileCheck.create(),
                # GenrePreferenceProfileCheck.create(),
                ColorPreferenceProfileCheck.create(),
            ],
            (4, "output"): {
                "@id": "output_ok_do_search",
                (0, "prompt"): GenericPrompt.ok(),
                (1, "output"): {
                    "@id": "output_2456876",
                    (0, "prompt"): {
                        "item": "\"{\"Search_Now\":\"{Search_Now}\", \"Style\":\"{Style_Preference}\", \"Color\":\"{Color_Preference}\", \"Index\":\"{Current_Index}\", \"Page\":\"{Page}\"}\"",
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
                                    (0, "cond"): ResultsCountConditions.equals_zero(),
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I'm afraid I found {%s} matching {Color_Preference} {Style_Preference}. Try changing your criteria." % NAME_RESULTS_COUNT,
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "getUserInput"): {
                                            (0, "input"): {
                                                (0, "grammar"): GenericGrammar.ok(),
                                                (1, "action"): [
                                                    ColorPreferenceAction.set_to_blank(),
                                                    StylePreferenceAction.set_to_blank()
                                                ],
                                                (2, "goto"): StylePreferenceProfileCheck.goto()
                                            },
                                            (1, "goto"): RemoveGenreInput.goto()
                                        }
                                    }
                                },
                                {
                                    (0, "cond"): [
                                        StyleConditions.is_blank(),
                                        ColorConditions.has_value()
                                    ],
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "Good choice, {User_Name}! I found {%s} results for {Recency_Preference} {Color_Preference}-rated movies." % NAME_RESULTS_COUNT,
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): AfterSearchResults.goto()
                                    }
                                },
                                {
                                    (0, "cond"): [
                                        ColorConditions.is_blank(),
                                        StyleConditions.has_value()
                                    ],
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "Good choice, {User_Name}! I found {%s} results for {Color_Preference} {Style_Preference} movies." % NAME_RESULTS_COUNT,
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): AfterSearchResults.goto()
                                    }
                                },
                                {
                                    (0, "cond"): [
                                        ColorConditions.is_blank(),
                                        StyleConditions.is_blank()
                                    ],
                                    (1, "output"): {
                                        (0, "prompt"): {
                                            "item": "I found {%s} results for ALL {Recency_Preference} movies." % NAME_RESULTS_COUNT,
                                            "@selectionType": "RANDOM"
                                        },
                                        (1, "goto"): AfterSearchResults.goto()
                                    }
                                }
                            ],
                            (2, "output"): {
                                (0, "prompt"): {
                                    "item": "Good choices, {User_Name}! I found {%s} results for {Color_Preference} {Style_Preference} movies." % NAME_RESULTS_COUNT,
                                    "@selectionType": "RANDOM"
                                },
                                (1, "getUserInput"): AfterSearchResults.create()
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
            (1, "action"): PageAction.set_to_repeat(),
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
                PageAction.set_to_previous(),
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
                        "item": "\"{Search_Now:\"{Search_Now}\", Style:\"{Style_Preference}\", Rating:\"{Color_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\"}\"",
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
                                        (2, "goto"): AfterSearchResults.goto()
                                    }
                                }
                            ],
                            (3, "output"): {
                                (0, "prompt"): {
                                    "item": "Here is the previous set of results",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): AfterSearchResults.goto()
                            }
                        }
                    }
                }
            }
        }


# class GenreRecencyPreference:
#     @staticmethod
#     def create():
#         return {
#             (0, "grammar"): {
#                 "item": [
#                     "Genre and Rating",
#                     "$ (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference}",
#                     "$ (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference}"
#                 ]
#             },
#             (1, "action"): [
#                 {
#                     "@varName": "Current_Index",
#                     "@operator": "SET_TO",
#                     "#text": "0"
#                 },
#                 GenrePreferenceAction.set_to_value(),
#                 {
#                     "@varName": "Page",
#                     "@operator": "SET_TO",
#                     "#text": "new"
#                 },
#                 CertificationPreferenceAction.set_to_value()
#             ],
#             (2, "goto"): Goto(ref="output_ok_do_search")
#         }


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
                PageAction.set_to_new(),
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
                PageAction.set_to_next()
            ],
            (2, "output"): {
                (0, "prompt"): {
                    "item": "Okay."
                },
                (1, "output"): {
                    (0, "prompt"): {
                        "item": "\"{Search_Now:\"{Search_Now}\", Color:\"{Color_Preference}\", Style:\"{Style_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\", Total_Movies:\"{%s}\", Total_Pages:\"{Total_Pages}\"}\"" % NAME_RESULTS_COUNT
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
                                        "#text": "{%s}" % NAME_RESULTS_COUNT
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
                                            StyleConditions.is_blank(),
                                            ColorConditions.has_value()
                                        ],
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "for {Style_Preference} {Color_Preference}-rated movies."
                                            },
                                            (1, "goto"): AfterSearchResults.goto()
                                        }
                                    },
                                    {
                                        (0, "cond"): [
                                            ColorConditions.is_blank(),
                                            StyleConditions.has_value()
                                        ],
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "for {Recency_Preference} {Genre_Preference} movies."
                                            },
                                            (1, "goto"): AfterSearchResults.goto()
                                        }
                                    },
                                    {
                                        (0, "cond"): [
                                            ColorConditions.is_blank(),
                                            StyleConditions.is_blank()
                                        ],
                                        (1, "output"): {
                                            (0, "prompt"): {
                                                "item": "for ALL {Recency_Preference} movies."
                                            },
                                            (1, "goto"): AfterSearchResults.goto()
                                        }
                                    }
                                ],
                                (2, "output"): {
                                    (0, "prompt"): {
                                        "item": "for {Recency_Preference} {Certification_Preference}-rated {Genre_Preference} movies."
                                    },
                                    (1, "goto"): AfterSearchResults.goto()
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
                # GenrePreferenceAction.set_to_value(),
                PageAction.set_to_new()
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


# class RecencyGenreRatingPreference:
#     @staticmethod
#     def create():
#         return {
#             (0, "grammar"): {
#                 "item": [
#                     "Recency, Genre and Rating",
#                     "$ (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference}",
#                     "$ (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference} ",
#                     "$ (GENRE)={Genre_Preference} (RECENCY)={Recency_Preference} (CERTIFICATION)={Certification_Preference}",
#                     "$ (GENRE)={Genre_Preference} (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference} ",
#                     "$ (CERTIFICATION)={Certification_Preference} (GENRE)={Genre_Preference} (RECENCY)={Recency_Preference}",
#                     "$ (CERTIFICATION)={Certification_Preference} (RECENCY)={Recency_Preference} (GENRE)={Genre_Preference}"
#                 ]
#             },
#             (1, "action"): [
#                 RecencyPreferenceAction.create_set_to_value(),
#                 GenrePreferenceAction.set_to_value(),
#                 {
#                     "@varName": "Page",
#                     "@operator": "SET_TO",
#                     "#text": "new"
#                 },
#                 CertificationPreferenceAction.set_to_value()
#             ],
#             (2, "goto"): Goto(ref="output_ok_do_search")
#         }


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
                (1, "goto"): AfterSearchResults.goto()
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


# class CertificationPreference:
#     @staticmethod
#     def create():
#         return {
#             (0, "grammar"): {
#                 "item": [
#                     "Rating",
#                     "$ (CERTIFICATION)={Certification_Preference}"
#                 ]
#             },
#             (1, "action"): [
#                 {
#                     "@varName": "Current_Index",
#                     "@operator": "SET_TO",
#                     "#text": "0"
#                 },
#                 {
#                     "@varName": "Page",
#                     "@operator": "SET_TO",
#                     "#text": "new"
#                 },
#                 CertificationPreferenceAction.set_to_value()
#             ],
#             (2, "input"): {
#                 (0, "grammar"): {
#                     "item": [
#                         "all",
#                         "$ all",
#                         "$ any"
#                     ]
#                 },
#                 (1, "action"): GenrePreferenceAction.set_to_blank(),
#                 (2, "goto"): Goto(ref="output_ok_do_search")
#             },
#             (3, "goto"): Goto(ref="output_ok_do_search")
#         }


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
                PageAction.set_to_new(),
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
