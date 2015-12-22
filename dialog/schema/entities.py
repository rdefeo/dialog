from dialog.elements import Grammar, Entity, Value

__author__ = 'robdefeo'


class Entities:
    def create(self):
        return {
            "entity": [
                Entity(
                    "CERTIFICATION", [
                        Value("G", "G", Grammar(watson_items=["G Rated", "G-Rated"])),
                        Value("PG", "PG", Grammar(watson_items=["PG Rated", "PG-Rated"]))
                    ]
                ).create(),
                Entity(
                    "GENRE", [
                        Value("Action", "Action", Grammar(watson_items=["Action"])),
                        Value("Adventure", "Adventure", Grammar(watson_items=["Adventure"]))
                    ]
                ).create(),
                Entity(
                    "DYNAMIC_DATA", [
                        Value("DataCapture", "DataCapture", Grammar(watson_items=["*"]))
                    ]
                ).create(),
                Entity(
                    "STYLE", [
                        Value("high heels", "high heels", Grammar(watson_items=["high heels", "high-heels"])),
                        Value("boots", "boots", Grammar(watson_items=["boots", "boot"]))
                    ]
                ).create(),
                Entity(
                    "COLOR", [
                        Value("red", "red", Grammar(watson_items=["red"])),
                        Value("white", "white", Grammar(watson_items=["white"])),
                        Value("black", "black", Grammar(watson_items=["black"]))
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