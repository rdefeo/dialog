from dialog.elements import Goto, Prompt, Output, If, Grammar, Input, GetUserInput
from dialog.schema.factories.action import ColorPreferenceAction, PageAction, CurrentIndexAction, SearchNowAction
from dialog.schema.factories.conditions import ColorConditions
from dialog.schema.factories.conditions.user_conditions import FirstTimeConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.search import PreliminarySequencesSearch


class ColorPreferenceProfileCheck:
    @staticmethod
    def __id():
        return "profileCheck_color_preference"

    @staticmethod
    def goto():
        return Goto(ref=ColorPreferenceProfileCheck.__id())

    @staticmethod
    def create():
        return If(
                _id=ColorPreferenceProfileCheck.__id(),
                elements=[
                    ColorConditions.is_blank(),
                    Output(
                            prompt=Prompt(items=["Do you prefer a certain color?"]),
                            children=[
                                If(
                                        elements=[
                                            FirstTimeConditions.is_yes(),
                                            Output(
                                                    prompt=Prompt(
                                                            items=[
                                                                "<mct:link><b><mct:input>Black</mct:input></b></mct:link>\n<mct:link><b><mct:input>White</mct:input></b></mct:link>\n<mct:link><b><mct:input>Red</mct:input></b></mct:link>\n<mct:link><b><mct:input>Green</mct:input></b></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>"]
                                                    ),
                                                    children=[
                                                        ColorPreferenceProfileCheckInput.goto()
                                                    ]
                                            )
                                        ]
                                ),
                                ColorPreferenceProfileCheckInput.create()
                            ]
                    )
                ]
        )


class ColorPreferenceProfileCheckInput:
    @staticmethod
    def __id():
        return "getUserInput_profileCheck_color_preference"

    @staticmethod
    def goto():
        return Goto(ref=ColorPreferenceProfileCheckInput.__id())

    @staticmethod
    def create():
        return GetUserInput(
                _id=ColorPreferenceProfileCheckInput.__id(),
                children=[
                    Input(
                            Grammar(
                                    items=[
                                        "What",
                                        "$ what",
                                        "$ which",
                                        "$ tell me"
                                    ]
                            ),
                            children=[
                                Input(
                                        Grammar(
                                                items=[
                                                    "colors",
                                                    "$ they",
                                                    "$ ones",
                                                    "$ choices",
                                                    "$ options",
                                                    "$ ratings",
                                                    "$ certifications",
                                                    "$ what else"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=["Black, White, Red, Brown or Green <br> <br>"]
                                                    ),
                                                    children=[ColorPreferenceProfileCheckInput.goto()]
                                            )
                                        ]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    items=[
                                        "Color",
                                        "$ (COLOR)={Color_Preference}"
                                    ]
                            ),
                            children=[
                                CurrentIndexAction.set_to_zero(),
                                PageAction.set_to_new(),
                                SearchNowAction.set_to_no(),
                                ColorPreferenceAction.set_to_value(),
                                Goto(ref="output_ok_do_search")
                            ]
                    ),
                    # TODO NOT SUPPORTED PATH
                    # {
                    #     (0, "grammar"): {
                    #         "item": [
                    #             "NC-17",
                    #             "$ NC-17"
                    #         ]
                    #     },
                    #     (1, "output"): {
                    #         (0, "prompt"): {
                    #             "item": "I'm afraid I cannot look up NC-17-rated movies.",
                    #             "@selectionType": "RANDOM"
                    #         },
                    #         (1, "goto"): {
                    #             "@ref": "getUserInput_2443780a"
                    #         }
                    #     }
                    # },
                    Input(
                            Grammar(
                                    items=[
                                        "No",
                                        "$ don't care",
                                        "$ don't know",
                                        "$ no preference",
                                        "$ no",
                                        "$ none",
                                        "$ all",
                                        "$ any",
                                        "$ anything",
                                        "$ whatever",
                                        "$ nothing specific",
                                        "$ don't have a preference"
                                    ]
                            ),
                            children=[
                                CurrentIndexAction.set_to_zero(),
                                PageAction.set_to_new(),
                                Goto(ref="output_2456875")
                            ]
                    ),
                    Input(
                            GenericGrammar.yes_okay(wildcard=False),
                            children=[
                                Output(
                                        Prompt(items=["Which one?"]),
                                        children=[ColorPreferenceProfileCheckInput.goto()]
                                )
                            ]
                    ),
                    PreliminarySequencesSearch.goto()
                ]
        )
