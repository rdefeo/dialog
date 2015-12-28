from dialog.elements import Goto, Grammar, Input, Prompt, Output, If, GetUserInput
from dialog.schema.factories.action import PageAction
from dialog.schema.factories.conditions import ResultsCountConditions
from dialog.schema.factories.inputs import RemoveAllSearchCriteriaInput
from dialog.schema.factories.inputs.remove_color import RemoveColorInput
from dialog.schema.factories.inputs.remove_style import RemoveStyleInput

from dialog.schema.factories.outputs.anything_else_can_help_with import AnythingElseCanHelpWith
from dialog.schema.factories.search import PreliminarySequencesSearch
from dialog.schema.factories.variables import NAME_RESULTS_COUNT

__author__ = 'robdefeo'


class AfterSearchResults:
    @staticmethod
    def __id():
        return "getUserInput_after_search_results"

    @staticmethod
    def goto():
        return Goto(ref=AfterSearchResults.__id())

    @staticmethod
    def create():
        from dialog.schema.factories.inputs.main_search_criteria import AgainOption, MoreOption, GoBackOption

        return GetUserInput(
            _id=AfterSearchResults.__id(),
            children=[
                Input(
                    _id="input_2456878",
                    grammar=Grammar(
                        items=[
                            "Okay",
                            "okay",
                            "$ done"
                        ]
                    ),
                    children=[AnythingElseCanHelpWith.create()]
                ),
                Input(
                    Grammar(
                        items=[
                            "What do you mean",
                            "$ what do you mean",
                            "$ what does that mean",
                            "$ what did you mean",
                            "$ what were those movies again",
                            "$ what did you mean",
                            "$ what are those"
                        ]
                    ),
                    children=[
                        Output(
                            prompt=Prompt(
                                items=["These are the {Recency_Preference} movies. Go ahead and click one!"]
                            ),
                            children=[AfterSearchResults.goto()]
                        )
                    ]
                ),
                # TODO could be the details flow?
                # (2, "input"): {
                #     (0, "grammar"): {
                #         "item": [
                #             "When are those showing?",
                #             "$ when * showing",
                #             "$ when * playing",
                #             "$ when * play",
                #             "$ what times * showing",
                #             "$ what times * playing",
                #             "$ what times * play",
                #             "$ what * showtimes",
                #             "$ where * showing",
                #             "$ where * playing",
                #             "$ where * play"
                #         ]
                #     },
                #     (1, "output"): {
                #         "@id": "output_ask_search_for_movies_in_area",
                #         (0, "prompt"): {
                #             "item": "Oh. You mean movies in your area. I must direct you to Fandango for that. Would you like the link?",
                #             "@selectionType": "RANDOM"
                #         },
                #         (1, "getUserInput"): {
                #             (0, "input"): [
                #                 {
                #                     (0, "grammar"): GenericGrammar.yes(),
                #                     (1, "output"): {
                #                         (0, "prompt"): GenericPrompt.ok(),
                #                         (1, "goto"): Goto(ref="output_showtimes_zipcode")
                #                     }
                #                 },
                #                 {
                #                     (0, "grammar"): GenericGrammar.no(),
                #                     (1, "output"): {
                #                         (0, "prompt"): GenericPrompt.ok(),
                #                         (1, "goto"): AfterSearchResults.goto()
                #                     }
                #                 }
                #             ],
                #             (1, "goto"): AfterSearchResults.goto()
                #         }
                #     }
                # },
                # (3, "if"): {
                #     (0, "cond"): {
                #         "@varName": "Popularity_Score",
                #         "@operator": "HAS_VALUE"
                #     },
                #     (1, "input"): [
                #         {
                #             (0, "grammar"): {
                #                 "item": [
                #                     "What are the ratings?",
                #                     "$ ratings for it",
                #                     "$ ratings does it get",
                #                     "$ ratings it gets",
                #                     "$ ratings it got",
                #                     "$ ratings it received",
                #                     "$ its ratings",
                #                     "$ how many * stars",
                #                     "why",
                #                     "why not",
                #                     "why do you say that"
                #                 ]
                #             },
                #             (1, "output"): {
                #                 (0, "prompt"): {
                #                     "item": "{Selected_Movie} gets {Popularity_Score} stars from users.",
                #                     "@selectionType": "RANDOM"
                #                 },
                #                 (1, "getUserInput"): {
                #                     (0, "input"): {
                #                         (0, "grammar"): {
                #                             "item": [
                #                                 "okay",
                #                                 "okay",
                #                                 "$ sucks",
                #                                 "haha"
                #                             ]
                #                         },
                #                         (1, "goto"): AnythingElseCanHelpWith.goto()
                #                     },
                #                     (1, "goto"): {
                #                         "@ref": "input_2456878"
                #                     }
                #                 }
                #             }
                #         },
                #         {
                #             (0, "grammar"): Grammar(
                #                 watson_items=[
                #                     "What is it about?",
                #                     "$ what's is about?"
                #                 ]
                #             ),
                #             (1, "output"): Output(
                #                 Prompt(
                #                     items=["There should be a short description of {Selected_Movie} to the right."]
                #                 ),
                #                 children=[
                #                     GetUserInput(
                #                         children=[
                #                             Input(
                #                                 grammar=Grammar(
                #                                     watson_items=[
                #                                         "okay",
                #                                         "okay",
                #                                         "$ sucks",
                #                                         "haha"
                #                                     ]
                #                                 ),
                #                                 children=[AnythingElseCanHelpWith.goto()]
                #                             ),
                #                             Goto(ref="input_2456878")
                #                         ]
                #                     )
                #                 ]
                #             )
                #         }
                #     ],
                #     (2, "goto"): Goto(ref="input_2459410")
                # },
                Input(
                    _id="input_2459410",
                    grammar=Grammar(
                        watson_items=[
                            "Are those",
                            "$ are those",
                            "$ are these",
                            "$ is that",
                            "$ were those",
                            "$ were these",
                            "$ does this",
                            "$ do these",
                            "$ are they"
                        ]
                    ),
                    children=[
                        Input(
                            Grammar(
                                watson_items=[
                                    "What are",
                                    "$ what are",
                                    "$ what were"
                                ]
                            ),
                            children=[
                                PageAction.set_to_repeat(),
                                Goto(ref="output_search_now")
                            ]
                        ),
                        Input(
                            Grammar(
                                watson_items=[
                                    "all of them",
                                    "$ all",
                                    "$ it"
                                ]
                            ),
                            children=[Goto(ref="profileCheck_2459411")]
                        ),
                        If(
                            _id="profileCheck_2459411",
                            elements=[
                                ResultsCountConditions.less_than("{%s}" % NAME_RESULTS_COUNT),
                                Output(
                                    Prompt(
                                        items=["No. Say <i>show me more</i> if you want to see more."]
                                    ),
                                    children=[AfterSearchResults.goto()]
                                )
                            ]
                        ),
                        Output(
                            Prompt(
                                items=["Yes. I'm afraid that's all of them."]
                            ),
                            children=[AfterSearchResults.goto()]
                        )
                    ]
                ),
                RemoveColorInput.create(),
                RemoveStyleInput.create(),
                RemoveAllSearchCriteriaInput.create(),
                # (8, "input"): Showtimes.create(),
                # (9, "input"): RecencyGenreRatingPreference.create(),
                # (10, "input"): RecencyGenrePreference.create(),
                # (11, "input"): RecencyRatingPreference.create(),
                # (12, "input"): GenreRecencyPreference.create(),
                # (13, "input"): RecencyPreference.create(),
                # (15, "input"): CertificationPreference.create(),
                # (16, "input"): UnsupportedGenre.create(),
                # (17, "input"): DateTimePreference.create(),
                AgainOption.create(),
                MoreOption.create(),
                GoBackOption.create(),
                PreliminarySequencesSearch.goto()
            ]
        )
