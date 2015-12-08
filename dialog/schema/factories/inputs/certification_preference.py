from dialog.schema.elements import Goto
from dialog.schema.factories.action import CertificationPreferenceAction



class FamilyFriendlyInput:
    @staticmethod
    def create():
        return {
            "@id": "input_family_friendly",
            (0, "grammar"): {
                "item": [
                    "family-friendly",
                    "$ family",
                    "$ childrens",
                    "$ child",
                    "$ kid"
                ]
            },
            (1, "action"): {
                "@varName": "Certification_Preference",
                "@operator": "SET_TO",
                "#text": "G"
            },
            (2, "goto"): Goto(ref="input_recency_preference")
        }


class CertificationPreferenceInput:
    @staticmethod
    def create():
        return {
            "@id": "input_certification_preference",
            (0, "grammar"): {
                "item": [
                    "rated",
                    "$(CERTIFICATION)={Certification_Preference}"
                ]
            },
            (1, "action"): CertificationPreferenceAction.create_set_to_value(),
            (2, "goto"): Goto(ref="input_family_friendly")
        }
