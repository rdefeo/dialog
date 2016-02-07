from dialog.elements import Goto, Input, Grammar
from dialog.schema.factories.action import PageAction, StylePreferenceAction, ColorPreferenceAction, CurrentIndexAction


class RemoveAllSearchCriteriaInput:
    @staticmethod
    def create():
        return Input(
            grammar=Grammar(
                watson_items=[
                    "all items",
                    "$ all items",
                    "$ all results"
                ]
            ),
            children=[
                CurrentIndexAction.set_to_zero(),
                PageAction.set_to_new(),
                StylePreferenceAction.set_to_blank(),
                ColorPreferenceAction.set_to_blank(),
                Goto(ref="output_ok_do_search")
            ]
        )
