from dialog.schema.factories.folder.sequences import BaseSequences, GlobalSequences, PreliminarySequences, \
    RoutingSequences, SystemInitiatedSequences


class LibraryFolder:
    @staticmethod
    def create():
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
