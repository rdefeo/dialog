from dialog.elements import Goto, Grammar, Input, Folder
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, TopicAction

__author__ = 'robdefeo'


class RoutingSequences:
    @staticmethod
    def create():
        return Folder(
            _id="folder_routing_sequences",
            label="ROUTING SEQUENCES",
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                Input(
                    Grammar(
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
                Input(
                    Grammar(
                        watson_items=[
                            "by out-of-scope movie topics",
                            "$ (BY_OTHER_MOVIE)={Topic}"
                        ]
                    ),
                    children=[
                        TopicAction.set_to_value(),
                        Goto(ref="output_2503370")
                    ]
                ),
                Input(
                    Grammar(
                        watson_items=[
                            "unsupported genres",
                            "$ (UNSUPPORTED_GENRES)={Topic}"
                        ]
                    ),
                    children=[
                        TopicAction.set_to_value(),
                        Goto(ref="output_2510164")
                    ]
                ),
                Input(
                    Grammar(
                        watson_items=[
                            "old movies",
                            "$ old movies",
                            "$ classic movies",
                            "$ oldies",
                            "$ classics"
                        ]
                    ),
                    children=[Goto(ref="output_2503380")]
                ),
                Input(
                    Grammar(
                        watson_items=[
                            "Review",
                            "$ review",
                            "$ find movies by rating",
                            "$ look up movies by rating",
                            "$ highest rating",
                            "$ highest rated",
                            "$ best rating",
                            "$ best rated",
                            "$ lowest rating",
                            "$ lowest rated",
                            "$ oscar winners",
                            "$ best movie",
                            "$ best movies"
                        ]
                    ),
                    children=[
                        GreetingAction.reset(),
                        SmallTalkAction.set_to_zero(),
                        Goto(ref="output_2469539")
                    ]
                ),
                Input(
                    Grammar(
                        [
                            "Movie theaters",
                            "$ movie theaters"
                        ]
                    ),
                    children=[
                        Goto(ref="output_2503320")
                    ]
                ),
                Input(
                    Grammar(
                        watson_items=[
                            "trailer",
                            "$ trailer",
                            "$ trailers"
                        ]
                    ),
                    children=[
                        GreetingAction.reset(),
                        SmallTalkAction.set_to_zero(),
                        Goto(ref="output_2510290")
                    ]
                )
            ]
        )
