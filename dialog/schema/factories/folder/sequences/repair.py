from dialog.elements import Prompt, Grammar, Goto, Output, Input, GetUserInput, Folder
from dialog.schema.factories.action import TopicAction


class RepairSequences:
    @staticmethod
    def create():
        from dialog.schema.factories.folder.sequences import SystemInitiatedSequences

        return Folder(
                label="REPAIR SEQUENCES",
                children=[
                    Input(
                            Grammar(
                                    items=[
                                        "Help",
                                        "$ help",
                                        "$ how does this work",
                                        "$ what do I do",
                                        "$ what can I do",
                                        "$ don't know",
                                        "$ I'm not sure"
                                    ]
                            ),
                            children=[
                                Output(
                                        Prompt(
                                                items=[
                                                    "Say <i>Never mind</i> or <i>nvm</i> to start over.\nSay <i>okay</i> or <i>thanks</i> if my response is acceptable.\nSay <i>What does X mean?</i> for a definition of X.\nSay <i>got to go</i> or <i>bye</i> when you're finished."
                                                ]
                                        )
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    items=[
                                        "Say that again",
                                        "$ say that again",
                                        "$ say again",
                                        "$ what did you say",
                                        "$ come again",
                                        "$ say what"
                                    ]
                            ),
                            children=[
                                Output(
                                        Prompt(items=["I said..."]),
                                        children=[Goto(ref="##special_DNR_GUI_PREVIOUS_OUTPUT_NODE_ID")]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    items=[
                                        "Never mind",
                                        "$ Nevermind",
                                        "$ Never mind",
                                        "$ nvm",
                                        "$ start over",
                                        "$ start again",
                                        "$ restart",
                                        "$ redo",
                                        "$ do over",
                                        "$ start from * beginning",
                                        "$ clear * selections"
                                    ]
                            ),
                            children=[
                                Output(
                                        Prompt(items=["Okay. Whatever you say, {User_Name}!"]),
                                        children=[SystemInitiatedSequences.goto()]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    items=[
                                        "what does * mean",
                                        "$ what does * mean",
                                        "$ what does * stand for",
                                        "$ do you mean by ",
                                        "$ what are examples of",
                                        "$ what is an example of"
                                    ]
                            ),
                            children=[
                                Input(
                                        Grammar(
                                                items=[
                                                    "trailers",
                                                    "$ trailer",
                                                    "$ trailers"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "<i>Trailers</i> are video previews for movies. <br> <br>"]
                                                    ),
                                                    children=[
                                                        GetUserInput(
                                                                children=[
                                                                    Input(
                                                                            Grammar(items=["okay"]),
                                                                            children=[
                                                                                Output(
                                                                                        Prompt(items=[
                                                                                            "Sure, happy to help. <br> <br>"]),
                                                                                        children=[Goto(
                                                                                                ref="##special_DNR_GET_USER_INPUT_NODE_ID")]
                                                                                )
                                                                            ]
                                                                    )
                                                                ]
                                                        )
                                                    ],
                                                    is_insert_DNR_statement=True
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "genre",
                                                    "$ genre",
                                                    "$ genres"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "The <i>genre</i> is the category of movie, like Drama, Comedy, Action, etc. <br> <br>"
                                                            ]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "rating",
                                                    "$ rating",
                                                    "$ ratings",
                                                    "$ mpaa"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "The <i>rating</i> is a recommendation by the Motion Picture Association of America about the suitability of a movie's content for particular age groups. For example, G is for general audiences, while R is restricted to people 17 and older.<br> <br>"]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "G",
                                                    "$ G"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "G stands for <i>General Audience</i> and is appropriate for everyone.", ]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "PG-13",
                                                    "$ PG-13"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "PG-13 means <i>Parents Strongly Cautioned</i> or that some material may not be suitable for children under 13 years old.",
                                                            ]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "Current",
                                                    "$ current"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "<i>Current</i> movies are those that have been playing for the past 28 days."
                                                            ]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "Upcoming",
                                                    "$ upcoming"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "<i>Upcoming</i> movies are those that will come out within the next 6 months."
                                                            ]
                                                    )
                                            )
                                        ]
                                ),
                                Input(
                                        Grammar(
                                                items=[
                                                    "$ (GENRE)={Topic}",
                                                    "$ (UNSUPPORTED_GENRES)={Topic}"
                                                ]
                                        ),
                                        children=[
                                            TopicAction.set_to_value(),
                                            Output(
                                                    Prompt(
                                                            items=[
                                                                "I'm afraid I don't have definitions of the different genres."
                                                            ]
                                                    )
                                            )
                                        ]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    items=[
                                        "I already told you!",
                                        "$ already told you",
                                        "$ already said it"
                                    ]
                            ),
                            children=[
                                Output(
                                        Prompt(
                                                items=["I'm sorry, please repeat it for me."]
                                        ),
                                        children=[Goto(ref="getUserInput_how_can_i_help_you")]
                                )
                            ]
                    )
                ]
        )
