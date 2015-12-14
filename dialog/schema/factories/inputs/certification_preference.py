from dialog.schema.elements import Goto, Grammar
from dialog.schema.factories.action import CertificationPreferenceAction
from dialog.schema.factories.inputs.style import StylePreferenceInput

#
# class FamilyFriendlyInput:
#     @staticmethod
#     def create():
#         return {
#             "@id": "input_family_friendly",
#             (0, "grammar"): {
#                 "item": [
#                     "family-friendly",
#                     "$ family",
#                     "$ childrens",
#                     "$ child",
#                     "$ kid"
#                 ]
#             },
#             (1, "action"): {
#                 "@varName": "Certification_Preference",
#                 "@operator": "SET_TO",
#                 "#text": "G"
#             },
#             (2, "goto"): StylePreferenceInput.goto()
#         }
#
#
# class CertificationPreferenceInput:
#     @staticmethod
#     def goto():
#         return Goto(ref=CertificationPreferenceInput.__id())
#
#     @staticmethod
#     def __id():
#         return "input_certification_preference"
#
#
#     @staticmethod
#     def create():
#         return {
#             "@id": CertificationPreferenceInput.__id(),
#             (0, "grammar"): Grammar(
#                 items=[
#                     "rated",
#                     "$(CERTIFICATION)={Certification_Preference}"
#                 ]
#             ),
#             (1, "action"): CertificationPreferenceAction.set_to_value(),
#             (2, "goto"): Goto(ref="input_family_friendly")
#         }
