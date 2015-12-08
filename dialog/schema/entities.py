from dialog.schema.elements import Grammar, Entity, Value

__author__ = 'robdefeo'


class Entities:
    def create(self):
        return {
            "entity": [
                Entity(
                    "CERTIFICATION", [
                        Value("G", "G", Grammar(["G Rated", "G-Rated"])),
                        Value("PG", "PG", Grammar(["PG Rated", "PG-Rated"]))
                    ]
                ).create(),
                Entity(
                    "GENRE", [
                        Value("Action", "Action", Grammar(["Action"])),
                        Value("Adventure", "Adventure", Grammar(["Adventure"]))
                    ]
                ).create(),
                Entity(
                    "DYNAMIC_DATA", [
                        Value("DataCapture", "DataCapture", Grammar(["*"]))
                    ]
                ).create(),
                Entity(
                    "RECENCY", [
                        Value("Upcoming", "Upcoming", Grammar(["coming soon"])),
                        Value("Current", "Current", Grammar(["current", "recent", "now", "new"]))
                    ]
                ).create()

            ]
        }