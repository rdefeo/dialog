from dialog.schema.elements import Goto
from dialog.schema.factories.action import RecencyPreferenceAction


class RecencyPreferenceProfileCheck:
    @staticmethod
    def create():
        return {
            "@id": "profileCheck_recency_preference",
            (0, "cond"): {
                "@varName": "Recency_Preference",
                "@operator": "IS_BLANK"
            },
            (1, "output"): {
                "@id": "output_ask_for_recency",
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
                                RecencyPreferenceAction.create_set_to_value()
                            ],
                            (2, "goto"): Goto(ref="profileCheck_genre_preference")
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
                                RecencyPreferenceAction.create_set_to_value(),
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
                            (2, "goto"): Goto(ref="profileCheck_genre_preference")
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "how recent",
                                    "$ (RECENCY)={Recency_Preference}"
                                ]
                            },
                            (1, "action"): [
                                RecencyPreferenceAction.create_set_to_value(),
                                {
                                    "@varName": "Current_Index",
                                    "@operator": "SET_TO",
                                    "#text": "0"
                                }
                            ],
                            (2, "goto"): Goto(ref="profileCheck_genre_preference")
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
                    (1, "goto"): Goto(ref="search_preliminary_sequences")
                }
            }
        }