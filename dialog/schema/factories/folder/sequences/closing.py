from dialog.elements import Grammar, Prompt, Goto, Output, Input, If, Folder
from dialog.schema.factories.conditions.system import TerminalExchangeConditions
from dialog.schema.factories.prompts.generic import GenericPrompt


class ClosingSequences:
    @staticmethod
    def create():
        return Folder(
            label="CLOSING SEQUENCES",
            children=[
                Input(
                    children=[
                        Grammar(
                            items=[
                                "I should be going",
                                "$ should be going",
                                "$ should go",
                                "$ need to go",
                                "$ got to go",
                                "$ gotta run",
                                "$ gotta go",
                                "$ need to run",
                                "$ need to leave",
                                "$ have to leave",
                                "$ have to go",
                                "$ gtg"
                            ]
                        ),
                        Output(
                            _id="output_2449675",
                            children=[
                                GenericPrompt.ok(),
                                Goto(ref="output_did_find_what_looking_for")
                            ]
                        )
                    ]
                ),
                Input(
                    children=[
                        Grammar(
                            items=[
                                "Thanks for your help",
                                "$ thank you for your help",
                                "$ thanks for your help"
                            ]
                        ),
                        Output(
                            children=[
                                Prompt(
                                    items=["You are welcome."]
                                ),
                                Goto(ref="output_did_find_what_looking_for")
                            ]
                        )
                    ]
                ),
                Input(
                    children=[
                        Grammar(items=["Goodbye"]),
                        If(
                            elements=[
                                TerminalExchangeConditions.is_yes(),
                                Goto(ref="output_end_of_conversation")
                            ]
                        ),
                        If(
                            elements=[
                                TerminalExchangeConditions.is_no(),
                                Goto(ref="output_2449675")
                            ]
                        )
                    ]
                )
            ]
        )
