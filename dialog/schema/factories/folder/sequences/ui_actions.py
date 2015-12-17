from dialog.schema.factories.inputs import AfterSearchResults

__author__ = 'robdefeo'


class UIActionsSequences:
    @staticmethod
    def create():
        return {
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
                                (1, "goto"): AfterSearchResults.goto()
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
                                (1, "goto"): AfterSearchResults.goto()
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
                        (1, "goto"): AfterSearchResults.goto()
                    }
                }
            }
        }
