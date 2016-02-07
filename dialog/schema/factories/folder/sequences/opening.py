from dialog.elements import Condition, If, Goto, Prompt, Output, GetUserInput, Input, Grammar, Folder
from dialog.schema.factories.action import GreetingAction
from dialog.schema.factories.grammar import GenericGrammar, FeelingGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.profile_checks.style_preference import StylePreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch
from dialog.schema.factories.variables import NAME_GREETING_COUNT, NAME_SMALL_TALK_COUNT, NAME_TERMINAL_EXCHANGE


class OpeningSequences:
    @staticmethod
    def create():
        return Folder(
                selection_type="RANDOM",
                label="OPENING SEQUENCES",
                children=[
                    Input(
                            GenericGrammar.create_hello(),
                            children=[
                                GreetingAction.create_increment(),
                                If(
                                        elements=[
                                            Condition(name=NAME_TERMINAL_EXCHANGE, operator="EQUAL_TO_YES"),
                                            Goto(ref="output_welcome_back")
                                        ]
                                ),
                                If(
                                        match_type="ANY",
                                        elements=[
                                            Condition(name=NAME_GREETING_COUNT, operator="GREATER_THEN", root_text="2"),
                                            Condition(name=NAME_SMALL_TALK_COUNT, operator="GREATER_THEN",
                                                      root_text="2"),
                                            Goto(ref="output_end_of_small_talk")
                                        ]
                                ),
                                Output(
                                        Prompt(
                                                items=[
                                                    "Hello.",
                                                    "Hi.",
                                                    "Hi there."
                                                ]
                                        ),
                                        children=[Output(
                                                _id="output_how_are_you",
                                                prompt=Prompt(
                                                        items=[
                                                            "How are you today?",
                                                            "How are you feeling today?",
                                                            "How is it going?"
                                                        ]
                                                ),
                                                children=[GetUserInput(
                                                        children=[
                                                            Input(
                                                                    Grammar(
                                                                            watson_items=[
                                                                                "Movies",
                                                                                "$ (STYLE)={Style_Preference}",
                                                                                "$ (COLOR)={Color_Preference}",
                                                                                "$ movies"
                                                                            ]
                                                                    ),
                                                                    children=[
                                                                        Goto(ref="input_main_search_criteria")
                                                                    ]
                                                            ),
                                                            Input(
                                                                    FeelingGrammar.create_not_so_good(),
                                                                    children=[
                                                                        Goto(ref="output_sorry_to_hear_that")
                                                                    ]
                                                            ),
                                                            Input(
                                                                    FeelingGrammar.create_not_so_bad(),
                                                                    children=[
                                                                        Goto(ref="output_good_to_hear")
                                                                    ]
                                                            ),
                                                            Input(
                                                                    FeelingGrammar.create_feeling_fine(),
                                                                    children=[
                                                                        Output(
                                                                                _id="output_good_to_hear",
                                                                                prompt=Prompt(
                                                                                        items=[
                                                                                            "Good to hear! <br> <br>"]
                                                                                ),
                                                                                children=[HowCanHelpYouOutput.goto()]
                                                                        )
                                                                    ]
                                                            ),
                                                            Input(
                                                                    FeelingGrammar.create_feeling_great(),
                                                                    children=[
                                                                        Output(
                                                                                Prompt(
                                                                                        items=[
                                                                                            "Fantastic! So glad to hear it. <br> <br>"]
                                                                                ),
                                                                                children=[HowCanHelpYouOutput.goto()]
                                                                        )
                                                                    ]
                                                            ),
                                                            Input(
                                                                    FeelingGrammar.create_feeling_bad(),
                                                                    children=[
                                                                        Output(
                                                                                _id="output_sorry_to_hear_that",
                                                                                prompt=Prompt(
                                                                                        items=[
                                                                                            "I'm sorry to hear that. <br> <br>"]
                                                                                ),
                                                                                children=[HowCanHelpYouOutput.goto()]
                                                                        )
                                                                    ]
                                                            ),
                                                            PreliminarySequencesSearch.goto()
                                                        ]
                                                )
                                                ]
                                        )]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    watson_items=[
                                        "How are you",
                                        "$ how have you been doing",
                                        "$ how is it going",
                                        "$ how are you",
                                        "$ what's shaking",
                                        "$ what's up"
                                    ]
                            ),
                            children=[
                                GreetingAction.create_increment(),
                                If(
                                        elements=[
                                            Condition(name=NAME_GREETING_COUNT, operator="GREATER_THEN", root_text="2"),
                                            Condition(name=NAME_SMALL_TALK_COUNT, operator="GREATER_THEN",
                                                      root_text="2"),
                                            Output(
                                                    _id="output_end_of_small_talk",
                                                    prompt=Prompt(
                                                            items=[
                                                                "You're very polite, but don't you want me to look up movies for you?"]
                                                    ),
                                                    children=[GetUserInput(
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
                                                                            GreetingAction.reset(),
                                                                            Output(
                                                                                    GenericPrompt.ok_fine()
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
                                                    "Fine",
                                                    "$ excellent",
                                                    "$ outstanding",
                                                    "$ fabulous",
                                                    "$ terrific",
                                                    "$ not good",
                                                    "$ not so good",
                                                    "$ not well",
                                                    "$ not so well",
                                                    "$ terrible",
                                                    "$ awful",
                                                    "$ worst",
                                                    "$ bored",
                                                    "$ sad",
                                                    "$ good",
                                                    "$ well",
                                                    "$ fine",
                                                    "$ thirsty",
                                                    "$ hungry",
                                                    "$ tired"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(items=["I am doing well, thanks."]),
                                                    children=[HowCanHelpYouOutput.goto()]
                                            )
                                        ]
                                ),
                                Output(
                                        Prompt(items=["I am doing well, thanks."]),
                                        children=[Goto(ref="output_how_are_you")]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    watson_items=[
                                        "Nice to meet you",
                                        "$ nice to meet you",
                                        "$ pleasure to meet you",
                                        "$ make your acquaintance"
                                    ]
                            ),
                            children=[
                                If(
                                        elements=[
                                            Condition(name="Greeting_Count", operator="GREATER_THEN", root_text="2"),
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "You're very polite, but don't you want me to look up movies for you?"]
                                                    ),
                                                    children=[GetUserInput(
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
                                                                            GreetingAction.reset(),
                                                                            Output(
                                                                                    GenericPrompt.ok_fine()
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
                                Output(
                                        Prompt(items=["Nice to meet you too, {User_Name}!"]),
                                        children=[HowCanHelpYouOutput.goto()]
                                )
                            ]
                    )
                ]
        )
