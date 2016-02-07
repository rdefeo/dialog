from dialog.elements import Prompt, Grammar, Input, GetUserInput, Output
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class FavoritesInput:
    @staticmethod
    def create():
        return Input(
            Grammar(
                watson_items=[
                    "Favorites",
                    "$ favorites",
                    "$ favorite movies",
                    "$ favorited",
                    "$ hearted"
                ]
            ),
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                Output(
                    Prompt(
                        items=[
                            "When you get the details for a movie, you can save the movie in your <i>Favorites</i> by clicking on the heart icon above the trailer."]
                    ),
                    children=[
                        GetUserInput(
                            children=[
                                Input(
                                    GenericGrammar.ok(),
                                    children=[HowCanHelpYouOutput.goto()]
                                ),
                                PreliminarySequencesSearch.goto()
                            ]
                        )
                    ]
                )
            ]
        )
