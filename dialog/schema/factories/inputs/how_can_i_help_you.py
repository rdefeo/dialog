from dialog.elements import Goto, Prompt, Output, GetUserInput
from dialog.elements.default import Default
from dialog.elements.search import Search
from dialog.schema.factories.search import PreliminarySequencesSearch


class HowCanHelpYouInput:
    @staticmethod
    def goto():
        return Goto(ref=HowCanHelpYouInput.__id())

    @staticmethod
    def __id():
        return "getUserInput_how_can_i_help_you"

    @staticmethod
    def create():
        return GetUserInput(
            _id=HowCanHelpYouInput.__id(),
            children=[
                PreliminarySequencesSearch.create(),
                Search(
                    ref="folder_routing_sequences"
                ),
                Search(
                    _id="search_2414740",
                    ref="folder_base_sequences"
                ),
                Default(
                    children=[
                        Output(
                            is_insert_DNR_statement=True,
                            prompt=Prompt(
                                items=[
                                    "I'm not sure what you mean. I can understand things like <i>Show me recent PG13-rated Action movies.</i>"]
                            ),
                            children=[Goto(ref="##special_DNR_GET_USER_INPUT_NODE_ID")]
                        )
                    ]
                )
            ]
        )
