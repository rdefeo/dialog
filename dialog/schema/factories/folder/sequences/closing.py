__author__ = 'robdefeo'


class ClosingSequences:
    @staticmethod
    def create():
        return {
            "@label": "CLOSING SEQUENCES",
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
            ]
        }
