from dialog.elements import Prompt, Output, Grammar, Condition, If, Input, Folder
from dialog.schema.factories.inputs import AfterSearchResults


class UIActionsSequences:
    @staticmethod
    def create():
        return Folder(
            label="UI ACTIONS",
            children=[
                Input(
                    Grammar(watson_items=["USER CLICKS BOX"]),
                    children=[
                        Output(
                            prompt=Prompt(
                                items=["{Selected_Movie}."]
                            ),
                            children=[
                                If(
                                    elements=[
                                        Condition(name="Popularity_Score", operator="GREATER_THEN", root_text="6.9"),
                                        Output(
                                            Prompt(
                                                items=[
                                                    "Great choice! That gets fabulous ratings.",
                                                    "That's a good one! You will love it.",
                                                    " I hear that's a really good movie!"
                                                ]
                                            ),
                                            children=[AfterSearchResults.goto()]
                                        )
                                    ]
                                ),
                                If(
                                    elements=[
                                        Condition(name="Popularity_Score", operator="LESS_THEN", root_text="4"),
                                        Output(
                                            Prompt(
                                                items=[
                                                    "Hmm, I hear that's not such a great movie.",
                                                    "Um, that one gets low ratings.",
                                                    "Are you sure about that? The ratings are terrible."
                                                ]
                                            ),
                                            children=[AfterSearchResults.goto()]
                                        )

                                    ]
                                ),
                                Output(
                                    prompt=Prompt(
                                        items=[
                                            "Okay.",
                                            "All right.",
                                            "Sure thing!",
                                            "Coming right up!"
                                        ]
                                    ),
                                    children=[AfterSearchResults.goto()]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
