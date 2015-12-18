from dialog.elements import Concept, Grammar


class StyleConcept:
    @staticmethod
    def create():
        return {
            "@label": "Style",
            "concept": [
                Concept(
                    id="high heels",
                    grammars=[
                        Grammar(items=["high heels", "high-heels"])
                    ]
                ),
                Concept(
                    id="boots",
                    grammars=[
                        Grammar(items=["boots", "boot"])
                    ]
                )
            ]
        }
