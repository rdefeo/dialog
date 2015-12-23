from dialog.elements import Concept, Grammar, Folder


class StyleConcept:
    @staticmethod
    def create():
        return Folder(
            label="Style",
            children=[
                Concept(
                    _id="high heels",
                    grammars=[
                        Grammar(watson_items=["high heels", "high-heels"])
                    ]
                ),
                Concept(
                    _id="boots",
                    grammars=[
                        Grammar(watson_items=["boots", "boot"])
                    ]
                )
            ]
        )
