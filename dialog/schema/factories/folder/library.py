from dialog.elements import Folder
from dialog.schema.factories.folder.sequences import BaseSequences, GlobalSequences, PreliminarySequencesFolder, \
    RoutingSequences, SystemInitiatedSequences


class LibraryFolder:
    @staticmethod
    def create():
        return Folder(
            label="Library",
            children=[
                SystemInitiatedSequences.create(),
                PreliminarySequencesFolder.create(),
                RoutingSequences.create(),
                BaseSequences.create(),
                GlobalSequences.create(),
                Folder(label="Storage")
            ]
        )
