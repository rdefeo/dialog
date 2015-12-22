from dialog.elements import Output, Prompt, Grammar, Input, GetUserInput, Folder
from dialog.schema.factories.action import StylePreferenceAction, ColorPreferenceAction, UserNameAction, TopicAction
from dialog.schema.factories.grammar import FeelingGrammar, ProfileGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.outputs.start_search import StartSearch
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch


class MainFolder:
    @staticmethod
    def create():
        return Folder(
            label="Main",
            children=[
                Output(
                    prompt=GenericPrompt.what_is_your_name(),
                    children=[
                        GetUserInput(
                            children=[
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "Movies",
                                            "$ (Color)={Color_Preference}",
                                            "$ (Style)={Style_Preference}",
                                            "$ movies",
                                            "$ want to see something",
                                            "$ planning to go see",
                                            "$ planning to go to the",
                                            "$ going out to see",
                                            "$ planning to see",
                                            "$ want to go see",
                                            "$ thinking of seeing",
                                            "$ thinking we want to see",
                                            "$ what do you recommend",
                                            "$ can you recommend something",
                                            "$ what are your recommendations"
                                        ]
                                    ),
                                    children=[
                                        ColorPreferenceAction.set_to_value(),
                                        # CertificationPreferenceAction.set_to_value(),
                                        StylePreferenceAction.set_to_value(),
                                        TopicAction.set_to_shoes(),
                                        PreliminarySequencesSearch.goto()
                                    ]
                                ),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "Movie-related",
                                            "$ (OTHER_MOVIE)={Topic}",
                                            "$ (BY_OTHER_MOVIE)={Topic}",
                                            "$ showtimes",
                                            "$ theaters",
                                            "$ fandango",
                                            "$ reviews",
                                            "$ review",
                                            "$ critiques",
                                            "$ critique",
                                            "$ old movies",
                                            "$ classic movies",
                                            "$ oldies",
                                            "$ classics",
                                            "$ trailers",
                                            "$ reviews",
                                            "$ (DINING)={Topic}",
                                            "$ (WEATHER)={Topic}",
                                            "$ (TRAFFIC)={Topic}"
                                        ]
                                    ),
                                    children=[PreliminarySequencesSearch.goto()]
                                ),
                                Input(
                                    grammar=FeelingGrammar.create_preliminaries(),
                                    children=[

                                        PreliminarySequencesSearch.goto()
                                    ]
                                ),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "Why do you need to know?",
                                            "$ why",
                                            "$ need to know",
                                            "$ use it",
                                            "$ do with it"
                                        ]
                                    ),
                                    children=[
                                        Output(
                                            prompt=Prompt(
                                                items=["Just trying to be friendly."]
                                            ),
                                            children=[StartSearch.goto()]
                                        )
                                    ]
                                ),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "I don't want to give it!",
                                            "$ don't want",
                                            "$ no",
                                            "$ refuse",
                                            "$ none of your business"
                                        ]
                                    ),
                                    children=[
                                        Output(
                                            Prompt(items=["That's fine."]),
                                            children=[StartSearch.goto()]
                                        )
                                    ]
                                ),
                                Input(
                                    ProfileGrammar.create_my_name_is_dynamic_data(),
                                    children=[
                                        UserNameAction.set_to_source(),
                                        Output(
                                            prompt=Prompt(items=["Hi {User_Name}!"]),
                                            children=[StartSearch.goto()]
                                        )
                                    ],
                                    _id="input_user_knownas_name"
                                )
                            ],
                            _id="getUserInput_what_is_your_name"
                        ),
                        StartSearch.create(),
                        HowCanHelpYouOutput.create()
                    ],
                    _id="output_what_is_name"
                )
            ]
        )
