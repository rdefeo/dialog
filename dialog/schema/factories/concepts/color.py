from dialog.elements import Concept, Grammar, Folder


class ColorConcept:
    @staticmethod
    def create():
        return Folder(
            label="Color",
            children=[
                Concept(
                    _id="red",
                    grammars=[
                        Grammar(watson_items=["red"])
                    ]
                ),
                Concept(
                    _id="white",
                    grammars=[
                        Grammar(watson_items=["white"])
                    ]
                ),
                Concept(
                    _id="black",
                    grammars=[
                        Grammar(watson_items=["black"])
                    ]
                )
            ]
        )
