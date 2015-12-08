from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar

__author__ = 'robdefeo'


class FavoritesInput:
    @staticmethod
    def create():
        return {
            (0, "grammar"): {
                "item": [
                    "Favorites",
                    "$ favorites",
                    "$ favorite movies",
                    "$ favorited",
                    "$ hearted"
                ]
            },
            (1, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.create_reset()
            ],
            (2, "output"): {
                (0, "prompt"): {
                    "item": "When you get the details for a movie, you can save the movie in your <i>Favorites</i> by clicking on the heart icon above the trailer.",
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
