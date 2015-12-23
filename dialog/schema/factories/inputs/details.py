from dialog.elements import Grammar, Prompt, Input, GetUserInput, Output
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class DetailsInput:
    @staticmethod
    def create():
        return Input(
            Grammar(
                watson_items=[
                    "Details",
                    "$ details",
                    "$ detail",
                    "$ movie info",
                    "$ movie information"
                ]
            ),
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                Output(
                    Prompt(
                        items=[
                            "After searching for movies, you can click on a particular movie result to see <i>details</i>, such as rating, summary and trailer.", ]
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
