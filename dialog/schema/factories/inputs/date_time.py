from dialog.schema.factories.action import RecencyPreferenceAction


# class RecencyPreferenceInput:
#     @staticmethod
#     def create():
#         return {
#             "@id": "input_recency_preference",
#             (0, "grammar"): {
#                 "item": [
#                     "how recent",
#                     "$ (RECENCY)={Recency_Preference}"
#                 ]
#             },
#             (1, "action"): RecencyPreferenceAction.create_set_to_value(),
#             (2, "goto"): {
#                 "@ref": "input_zipcode"
#             }
#         }


class DateTimeInput:
    @staticmethod
    def create():
        from dialog.schema.factories.inputs import CertificationPreferenceInput
        return {
            "@id": "input_date_time",
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
                    "@ref": "profileCheck_2503417"
                }
            },
            (3, "if"): {
                "@id": "profileCheck_2503417",
                (0, "cond"): {
                    "@varName": "Recency_Preference",
                    "@operator": "EQUALS",
                    "#text": "Upcoming"
                },
                (1, "goto"): CertificationPreferenceInput.goto()
            },
            (4, "output"): {
                (0, "prompt"): {
                    "@selectionType": "RANDOM"
                },
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
                                "action": RecencyPreferenceAction().set_to_current(),
                                "@ref": "input_certification_preference"
                            }
                        },
                        (3, "goto"): {
                            "action": RecencyPreferenceAction().create_set_to_upcoming(),
                            "@ref": "input_certification_preference"
                        }
                    }
                },
                (2, "goto"): CertificationPreferenceInput.goto()
            }
        }
