from dialog.schema.factories.action import GreetingAction, SmallTalkAction

__author__ = 'robdefeo'


class RoutingSequences:
    @staticmethod
    def create():
        return {
            "@id": "folder_routing_sequences",
            "@selectionType": "RANDOM",
            "@label": "ROUTING SEQUENCES",
            (0, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.create_reset()
            ],
            (1, "input"): [
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
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "by out-of-scope movie topics",
                            "$ (BY_OTHER_MOVIE)={Topic}"
                        ]
                    },
                    (1, "action"): {
                        "@varName": "Topic",
                        "@operator": "SET_TO",
                        "#text": "{Topic.value:main}"
                    },
                    (2, "goto"): {
                        "@ref": "output_2503370"
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "unsupported genres",
                            "$ (UNSUPPORTED_GENRES)={Topic}"
                        ]
                    },
                    (1, "action"): {
                        "@varName": "Topic",
                        "@operator": "SET_TO",
                        "#text": "{Topic.value:main}"
                    },
                    (2, "goto"): {
                        "@ref": "output_2510164"
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "old movies",
                            "$ old movies",
                            "$ classic movies",
                            "$ oldies",
                            "$ classics"
                        ]
                    },
                    (1, "goto"): {
                        "@ref": "output_2503380"
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Review",
                            "$ review",
                            "$ find movies by rating",
                            "$ look up movies by rating",
                            "$ highest rating",
                            "$ highest rated",
                            "$ best rating",
                            "$ best rated",
                            "$ lowest rating",
                            "$ lowest rated",
                            "$ oscar winners",
                            "$ best movie",
                            "$ best movies"
                        ]
                    },
                    (1, "action"): [
                        GreetingAction.create_reset(),
                        SmallTalkAction.create_reset()
                    ],
                    (2, "goto"): {
                        "@ref": "output_2469539"
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "Movie theaters",
                            "$ movie theaters"
                        ]
                    },
                    (1, "goto"): {
                        "@ref": "output_2503320"
                    }
                },
                {
                    (0, "grammar"): {
                        "item": [
                            "trailer",
                            "$ trailer",
                            "$ trailers"
                        ]
                    },
                    (1, "action"): [
                        GreetingAction.create_reset(),
                        {
                            "@varName": "Small_Talk_Count",
                            "@operator": "SET_TO",
                            "#text": "0"
                        }
                    ],
                    (2, "goto"): {
                        "@ref": "output_2510290"
                    }
                }
            ]
        }
