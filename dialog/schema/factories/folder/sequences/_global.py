from dialog.elements import Folder
from dialog.schema.factories.folder.sequences import ClosingSequences, OpeningSequences, UIActionsSequences, \
    RepairSequences, SmallTalkSequences


class GlobalSequences:
    @staticmethod
    def create():
        return Folder(
            # "@selectionType": "RANDOM",
            label="GLOBAL SEQUENCES",
            _id="folder_global_sequences",
            children=[
                UIActionsSequences.create(),
                OpeningSequences.create(),
                ClosingSequences.create(),
                RepairSequences.create(),
                SmallTalkSequences.create()
            ]
        )
