from dialog.elements import Grammar, Entity, Value


class Entities:
    def create(self):
        from dialog.elements import Entities as EntitiesElement
        return EntitiesElement(
            [
                Entity(
                    "DYNAMIC_DATA", [
                        Value("DataCapture", "DataCapture", Grammar(items=["*"]))
                    ]
                ),
                Entity(
                    "STYLE", [
                        Value("high heels", "high heels", Grammar(items=["high heels", "high-heels"])),
                        Value("boots", "boots", Grammar(items=["boots", "boot"]))
                    ]
                ),
                Entity(
                    "COLOR", [
                        Value("red", "red", Grammar(items=["red"])),
                        Value("white", "white", Grammar(items=["white"])),
                        Value("black", "black", Grammar(items=["black"]))
                    ]
                ),
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
        )
