from dialog.schema.elements import Goto

__author__ = 'robdefeo'


class HowCanHelpYou:
    @staticmethod
    def goto():
        return Goto(ref=HowCanHelpYou.id())

    @staticmethod
    def id():
        return "output_how_can_i_help_you"

    @staticmethod
    def create():
        return {
            "@id": HowCanHelpYou.id(),
            (0, "prompt"): {
                "item": [
                    "How can I help you?",
                    "What can I do for you?"
                ],
                "@selectionType": "RANDOM"
            },
            (1, "getUserInput"): {
                "@id": "getUserInput_2414745",
                (0, "search"): [
                    {
                        "@id": "search_preliminary_sequences",
                        "@ref": "folder_preliminary_sequences"
                    },
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
        }
