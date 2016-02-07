from dialog.elements import Grammar, Goto, Input, Prompt, GetUserInput, Output, Action, If, Folder
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, StylePreferenceAction, TopicAction, \
    OutOfScopeCountAction
from dialog.schema.factories.conditions.user_conditions import OutOfScopeCountConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.profile_checks.style_preference import StylePreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class PreliminarySequencesFolder:
    @staticmethod
    def _id():
        return "folder_preliminary_sequences"

    @staticmethod
    def create():
        return Folder(
            label="PRELIMINARY SEQUENCES",
            _id=PreliminarySequencesFolder._id(),
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                Input(
                    Grammar(
                        watson_items=[
                            "Do you know",
                            "$ do you know",
                            "$ can you",
                            "$ do you have information",
                            "$ can I",
                            "$ can you tell",
                            "$ what kind of",
                            "$ what else do you know"
                        ]
                    ),
                    children=[
                        GreetingAction.reset(),
                        SmallTalkAction.set_to_zero(),
                        Input(
                            Grammar(
                                watson_items=[
                                    "out-of-scope movie topics",
                                    "$ (OTHER_MOVIE)={Topic}"
                                ]
                            ),
                            children=[
                                TopicAction.set_to_value(),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    children=[Goto(ref="output_no_topic_lookup")]
                                ),
                                Output(
                                    Prompt(items=["No."]),
                                    children=[
                                        Output(
                                            _id="output_no_topic_lookup",
                                            prompt=Prompt(
                                                items=[
                                                    "I'm afraid I can't look up movies by {Topic}, only by Genre or MPAA Rating."]
                                            ),
                                            children=[
                                                GetUserInput(
                                                    children=[
                                                        Input(
                                                            GenericGrammar.ok(),
                                                            children=[
                                                                HowCanHelpYouOutput.goto()
                                                            ]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        Input(
                            Grammar(
                                watson_items=[
                                    "by out-of-scope movie topics",
                                    "$ (BY_OTHER_MOVIE)={Topic}"
                                ]
                            ),
                            children=[
                                TopicAction.set_to_value(),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    children=[Goto(ref="output_2503370")]
                                ),
                                Output(
                                    Prompt(
                                        items=["No."]
                                    ),
                                    children=[
                                        Output(
                                            _id="output_2503370",
                                            prompt=Prompt(
                                                items=[
                                                    "I'm afraid I can't look up {Topic}, only Current and Upcoming movies by Genre or MPAA Rating.", ]
                                            ),
                                            children=[
                                                GetUserInput(
                                                    children=[
                                                        Input(
                                                            Grammar(watson_items=["Okay."]),
                                                            children=[HowCanHelpYouOutput.goto()]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        Input(
                            Grammar(
                                watson_items=[
                                    "unsupported genres",
                                    "$ (UNSUPPORTED_GENRES)={Topic}"
                                ]
                            ),
                            children=[
                                TopicAction.set_to_value(),
                                Input(
                                    grammar=Grammar(
                                        watson_items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    children=[Goto(ref="output_2510164")]
                                ),
                                Output(
                                    Prompt(items=["No."]),
                                    children=[
                                        Output(
                                            _id="output_2510164",
                                            prompt=Prompt(
                                                items=[
                                                    "I'm afraid {Topic} isn't a movie genre I know. Please try another one."]
                                            ),
                                            children=[
                                                GetUserInput(
                                                    children=[
                                                        Input(
                                                            grammar=Grammar(
                                                                watson_items=["Okay."]
                                                            ),
                                                            children=[HowCanHelpYouOutput.goto()]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        # {
                        #     (0, "grammar"): {
                        #         "item": [
                        #             "theaters",
                        #             "$ theaters",
                        #             "$ fandango"
                        #         ]
                        #     },
                        #     (1, "input"): {
                        #         (0, "grammar"): {
                        #             "item": [
                        #                 "what",
                        #                 "$ what"
                        #             ]
                        #         },
                        #         (1, "goto"): {
                        #             "@ref": "output_2503320"
                        #         }
                        #     },
                        #     (2, "output"): {
                        #         (0, "prompt"): {
                        #             "item": "No."
                        #         },
                        #         (1, "output"): {
                        #             "@id": "output_2503320",
                        #             (0, "prompt"): {
                        #                 "item": "I'm afraid I cannot look up theaters myself, but I can give you a link to Fandango.com where you can buy tickets in your ZIP code. ",
                        #                 "@selectionType": "RANDOM"
                        #             },
                        #             (1, "getUserInput"): {
                        #                 (0, "input"): {
                        #                     (0, "grammar"): GenericGrammar.ok(),
                        #                     (1, "goto"): HowCanHelpYouOutput.goto()
                        #                 },
                        #                 (1, "goto"): PreliminarySequencesSearch.goto()
                        #             }
                        #         }
                        #     }
                        # },
                        Input(
                            Grammar(
                                watson_items=["$ (STYLE)={Style_Preference}"]
                            ),
                            children=[
                                StylePreferenceAction.set_to_value(),
                                Goto(ref="search_2414740")
                            ]
                        ),
                        Input(
                            Grammar(
                                watson_items=[
                                    "genres",
                                    "$ genres"
                                ]
                            ),
                            children=[
                                Output(
                                    Prompt(
                                        items=[
                                            "Action, adventure, animated, comedy, crime, documentary, drama, family, fantasy, foreign, historical, horror, music, mystery, romance, science fiction, TV movie, thriller, war movies and western.  <br> <br>"]
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
                        ),
                        # {
                        #     (0, "grammar"): {
                        #         "item": [
                        #             "old movies",
                        #             "$ old movies",
                        #             "$ classic movies",
                        #             "$ oldies",
                        #             "$ classics"
                        #         ]
                        #     },
                        #     (1, "input"): {
                        #         (0, "grammar"): {
                        #             "item": [
                        #                 "what",
                        #                 "$ what"
                        #             ]
                        #         },
                        #         (1, "goto"): {
                        #             "@ref": "output_2503380"
                        #         }
                        #     },
                        #     (2, "output"): {
                        #         (0, "prompt"): {
                        #             "item": "No."
                        #         },
                        #         (1, "output"): {
                        #             "@id": "output_2503380",
                        #             (0, "prompt"): {
                        #                 "item": "I'm afraid I cannot look up Old Movies, only Current and Upcoming.",
                        #                 "@selectionType": "RANDOM"
                        #             },
                        #             (1, "getUserInput"): {
                        #                 (0, "input"): {
                        #                     (0, "grammar"): GenericGrammar.ok(),
                        #                     (1, "goto"): HowCanHelpYouOutput.goto()
                        #                 },
                        #                 (1, "goto"): PreliminarySequencesSearch.goto()
                        #             }
                        #         }
                        #     }
                        # },
                        Input(
                            Grammar(
                                watson_items=[
                                    "shoes",
                                    "$ shoes"
                                ]
                            ),
                            children=[
                                TopicAction.set_to_shoes(),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    children=[
                                        Goto(ref="output_what_jemboo_knows")
                                    ]
                                ),
                                Output(
                                    prompt=Prompt(
                                        items=["Yes."]
                                    ),
                                    children=[
                                        Output(
                                            _id="output_what_jemboo_knows",
                                            prompt=Prompt(
                                                items=[
                                                    "I can look up current and upcoming movies by Genre or MPAA Rating and show you trailers for them. But I'm afraid I cannot search by number of stars or by movie titles or actor and director names at this time.", ]
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
                            ]
                        ),
                        # {
                        #     (0, "grammar"): {
                        #         "item": [
                        #             "trailer",
                        #             "$ trailer",
                        #             "$ trailers"
                        #         ]
                        #     },
                        #     (1, "input"): {
                        #         (0, "grammar"): {
                        #             "item": [
                        #                 "what",
                        #                 "$ what"
                        #             ]
                        #         },
                        #         (1, "goto"): {
                        #             "@ref": "output_2510290"
                        #         }
                        #     },
                        #     (2, "output"): {
                        #         (0, "prompt"): {
                        #             "item": "Yes."
                        #         },
                        #         (1, "output"): {
                        #             "@id": "output_2510290",
                        #             (0, "prompt"): {
                        #                 "item": "After searching for movies, you can click on a particular movie result to watch its <i>trailer</i>, or video preview.",
                        #                 "@selectionType": "RANDOM"
                        #             },
                        #             (1, "getUserInput"): {
                        #                 (0, "input"): {
                        #                     (0, "grammar"): GenericGrammar.ok(),
                        #                     (1, "goto"): HowCanHelpYouOutput.goto()
                        #                 },
                        #                 (1, "goto"): PreliminarySequencesSearch.goto()
                        #             }
                        #         }
                        #     }
                        # },
                        Input(
                            Grammar(
                                watson_items=[
                                    "out-of-scope topics",
                                    "$ (DINING)={Topic}",
                                    "$ (WEATHER)={Topic}",
                                    "$ (TRAFFIC)={Topic}"
                                ]
                            ),
                            children=[
                                TopicAction.set_to_value(),
                                OutOfScopeCountAction.increment(),
                                If(
                                    elements=[
                                        OutOfScopeCountConditions.is_greater_then("2"),
                                        Output(
                                            Prompt(
                                                items=[
                                                    "I'm sorry I don't know about that. Can I look up some shoes for you?"]
                                            ),
                                            children=[
                                                GetUserInput(
                                                    children=[
                                                        Input(
                                                            GenericGrammar.yes(),
                                                            children=[
                                                                StylePreferenceProfileCheck.goto()
                                                            ]
                                                        ),
                                                        Input(
                                                            GenericGrammar.no(),
                                                            children=[
                                                                Action(var_name="Out-of-Scope_Count", operator="SET_TO",
                                                                       text="0"),
                                                                Output(
                                                                    prompt=GenericPrompt.ok_fine()
                                                                )
                                                            ]
                                                        ),
                                                        Input(
                                                            GenericGrammar.ok(),
                                                            children=[
                                                                StylePreferenceProfileCheck.goto()
                                                            ]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                Input(
                                    Grammar(
                                        watson_items=[
                                            "what",
                                            "$ what"
                                        ]
                                    ),
                                    children=[Goto(ref="output_2497989")]
                                ),
                                Output(
                                    Prompt(items=["No."]),
                                    children=[

                                        Output(
                                            _id="output_2497989",
                                            prompt=Prompt(
                                                items=["I'm afraid I don't know much about {Topic}. Just movies."]),
                                            children=[
                                                GetUserInput(
                                                    children=[
                                                        Input(
                                                            Grammar(watson_items=["Okay."]),
                                                            children=[HowCanHelpYouOutput.goto()]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        Goto(ref="output_what_jemboo_knows")
                    ]
                )
            ]
        )
