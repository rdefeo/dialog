from dialog.elements import Goto, Grammar, Input, Prompt, GetUserInput, Output, If, Action, Condition
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, \
    StylePreferenceAction, ColorPreferenceAction, PageAction, CurrentIndexAction, \
    TopicAction
from dialog.schema.factories.conditions import ColorConditions, StyleConditions
# from dialog.schema.factories.conditions.certification import CertificationsConditions
from dialog.schema.factories.conditions.results_count import ResultsCountConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs.remove_color import RemoveColorInput
from dialog.schema.factories.inputs.after_search_results import AfterSearchResults
from dialog.schema.factories.inputs.color import ColorPreferenceInput
from dialog.schema.factories.inputs.style import StylePreferenceInput
from dialog.schema.factories.profile_checks import StylePreferenceProfileCheck, ColorPreferenceProfileCheck
from dialog.schema.factories.prompts.generic import GenericPrompt
from dialog.schema.factories.variables import NAME_RESULTS_COUNT


class MainSearchCriteriaInput:
    @staticmethod
    def create():
        return Input(
            _id="input_main_search_criteria",
            grammar=Grammar(
                watson_items=[
                    "Movies",
                    "$ (COLOR)={Color_Preference}",
                    "$ (STYLE)={Style_Preference}",
                    # "$ movies"
                ]
            ),
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                CurrentIndexAction.set_to_zero(),
                PageAction.set_to_new(),
                TopicAction.set_to_shoes(),
                ColorPreferenceAction.set_to_value(),
                StylePreferenceAction.set_to_value(),
                # DateTimeInput.create(),
                # CertificationPreferenceInput.create(),
                # FamilyFriendlyInput.create(),
                ColorPreferenceInput.create(StylePreferenceInput.goto()),
                StylePreferenceInput.create(Goto(ref="out_of_scope_topics")),
                # ZipcodeInput.create(),
                Input(
                    _id="out_of_scope_topics",
                    grammar=Grammar(
                        watson_items=[
                            "out-of-scope movie topics",
                            "$ (OTHER_MOVIE)={Topic}"
                        ]
                    ),
                    children=[
                        TopicAction.set_to_value(),
                        Goto(ref="output_no_topic_lookup")
                    ]
                ),
                StylePreferenceProfileCheck.create(),
                # GenrePreferenceProfileCheck.create(),
                ColorPreferenceProfileCheck.create(),
                Output(
                    _id="output_ok_do_search",
                    prompt=GenericPrompt.ok(),
                    children=[
                        Output(
                            _id="output_search_now",
                            prompt=Prompt(
                                items=["Search_Now"]
                            ),
                            children=[
                                Action(var_name="Last_Results", operator="SET_TO_NO"),
                                Action(var_name="First_Results", operator="SET_TO_NO"),
                                Action(var_name="Search_Now", operator="SET_TO_YES"),
                                Action(var_name="First_Time", operator="SET_TO_NO"),
                                Input(
                                    Grammar(
                                        watson_items=["UPDATE NUM_MOVIES"]
                                    ),
                                    children=[
                                        If(
                                            elements=[
                                                ResultsCountConditions.equals_zero(),
                                                Output(
                                                    Prompt(
                                                        items=[
                                                            "I'm afraid I found {%s} matching {Color_Preference} {Style_Preference}. Try changing your criteria." % NAME_RESULTS_COUNT]
                                                    ),
                                                    children=[
                                                        GetUserInput(
                                                            children=[
                                                                Input(
                                                                    GenericGrammar.ok(),
                                                                    children=[
                                                                        ColorPreferenceAction.set_to_blank(),
                                                                        StylePreferenceAction.set_to_blank(),
                                                                        StylePreferenceProfileCheck.goto(),
                                                                        RemoveColorInput.goto()
                                                                    ]
                                                                ),
                                                                RemoveColorInput.goto()
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        If(
                                            elements=[
                                                StyleConditions.is_blank(),
                                                ColorConditions.has_value(),
                                                Output(
                                                    Prompt(
                                                        items=[
                                                            "Good choice, {User_Name}! I found {%s} results for {Recency_Preference} {Color_Preference}-rated movies." % NAME_RESULTS_COUNT]
                                                    ),
                                                    children=[AfterSearchResults.goto()]
                                                )
                                            ]
                                        ),
                                        If(
                                            elements=[
                                                ColorConditions.is_blank(),
                                                StyleConditions.has_value(),
                                                Output(
                                                    Prompt(
                                                        items=[
                                                            "Good choice, {User_Name}! I found {%s} results for {Color_Preference} {Style_Preference} movies." % NAME_RESULTS_COUNT]
                                                    ),
                                                    children=[AfterSearchResults.goto()]
                                                )
                                            ]
                                        ),
                                        If(
                                            elements=[
                                                ColorConditions.is_blank(),
                                                StyleConditions.is_blank(),
                                                Output(
                                                    Prompt(
                                                        items=[
                                                            "I found {%s} results for ALL {Recency_Preference} movies." % NAME_RESULTS_COUNT]
                                                    ),
                                                    children=[AfterSearchResults.goto()]
                                                )
                                            ]
                                        ),
                                        Output(
                                            Prompt(
                                                items=[
                                                    "Good choices, {User_Name}! I found {%s} results for {Color_Preference} {Style_Preference} movies." % NAME_RESULTS_COUNT]
                                            ),
                                            children=[AfterSearchResults.create()]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )


class AgainOption:
    @staticmethod
    def create():
        return Input(
            Grammar(
                watson_items=[
                    "again",
                    "$ again",
                    "$ one more time"
                ]),
            children=[
                PageAction.set_to_repeat(),
                Goto(ref="output_ok_do_search")
            ]
        )


class GoBackOption:
    @staticmethod
    def create():
        return Input(
            Grammar(
                watson_items=[
                    "Go back",
                    "$ back",
                    "$ previous",
                    "$ prior"
                ]
            ),
            children=[
                PageAction.set_to_previous(),
                Action("Show_Previous", operator="SET_TO_YES"),
                If(
                    elements=[
                        Condition(name="Current_Index", operator="EQUALS", root_text="10"),
                        Output(
                            prompt=Prompt(items=["Those were the first results"]),
                            children=[Goto(ref="profileCheck_2503183")]
                        )
                    ]
                ),
                Output(
                    prompt=GenericPrompt.ok(),
                    children=[
                        Output(
                            prompt=Prompt(
                                items=[
                                    "\"{Search_Now:\"{Search_Now}\", Style:\"{Style_Preference}\", Rating:\"{Color_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\"}\""
                                ]
                            ),
                            children=[
                                Action(var_name="Last_Results", operator="SET_TO_NO"),
                                GetUserInput(
                                    children=[
                                        Input(
                                            Grammar(watson_items=["UPDATE CURRENT_INDEX"]),
                                            children=[
                                                Action(var_name="Show_Next", operator="SET_TO_NO"),
                                                Action(var_name="Show_Previous", operator="SET_TO_NO"),
                                                If(
                                                    elements=[
                                                        Condition(name="First_Results", operator="EQUAL_TO_YES"),
                                                        Output(
                                                            prompt=Prompt(items=["Those were the first results"]),
                                                            children=[Goto(ref="getUserInput_2503174")]
                                                        )
                                                    ]
                                                ),
                                                If(
                                                    elements=[
                                                        Condition(name="Current_Index", operator="EQUALS",
                                                                  root_text="10"),
                                                        Output(
                                                            prompt=Prompt(items=["Here are the first results"]),
                                                            children=[
                                                                Action(var_name="First_Results", operator="SET_TO_YES"),
                                                                AfterSearchResults.goto()
                                                            ]
                                                        )]
                                                ),
                                                Output(
                                                    prompt=Prompt(items=["Here is the previous set of results"]),
                                                    children=[AfterSearchResults.goto()]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )


class MoreOption:
    @staticmethod
    def create():
        return Input(
            grammar=Grammar(
                items=[
                    "more",
                    "$ more",
                    "$ next",
                    "$ forward"
                ]
            ),
            children=[
                Action(var_name="Show_Next", operator="SET_TO_YES"),
                PageAction.set_to_next(),
                Output(
                    Prompt(items=["Okay."]),
                    children=[
                        Output(
                            Prompt(
                                "\"{Search_Now:\"{Search_Now}\", Color:\"{Color_Preference}\", Style:\"{Style_Preference}\", Index:\"{Current_Index}\", Page:\"{Page}\", Total_Movies:\"{%s}\", Total_Pages:\"{Total_Pages}\"}\"" % NAME_RESULTS_COUNT
                            ),
                            children=[
                                Action(var_name="First_Results", operator="SET_TO_NO"),
                                GetUserInput(
                                    _id="getUserInput_2503174",
                                    children=[
                                        Input(
                                            grammar=Grammar(items=["UPDATE CURRENT_INDEX"]),
                                            children=[
                                                Action(var_name="Show_Next", operator="SET_TO_NO"),
                                                Action(var_name="Show_Previous", operator="SET_TO_NO"),
                                                If(
                                                    elements=[
                                                        Condition(name="Last_Results", operator="EQUAL_TO_YES"),
                                                        Output(
                                                            prompt=Prompt(items="Those were the last results"),
                                                            children=[Goto(ref="profileCheck_2503183")]
                                                        )
                                                    ]
                                                ),
                                                If(
                                                    elements=[
                                                        Condition(name="Current_Index", operator="EQUALS",
                                                                  root_text="{%s}" % NAME_RESULTS_COUNT),
                                                        Output(
                                                            prompt=Prompt(
                                                                items=["Here are the last results"]
                                                            ),
                                                            children=[
                                                                Action(var_name="Last_Results", operator="SET_TO_YES"),
                                                                Goto(ref="profileCheck_2503183")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                Output(
                                                    prompt=Prompt(items=["Here is the next set of results"]),
                                                    children=[
                                                        If(
                                                            elements=[
                                                                StyleConditions.is_blank(),
                                                                ColorConditions.has_value(),
                                                                Output(
                                                                    prompt=Prompt(
                                                                        items=[
                                                                            "for {Style_Preference} {Color_Preference}-rated movies."]),
                                                                    children=[AfterSearchResults.goto()]
                                                                )
                                                            ],
                                                            _id="profileCheck_2503183"
                                                        ),
                                                        If(
                                                            elements=[
                                                                ColorConditions.is_blank(),
                                                                StyleConditions.has_value(),
                                                                Output(
                                                                    Prompt(
                                                                        items=[
                                                                            "for {Recency_Preference} {Genre_Preference} movies."]),
                                                                    children=[AfterSearchResults.goto()]
                                                                )
                                                            ]
                                                        ),
                                                        If(
                                                            elements=[
                                                                ColorConditions.is_blank(),
                                                                StyleConditions.is_blank(),
                                                                Output(
                                                                    prompt=Prompt(
                                                                        items=["for ALL {Recency_Preference} movies."]),
                                                                    children=[AfterSearchResults.goto()]
                                                                )
                                                            ]
                                                        ),
                                                        Output(
                                                            Prompt(items=[
                                                                "for {Recency_Preference} {Certification_Preference}-rated {Genre_Preference} movies."]),
                                                            children=[AfterSearchResults.goto()]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
