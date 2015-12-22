from dialog.elements import Action, Goto, Prompt, Output, Input, GetUserInput, Grammar, Folder
from dialog.schema.factories.action import TerminalExchangeAction, GreetingAction, SmallTalkAction, \
    CertificationPreferenceAction, StylePreferenceAction, \
    ColorPreferenceAction, PageAction, RequestSuccessAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.outputs import HowCanHelpYouOutput
from dialog.schema.factories.profile_checks.style_preference import StylePreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.search import PreliminarySequencesSearch


class SystemInitiatedSequences:
    @staticmethod
    def __id():
        return "output_help_with_anything_else"

    @staticmethod
    def goto():
        return Goto(ref=SystemInitiatedSequences.__id())

    @staticmethod
    def create():
        # Folder
        return Folder(
                label="SYSTEM INITIATED SEQUENCES",
                children=[
                    Output(
                            _id=SystemInitiatedSequences.__id(),
                            prompt=Prompt(
                                    items=["Is there anything else I can help you with?"]
                            ),
                            children=[
                                PageAction.set_to_new(),
                                Action(var_name="Current_Index", operator="SET_TO", text="0"),
                                CertificationPreferenceAction.set_to_blank(),
                                ColorPreferenceAction.set_to_blank(),
                                # RecencyPreferenceAction.set_to_blank(),
                                StylePreferenceAction.set_to_blank(),
                                Action(var_name="Search_Now", operator="SET_TO_NO"),
                                Action(var_name="Terminal_Exchange", operator="SET_TO_BLANK"),
                                Action(var_name="Topic", operator="SET_TO_BLANK"),
                                Action(var_name="ZIP_Code_Preference", operator="SET_TO_BLANK"),
                                Action(var_name="Display_Trailer", operator="SET_TO_NO"),
                                Action(var_name="Selected_Movie", operator="SET_TO_BLANK"),
                                Action(var_name="Display_Movie_Details", operator="SET_TO_NO"),
                                Action(var_name="Display_Reviews", operator="SET_TO_NO"),
                                Action(var_name="Popularity_Score", operator="SET_TO", text="0.5"),
                                GetUserInput(
                                        children=[
                                            Input(
                                                    GenericGrammar.yes(),
                                                    children=[HowCanHelpYouOutput.goto()]
                                            ),
                                            Input(
                                                    GenericGrammar.no(),
                                                    children=[
                                                        Output(
                                                                prompt=GenericPrompt.ok(),
                                                                children=[Goto(ref="output_did_find_what_looking_for")]
                                                        )
                                                    ]
                                            ),
                                            PreliminarySequencesSearch.goto()
                                        ]
                                )
                            ]
                    ),
                    Output(
                            _id="output_did_find_what_looking_for",
                            prompt=Prompt(
                                    items=["Did you find what you were looking for, {User_Name}?"]
                            ),
                            children=[
                                GetUserInput(
                                        children=[
                                            Input(
                                                    GenericGrammar().yes(),
                                                    children=[
                                                        RequestSuccessAction.set_to_yes(),
                                                        Output(
                                                                prompt=Prompt(
                                                                        items=["Great!"]
                                                                ),
                                                                children=[
                                                                    Output(
                                                                            _id="output_goodbye",
                                                                            prompt=Prompt(
                                                                                    items=["Goodbye.<br> <br>"]
                                                                            ),
                                                                            children=[
                                                                                TerminalExchangeAction.set_to_yes(),
                                                                                GreetingAction.reset(),
                                                                                GetUserInput(
                                                                                        children=[
                                                                                            Input(
                                                                                                    Grammar(
                                                                                                            watson_items=[
                                                                                                                "Goodbye",
                                                                                                                "$ goodbye"
                                                                                                            ]
                                                                                                    ),
                                                                                                    children=[
                                                                                                        Output(
                                                                                                                _id="output_end_of_conversation",
                                                                                                                prompt=Prompt(
                                                                                                                        items="&lt;i&gt;Say anything to continue.&lt;/i&gt;"
                                                                                                                ),
                                                                                                                children=[
                                                                                                                    GetUserInput(
                                                                                                                            children=[
                                                                                                                                Output(
                                                                                                                                        _id="output_welcome_back",
                                                                                                                                        prompt=Prompt(
                                                                                                                                                items=[
                                                                                                                                                    "Welcome back!"]
                                                                                                                                        ),
                                                                                                                                        children=[HowCanHelpYouOutput.goto()]
                                                                                                                                )
                                                                                                                            ]
                                                                                                                    )
                                                                                                                ]
                                                                                                        ),

                                                                                                    ]
                                                                                            ),
                                                                                            HowCanHelpYouOutput.goto()
                                                                                        ]
                                                                                )
                                                                            ]
                                                                    )
                                                                ]
                                                        )
                                                    ]
                                            ),
                                            Input(
                                                    GenericGrammar.no(),
                                                    children=[
                                                        RequestSuccessAction.set_to_no(),
                                                        Output(
                                                                prompt=Prompt(
                                                                        items=["Oh no. Do you want to try again?"]
                                                                ),
                                                                children=[
                                                                    GetUserInput(
                                                                            children=[
                                                                                Input(
                                                                                        GenericGrammar.no(),
                                                                                        children=[
                                                                                            TerminalExchangeAction.set_to_no(),
                                                                                            Output(
                                                                                                    prompt=GenericPrompt.ok(),
                                                                                                    children=[Goto(
                                                                                                            ref="output_goodbye")]
                                                                                            )
                                                                                        ]
                                                                                ),
                                                                                Input(
                                                                                        GenericGrammar.yes(),
                                                                                        children=[
                                                                                            Output(
                                                                                                    prompt=Prompt(
                                                                                                            items=[
                                                                                                                "Okay. What can I do for you?"]
                                                                                                    ),
                                                                                                    children=[
                                                                                                        Goto(
                                                                                                                "getUserInput_how_can_i_help_you")
                                                                                                    ]
                                                                                            )
                                                                                        ]
                                                                                )
                                                                            ]
                                                                    )
                                                                ]
                                                        )
                                                    ]
                                            ),
                                            PreliminarySequencesSearch.goto()
                                        ]
                                )
                            ]
                    ),
                    Output(
                            _id="output_too_much_small_talk",
                            prompt=Prompt(
                                    items=["This is fun, but wouldn't you like to look up some movies?"]
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
                                                        SmallTalkAction.set_to_zero(),
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
        )
