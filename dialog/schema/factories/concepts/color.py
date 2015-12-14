from dialog.schema.elements import Concept, Grammar


class ColorConcept:
    @staticmethod
    def create():
        return {
            "@label": "Color",
            "concept": [
                Concept(
                    id="red",
                    grammars=[
                        Grammar(items=["red"])
                    ]
                ),
                Concept(
                    id="white",
                    grammars=[
                        Grammar(items=["white"])
                    ]
                ),
                Concept(
                    id="black",
                    grammars=[
                        Grammar(items=["black"])
                    ]
                )
            ]
        }
