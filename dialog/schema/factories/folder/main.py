from dialog.schema.elements import Goto
from dialog.schema.factories.action import StylePreferenceAction, ColorPreferenceAction
from dialog.schema.factories.grammar import FeelingGrammar, ProfileGrammar, GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.outputs.start_search import StartSearch
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch


class MainFolder:
    @staticmethod
    def create():
        return {
            "@label": "Main",
            (0, "output"): {
                "@id": "output_what_is_name",
                (0, "prompt"): GenericPrompt.what_is_your_name(),
                (1, "getUserInput"): {
                    "@id": "getUserInput_what_is_your_name",
                    "input": [
                        {
                            (0, "grammar"): {
                                "item": [
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
                            },
                            (1, "action"): [
                                ColorPreferenceAction.set_to_value(),
                                # CertificationPreferenceAction.set_to_value(),
                                StylePreferenceAction.set_to_value(),
                                {
                                    "@varName": "Topic",
                                    "@operator": "SET_TO",
                                    "#text": "movies"
                                }
                            ],
                            (2, "goto"): PreliminarySequencesSearch.goto()
                        },
                        {
                            (0, "grammar"): {
                                "item": [
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
                            },
                            (1, "goto"): PreliminarySequencesSearch.goto()
                        },
                        {
                            (0, "grammar"): FeelingGrammar.create_preliminaries(),
                            (1, "goto"): PreliminarySequencesSearch.goto()
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "Why do you need to know?",
                                    "$ why",
                                    "$ need to know",
                                    "$ use it",
                                    "$ do with it"
                                ]
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "Just trying to be friendly.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): StartSearch.goto()
                            }
                        },
                        {
                            (0, "grammar"): {
                                "item": [
                                    "I don't want to give it!",
                                    "$ don't want",
                                    "$ no",
                                    "$ refuse",
                                    "$ none of your business"
                                ]
                            },
                            (1, "output"): {
                                (0, "prompt"): {
                                    "item": "That's fine.",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): StartSearch.goto()
                            }
                        },
                        {
                            "@id": "input_user_knownas_name",
                            (0, "grammar"): ProfileGrammar.create_my_name_is_dynamic_data(),
                            (1, "action"): {
                                "@varName": "User_Name",
                                "@operator": "SET_TO",
                                "#text": "{User_Name.source}"
                            },
                            (2, "output"): {
                                (0, "prompt"): {
                                    "item": "Hi {User_Name}!",
                                    "@selectionType": "RANDOM"
                                },
                                (1, "goto"): StartSearch.goto()
                            }
                        }
                    ]
                },
                (2, "output"): [
                    StartSearch.create(),
                    HowCanHelpYouOutput.create()
                ]
            }
        }
