from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar

__author__ = 'robdefeo'


class DetailsInput:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "Details",
                    "$ details",
                    "$ detail",
                    "$ movie info",
                    "$ movie information"
                ]
            },
            (1, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.create_reset()
            ],
            (2, "output"): {
                (0, "prompt"): {
                    "item": "After searching for movies, you can click on a particular movie result to see <i>details</i>, such as rating, summary and trailer.",
                    "@selectionType": "RANDOM"
                },
                (1, "getUserInput"): {
                    (0, "input"): {
                        (0, "grammar"): GenericGrammar.create_ok(),
                        (1, "goto"): Goto(ref="output_how_can_i_help_you")
                    },
                    (1, "goto"): Goto(ref="search_preliminary_sequences")
                }
            }
        }
