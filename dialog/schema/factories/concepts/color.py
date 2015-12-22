from dialog.elements import Concept, Grammar


class ColorConcept:
    @staticmethod
    def create():
        return {
            "@label": "Color",
            "concept": [
                Concept(
                    id="red",
                    grammars=[
                        Grammar(watson_items=["red"])
                    ]
                ),
                Concept(
                    id="white",
                    grammars=[
                        Grammar(watson_items=["white"])
                    ]
                ),
                Concept(
                    id="black",
                    grammars=[
                        Grammar(watson_items=["black"])
                    ]
                )
            ]
        }
