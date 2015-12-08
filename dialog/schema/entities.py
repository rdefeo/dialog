from dialog.schema.elements import Grammar, Entity, Value

__author__ = 'robdefeo'


class Entities:
    def create(self):
        return {
            "entity": [
                Entity(
                    "CERTIFICATION", [
                        Value("G", "G", Grammar(items=["G Rated", "G-Rated"])),
                        Value("PG", "PG", Grammar(items=["PG Rated", "PG-Rated"]))
                    ]
                ).create(),
                Entity(
                    "GENRE", [
                        Value("Action", "Action", Grammar(items=["Action"])),
                        Value("Adventure", "Adventure", Grammar(items=["Adventure"]))
                    ]
                ).create(),
                Entity(
                    "DYNAMIC_DATA", [
                        Value("DataCapture", "DataCapture", Grammar(items=["*"]))
                    ]
                ).create(),
                Entity(
                    "RECENCY", [
                        Value("Upcoming", "Upcoming", Grammar(items=["coming soon"])),
                        Value("Current", "Current", Grammar(items=["current", "recent", "now", "new"]))
                    ]
                ).create(),
                Entity(
                    "DINING", [

                    ]
                )
                # TODO
        #         <entity name="DINING">
        #     <value name="restaurants" value="restaurants">
        #         <concept ref="concept_2456113"/>
        #     </value>
        #     <value name="bars" value="bars"/>
        # </entity>
            ]
        }