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
                    children=[
                        GenericGrammar.create_hello(),
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
                                Condition(name=NAME_SMALL_TALK_COUNT, operator="GREATER_THEN", root_text="2"),
                                Goto(ref="output_end_of_small_talk")
                            ]
                        ),
                        Output(
                            children=[
                                Prompt(
                                    items=[
                                        "Hello.",
                                        "Hi.",
                                        "Hi there."
                                    ]
                                ),
                                Output(
                                    _id="output_how_are_you",
                                    children=[
                                        Prompt(
                                            items=[
                                                "How are you today?",
                                                "How are you feeling today?",
                                                "How is it going?"
                                            ]
                                        ),
                                        GetUserInput(
                                            children=[
                                                Input(
                                                    children=[
                                                        Grammar(
                                                            items=[
                                                                "Movies",
                                                                "$ (STYLE)={Style_Preference}",
                                                                "$ (COLOR)={Color_Preference}",
                                                                "$ movies"
                                                            ]
                                                        ),
                                                        Goto(ref="input_main_search_criteria")
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        FeelingGrammar.create_not_so_good(),
                                                        Goto(ref="output_sorry_to_hear_that")
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        FeelingGrammar.create_not_so_bad(),
                                                        Goto(ref="output_good_to_hear")
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        FeelingGrammar.create_feeling_fine(),
                                                        Output(
                                                            _id="output_good_to_hear",
                                                            children=[
                                                                Prompt(
                                                                    items=["Good to hear! <br> <br>"]
                                                                ),
                                                                HowCanHelpYouOutput.goto()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        FeelingGrammar.create_feeling_great(),
                                                        Output(
                                                            children=[
                                                                Prompt(
                                                                    items=["Fantastic! So glad to hear it. <br> <br>"]
                                                                ),
                                                                HowCanHelpYouOutput.goto()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        FeelingGrammar.create_feeling_bad(),
                                                        Output(
                                                            _id="output_sorry_to_hear_that",
                                                            children=[
                                                                Prompt(
                                                                    items=["I'm sorry to hear that. <br> <br>"]
                                                                ),
                                                                HowCanHelpYouOutput.goto()
                                                            ]
                                                        )
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
                    children=[
                        Grammar(
                            items=[
                                "How are you",
                                "$ how have you been doing",
                                "$ how is it going",
                                "$ how are you",
                                "$ what's shaking",
                                "$ what's up"
                            ]
                        ),
                        GreetingAction.create_increment(),
                        If(
                            elements=[
                                Condition(name=NAME_GREETING_COUNT, operator="GREATER_THEN", root_text="2"),
                                Condition(name=NAME_SMALL_TALK_COUNT, operator="GREATER_THEN", root_text="2"),
                                Output(
                                    _id="output_end_of_small_talk",
                                    children=[
                                        Prompt(
                                            items=[
                                                "You're very polite, but don't you want me to look up movies for you?"]
                                        ),
                                        GetUserInput(
                                            children=[
                                                Input(
                                                    children=[
                                                        GenericGrammar.yes(),
                                                        StylePreferenceProfileCheck.goto()
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        GenericGrammar.no(),
                                                        GreetingAction.reset(),
                                                        Output(
                                                            children=[
                                                                GenericPrompt.ok_fine()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        GenericGrammar.ok(),
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
                            children=[
                                Grammar(
                                    items=[
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
                                ), Output(
                                    children=[
                                        Prompt(items=["I am doing well, thanks."]),
                                        HowCanHelpYouOutput.goto()
                                    ]
                                )
                            ]
                        ),
                        Output(
                            children=[
                                Prompt(items=["I am doing well, thanks."]),
                                Goto(ref="output_how_are_you")
                            ]
                        )
                    ]
                ),
                Input(
                    children=[
                        Grammar(
                            items=[
                                "Nice to meet you",
                                "$ nice to meet you",
                                "$ pleasure to meet you",
                                "$ make your acquaintance"
                            ]
                        ),
                        If(
                            elements=[
                                Condition(name="Greeting_Count", operator="GREATER_THEN", root_text="2"),
                                Output(
                                    children=[
                                        Prompt(
                                            items=[
                                                "You're very polite, but don't you want me to look up movies for you?"]
                                        ),
                                        GetUserInput(
                                            children=[
                                                Input(
                                                    children=[
                                                        GenericGrammar.yes(),
                                                        StylePreferenceProfileCheck.goto()
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        GenericGrammar.no(),
                                                        GreetingAction.reset(),
                                                        Output(
                                                            children=[
                                                                GenericPrompt.ok_fine()
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                Input(
                                                    children=[
                                                        GenericGrammar.ok(),
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
                            children=[
                                Prompt(items=["Nice to meet you too, {User_Name}!"]),
                                HowCanHelpYouOutput.goto()
                            ]
                        )
                    ]
                )
            ]
        )
