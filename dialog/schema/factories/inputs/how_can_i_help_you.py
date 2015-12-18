from dialog.elements import Goto
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class HowCanHelpYouInput:
    @staticmethod
    def goto():
        return Goto(ref=HowCanHelpYouInput.__id())

    @staticmethod
    def __id():
        return "getUserInput_how_can_i_help_you"

    @staticmethod
    def create():
        return {
            "@id": HowCanHelpYouInput.__id(),
            (0, "search"): [
                PreliminarySequencesSearch.create(),
                {
                    "@ref": "folder_routing_sequences"
                },
                {
                    "@id": "search_2414740",
                    "@ref": "folder_base_sequences"
                }
            ],
            (1, "default"): {
                (0, "output"): {
                    "@isInsertDNRStatement": "true",
                    (0, "prompt"): {
                        "item": "I'm not sure what you mean. I can understand things like <i>Show me recent PG13-rated Action movies.</i>",
                        "@selectionType": "RANDOM"
                    },
                    (1, "goto"): {
                        "@ref": "##special_DNR_GET_USER_INPUT_NODE_ID"
                    }
                }
            }
        }
