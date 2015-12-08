from dialog.schema.elements import Goto


class ZipcodeInput:
    @staticmethod
    def create():
        return {
            "@id": "input_zipcode",
            (0, "grammar"): {
                "item": [
                    "near me",
                    "$ (ZIPCODE)={ZIP_Code_Preference}",
                    "$ near me"
                ]
            },
            (1, "action"): {
                "@varName": "ZIP_Code_Preference",
                "@operator": "SET_TO",
                "#text": "{ZIP_Code_Preference.value:main}"
            },
            (2, "goto"): Goto(ref="profileCheck_zipcode")
        }
