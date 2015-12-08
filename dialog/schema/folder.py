from dialog.schema.elements import Action, Concept, Grammar
from dialog.schema.factories.action import GreetingAction, TerminalExchangeAction, SmallTalkAction
from dialog.schema.factories.folder.base_sequences import BaseSequences
from dialog.schema.factories.folder.global_sequences import GlobalSequences
from dialog.schema.factories.folder.preliminary_sequences import PreliminarySequences
from dialog.schema.factories.folder.routing_sequences import RoutingSequences
from dialog.schema.factories.folder.system_initiated_sequences import SystemInitiatedSequences
from dialog.schema.factories.grammar import FeelingGrammar, ProfileGrammar, GenericGrammar


class LibraryFolder:
    def create(self):
        return {
            "@label": "Library",
            "folder": [
                SystemInitiatedSequences.create(),
                PreliminarySequences.create(),
                RoutingSequences.create(),
                BaseSequences.create(),
                GlobalSequences.create(),
                {
                    "@label": "Storage"
                }
            ]
        }




