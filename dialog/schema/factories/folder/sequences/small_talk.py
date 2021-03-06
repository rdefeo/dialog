from dialog.elements import Goto, Prompt, Grammar, Input, GetUserInput, Output, If, Folder
from dialog.schema.factories.action import SmallTalkAction, TopicAction
from dialog.schema.factories.conditions import SmallTalkConditions
from dialog.schema.factories.conditions.user_conditions import UserNameConditions
from dialog.schema.factories.search import PreliminarySequencesSearch

__author__ = 'robdefeo'


class SmallTalkSequences:
    @staticmethod
    def create():
        from dialog.schema.factories.folder.sequences import SystemInitiatedSequences
        return Folder(
                selection_type="RANDOM",
                label="SMALL TALK SEQUENCES",
                children=[
                    SmallTalkAction.create_increment(),
                    Input(
                            Grammar(
                                    watson_items=[
                                        "What is your name?",
                                        "$ your name",
                                        "$ you called",
                                        "$ they call you",
                                        "$ what can I call you"
                                    ]
                            ),
                            children=[
                                SmallTalkConditions.too_much_small_talk_goto(),
                                Output(
                                        Prompt(items=["My name is Jemboo."]),
                                        children=[If(
                                                elements=[
                                                    UserNameConditions.is_blank(),
                                                    Output(
                                                            Prompt(items=["What's your name?"]),
                                                            children=[Goto(ref="getUserInput_what_is_your_name")]
                                                    )
                                                ]
                                        ),
                                            GetUserInput(
                                                    children=[
                                                        Input(
                                                                Grammar(
                                                                        watson_items=[
                                                                            "Okay",
                                                                            "okay",
                                                                            "hi",
                                                                            "hi jemboo"
                                                                        ]
                                                                ),
                                                                children=[
                                                                    Goto(ref="output_what_is_name")
                                                                ]
                                                        ),
                                                        Input(
                                                                Grammar(
                                                                        watson_items=[
                                                                            "My name is",
                                                                            "$ my name",
                                                                            "$ call me",
                                                                            "$ I'm called",
                                                                            "$ I am called",
                                                                            "$ known as"
                                                                        ]
                                                                ),
                                                                children=[
                                                                    Goto(ref="input_user_knownas_name")
                                                                ]
                                                        ),
                                                        PreliminarySequencesSearch.goto()
                                                    ]
                                            )]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    watson_items=[
                                        "Siri",
                                        "$ (VIRTUAL_AGENTS)={Topic}"
                                    ]
                            ),

                            children=[
                                TopicAction.set_to_value(),
                                SmallTalkConditions.too_much_small_talk_goto(),
                                Input(
                                        Grammar(
                                                watson_items=[
                                                    "is better",
                                                    "$ better",
                                                    "$ smarter"
                                                ]
                                        ),
                                        children=[
                                            Output(
                                                    Prompt(items=["Now you're hurting my feelings."]),
                                                    children=[GetUserInput(
                                                            children=[
                                                                Input(
                                                                        Grammar(watson_items=["Okay", "$ sorry"]),
                                                                        children=[SystemInitiatedSequences.goto()]
                                                                ),
                                                                PreliminarySequencesSearch.goto()
                                                            ]
                                                    )]
                                            )
                                        ]
                                )
                            ]
                    ),
                    Input(
                            Grammar(
                                    watson_items=[
                                        "Do you speak English",
                                        "$ speak English",
                                        "$ understand English",
                                        "$ know English",
                                        "$ get English"
                                    ]
                            ),
                            children=[
                                SmallTalkConditions.too_much_small_talk_goto(),
                                Output(
                                        Prompt(items=[
                                            "I'm sorry, English is my second language. My native tongue is Binary. 01110011 01101111 01110010 01110010 01111001"]
                                        ),
                                        children=[GetUserInput(
                                                children=[
                                                    Input(
                                                            Grammar(watson_items=["haha", "ok"]),
                                                            children=[SystemInitiatedSequences.goto()]
                                                    ),
                                                    Input(
                                                            Grammar(
                                                                    watson_items=[
                                                                        "01101110 01110000",
                                                                        "01101110 01101111 00100000 01110000 01110010 01101111 01100010 01101100 01100101 01101101",
                                                                        "01101110 01110000",
                                                                        "01100100 01101111 01101110 00100111 01110100 00100000 01110111 01101111 01110010 01110010 01111001"
                                                                    ]
                                                            ),
                                                            children=[
                                                                Output(
                                                                        Prompt(items=["haha, you're good!"]),
                                                                        children=[SystemInitiatedSequences.goto()]
                                                                )
                                                            ]
                                                    ),
                                                    PreliminarySequencesSearch.goto()
                                                ]
                                        )]
                                )
                            ]
                    )
                ]
        )


        # {
        #     (0, "grammar"): {
        #         "item": [
        #             "What is your favorite",
        #             "$ your favorite",
        #             "$ favorite",
        #             "$ you like",
        #             "$ you prefer"
        #         ]
        #     },
        #     (1, "if"): SmallTalkConditions.too_much_small_talk_goto(),
        #     (2, "input"): [
        #         {
        #             (0, "grammar"): {
        #                 "item": [
        #                     "genre",
        #                     "$ genre",
        #                     "$ kind of movie"
        #                 ]
        #             },
        #             (1, "output"): {
        #                 (0, "prompt"): {
        #                     "item": "Well, Science Fiction is probably my favorite genre!",
        #                     "@selectionType": "RANDOM"
        #                 },
        #                 (1, "getUserInput"): {
        #                     (0, "input"): {
        #                         (0, "grammar"): {
        #                             "item": [
        #                                 "haha",
        #                                 "okay"
        #                             ]
        #                         },
        #                         (1, "goto"): HowCanHelpYouOutput.goto()
        #                     },
        #                     (1, "goto"): PreliminarySequencesSearch.goto()
        #                 }
        #             }
        #         },
        #         {
        #             (0, "grammar"): {
        #                 "item": [
        #                     "movie",
        #                     "$ movie"
        #                 ]
        #             },
        #             (1, "action"): {
        #                 "@varName": "Topic",
        #                 "@operator": "SET_TO",
        #                 "#text": "movie"
        #             },
        #             (2, "output"): {
        #                 (0, "prompt"): {
        #                     "item": "Oh... 2001: A Space Odyssey... Terminator... The Matrix... I guess I like movies with a strong AI lead.",
        #                     "@selectionType": "RANDOM"
        #                 },
        #                 (1, "getUserInput"): {
        #                     (0, "input"): {
        #                         (0, "grammar"): {
        #                             "item": [
        #                                 "haha",
        #                                 "okay"
        #                             ]
        #                         },
        #                         (1, "goto"): HowCanHelpYouOutput.goto()
        #                     },
        #                     (1, "goto"): PreliminarySequencesSearch.goto()
        #                 }
        #             }
        #         }
        #     ]
        # },
        # {
        #     (0, "grammar"): {
        #         "item": [
        #             "What is 2001: A Space Odyssey about?",
        #             "$ what is 2001 about"
        #         ]
        #     },
        #     (1, "if"): SmallTalkConditions.too_much_small_talk_goto(),
        #     (2, "output"): {
        #         (0, "prompt"): {
        #             "item": "It's about an intelligent computer, named HAL, who tries to kill the crew of a spaceship.",
        #             "@selectionType": "RANDOM"
        #         },
        #         (1, "getUserInput"): {
        #             (0, "input"): [
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Okay",
        #                             "haha"
        #                         ]
        #                     },
        #                     (1, "goto"): SystemInitiatedSequences.goto()
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Intelligent computer?",
        #                             "$ intelligent computer",
        #                             "$ named HAL",
        #                             "$ kill the crew",
        #                             "$ deactivate him",
        #                             "$ kill them first"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): Prompt(items=["Yes, that's right."]),
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457908"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "What do you mean",
        #                             "$ why",
        #                             "$ what do you mean"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): Prompt(items=[
        #                             "The human crew plans to deactivate him so HAL tries to kill them first."]),
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457908"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "What does HAL stand for?",
        #                             "$ HAL stand for",
        #                             "$ HAL mean"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "\"H-A-L\" is derived from Heuristic ALgorithm according to the author, Arthur C. Clarke. But there is also an urban legend that it is a code name for IBM. Shift each letter back once and see what you get!",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457908"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Does he succeed?",
        #                             "$ succeed",
        #                             "$ kill them",
        #                             "$ only tries"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): Prompt(items=["Well, I don't want to spoil the surprise!"]),
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457908"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "No, I mean",
        #                             "$ no i mean",
        #                             "$ no i meant",
        #                             "$ no",
        #                             "$ i mean",
        #                             "$ i meant",
        #                             "$ what about",
        #                             "$ how about"
        #                         ]
        #                     },
        #                     (1, "input"): [
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "The Terminator",
        #                                     "$ terminator"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457979"
        #                             }
        #                         },
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "The Matrix",
        #                                     "$ matrix"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457995"
        #                             }
        #                         }
        #                     ],
        #                     (2, "goto"): PreliminarySequencesSearch.goto()
        #                 }
        #             ],
        #             (1, "goto"): PreliminarySequencesSearch.goto(),
        #             "@id": "getUserInput_2457908"
        #         },
        #         "@id": "output_2457907"
        #     }
        # },
        # {
        #     (0, "grammar"): {
        #         "item": [
        #             "What is the Terminator about?",
        #             "$ what is the Terminator about",
        #             "$ what is Terminator about"
        #         ]
        #     },
        #     (1, "if"): SmallTalkConditions.too_much_small_talk_goto(),
        #     (2, "output"): {
        #         (0, "prompt"): {
        #             "item": "It's about a robot who travels back in time to kill the inventor of intelligent machines.",
        #             "@selectionType": "RANDOM"
        #         },
        #         (1, "getUserInput"): {
        #             (0, "input"): [
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Okay",
        #                             "haha"
        #                         ]
        #                     },
        #                     (1, "goto"): SystemInitiatedSequences.goto()
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "On earth?",
        #                             "$ on earth",
        #                             "$ a robot",
        #                             "$ killer robot",
        #                             "$ the inventor",
        #                             "$ intelligent machines",
        #                             "$ the 1980s",
        #                             "$ back in time"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "Yes, that's right.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457980"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "What do you mean",
        #                             "$ why",
        #                             "$ what do you mean"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "In the future, machines take over the world so the humans send a killer robot back to the 1980s to try to kill the guy who invented the intelligent machines.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457980"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Who is the Terminator",
        #                             "$ who is the terminator",
        #                             "$ who's the terminator",
        #                             "$ what is the terminator"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "The \"terminator\" is the killer robot from the future.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457980"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Does he succeed?",
        #                             "$ succeed",
        #                             "$ kill him",
        #                             "$ only tries"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "Well, I don't want to spoil the surprise!"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457980"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "No, I mean",
        #                             "$ no i mean",
        #                             "$ no i meant",
        #                             "$ no",
        #                             "$ i mean",
        #                             "$ i meant",
        #                             "$ what about",
        #                             "$ how about"
        #                         ]
        #                     },
        #                     (1, "input"): [
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "2001",
        #                                     "$ 2001"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457907"
        #                             }
        #                         },
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "The Matrix",
        #                                     "$ matrix"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457995"
        #                             }
        #                         }
        #                     ],
        #                     (2, "goto"): PreliminarySequencesSearch.goto()
        #                 }
        #             ],
        #             (1, "goto"): PreliminarySequencesSearch.goto(),
        #             "@id": "getUserInput_2457980"
        #         },
        #         "@id": "output_2457979"
        #     }
        # },
        # {
        #     (0, "grammar"): {
        #         "item": [
        #             "What is the Matrix about?",
        #             "$ what is the matrix about",
        #             "$ what is matrix about",
        #             "$ what is the matrix"
        #         ]
        #     },
        #     (1, "if"): SmallTalkConditions.too_much_small_talk_goto(),
        #     (2, "output"): {
        #         (0, "prompt"): {
        #             "item": "It's about a guy, named Neo, who has special powers for fighting intelligent programs in a computer simulation.",
        #             "@selectionType": "RANDOM"
        #         },
        #         (1, "getUserInput"): {
        #             (0, "input"): [
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Okay",
        #                             "haha"
        #                         ]
        #                     },
        #                     (1, "goto"): SystemInitiatedSequences.goto()
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "On earth?",
        #                             "$ on earth",
        #                             "$ in the future",
        #                             "$ named Neo",
        #                             "$ intelligent programs",
        #                             "$ computer simulation"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "Yes, that's right.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457996"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "What do you mean",
        #                             "$ why",
        #                             "$ what do you mean"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "In the future, machines take over the world and trick humans into believing that a simulation, The Matrix, is reality. But one human has special abilities for defeating the machines.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457996"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "What is the Matrix",
        #                             "$ what is the matrix"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "\"The Matrix\" is the name for the realistic computer simulation of earth.",
        #                             "@selectionType": "RANDOM"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457996"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "Does he succeed?",
        #                             "$ succeed",
        #                             "$ kill him",
        #                             "$ only tries"
        #                         ]
        #                     },
        #                     (1, "output"): {
        #                         (0, "prompt"): {
        #                             "item": "Well, I don't want to spoil the surprise!"
        #                         },
        #                         (1, "goto"): {
        #                             "@ref": "getUserInput_2457996"
        #                         }
        #                     }
        #                 },
        #                 {
        #                     (0, "grammar"): {
        #                         "item": [
        #                             "No, I mean",
        #                             "$ no i mean",
        #                             "$ no i meant",
        #                             "$ no",
        #                             "$ i mean",
        #                             "$ i meant",
        #                             "$ what about",
        #                             "$ how about"
        #                         ]
        #                     },
        #                     (1, "input"): [
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "2001",
        #                                     "$ 2001"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457907"
        #                             }
        #                         },
        #                         {
        #                             (0, "grammar"): {
        #                                 "item": [
        #                                     "Terminator",
        #                                     "$ terminator"
        #                                 ]
        #                             },
        #                             (1, "action"): CertificationPreferenceAction.set_to_value(),
        #                             (2, "goto"): {
        #                                 "@ref": "output_2457979"
        #                             }
        #                         }
        #                     ],
        #                     (2, "goto"): PreliminarySequencesSearch.goto()
        #                 }
        #             ],
        #             (1, "goto"): PreliminarySequencesSearch.goto(),
        #             "@id": "getUserInput_2457996"
        #         },
        #         "@id": "output_2457995"
        #     }
        # }
