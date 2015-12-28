from dialog.elements import Goto, Prompt, Output, Condition, If, Grammar, Input, GetUserInput
from dialog.elements.grammar_item import EntityGrammarItem
from dialog.schema.factories.action import StylePreferenceAction, PageAction, CurrentIndexAction, SearchNowAction
from dialog.schema.factories.conditions.style import StyleConditions
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.search import PreliminarySequencesSearch


class StylePreferenceProfileCheck:
    @staticmethod
    def __id():
        return "profileCheck_style_preference"

    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceProfileCheck.__id())

    @staticmethod
    def create():
        return If(
            _id=StylePreferenceProfileCheck.__id(),
            elements=[
                StyleConditions.is_blank(),
                Output(
                    Prompt(items=["Do you prefer a certain style? "]),
                    children=[
                        If(
                            elements=[
                                Condition(name="First_Time", operator="EQUAL_TO_YES"),
                                Output(
                                    Prompt(
                                        items=[
                                            "<mct:link><b><mct:input>High heels</mct:input></b></mct:link>\n<mct:link><b><mct:input>Boots</mct:input></b></mct:link>\n<mct:link><b><mct:input>Sandals</mct:input></b></mct:link>\n<mct:link><b><mct:input>Trainers</mct:input></b></mct:link>\n<mct:link><b><mct:input>No Preference</mct:input></b></mct:link>", ]
                                    ),
                                    children=[StylePreferenceProfileCheckInput.goto()]
                                )
                            ]
                        ),
                        StylePreferenceProfileCheckInput.create()
                    ]
                )
            ]
        )


class StylePreferenceProfileCheckInput:
    @staticmethod
    def __id():
        return "getUserInput_profileCheck_style_preference"

    @staticmethod
    def goto():
        return Goto(ref=StylePreferenceProfileCheckInput.__id())

    @staticmethod
    def create():
        return GetUserInput(
            _id=StylePreferenceProfileCheckInput.__id(),
            children=[
                Input(
                    Grammar(
                        watson_items=[
                            "What",
                            "$ what",
                            "$ which",
                            "$ tell me"
                        ]
                    ),
                    children=[
                        Input(
                            Grammar(
                                watson_items=[
                                    "styles",
                                    "$ they",
                                    "$ ones",
                                    "$ choices",
                                    "$ options",
                                    "$ styles",
                                    "$ what else"
                                ]
                            ),
                            children=[
                                Output(
                                    Prompt(
                                        items=[
                                            "For example.... Boots, High heels, Sandals, Trainers or Flats <br> <br>"]
                                    ),
                                    children=[StylePreferenceProfileCheckInput.goto()]
                                )
                            ]
                        )
                    ]
                ),
                Input(
                    Grammar(
                        items=[
                            EntityGrammarItem(dynamic_field_assignment="Style_Preference", entity_id="STYLE")
                        ],
                        watson_items=[
                            "Style",
                            "$ (Style)={Style_Preference}"
                        ]
                    ),
                    children=[
                        CurrentIndexAction.set_to_zero(),
                        PageAction.set_to_new(),
                        SearchNowAction.set_to_no(),
                        StylePreferenceAction.set_to_value(),
                        Goto(ref="output_ok_do_search")
                    ]
                ),
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
                #         (1, "goto"): StylePreferenceProfileCheckInput.goto()
                #     }
                # },
                Input(
                    Grammar(
                        watson_items=[
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
                    GenericGrammar.yes(),
                    children=[
                        Output(
                            Prompt(items=["What style?", "Please tell me the style you would prefer."]),
                            children=[StylePreferenceProfileCheckInput.goto()]
                        )
                    ]
                ),
                PreliminarySequencesSearch.goto()
            ]
        )
