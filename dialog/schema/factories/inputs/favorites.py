from dialog.schema.elements import Goto, Prompt
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.search import PreliminarySequencesSearch

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
                SmallTalkAction.set_to_zero()
            ],
            (2, "output"): {
                (0, "prompt"): Prompt(
                    items=[
                        "When you get the details for a movie, you can save the movie in your <i>Favorites</i> by clicking on the heart icon above the trailer."]
                ),
                (1, "getUserInput"): {
                    (0, "input"): {
                        (0, "grammar"): GenericGrammar.ok(),
                        (1, "goto"): HowCanHelpYouOutput.goto()
                    },
                    (1, "goto"): PreliminarySequencesSearch.goto()
                }
            }
        }
