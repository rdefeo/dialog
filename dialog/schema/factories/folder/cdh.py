from dialog.elements import Concept, Grammar, Folder


class CDHFolder:
    @staticmethod
    def create():
        return Folder(
            label="cdh",
            children=[
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Monday",
                            "Mon"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Tuesday",
                            "Tues"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Wednesday",
                            "Wed"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Thursday",
                            "Thurs",
                            "Thu"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Friday",
                            "Fri"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Saturday",
                            "Sat"
                        ]
                    )
                ),
                Concept(
                    grammar=Grammar(
                        watson_items=[
                            "Sunday",
                            "Sun"
                        ]
                    )
                )
            ]
        )
