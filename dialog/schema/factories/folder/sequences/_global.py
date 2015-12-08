from dialog.schema.factories.folder.sequences import ClosingSequences, OpeningSequences, UIActionsSequences, \
    RepairSequences, SmallTalkSequences


class GlobalSequences:
    @staticmethod
    def create():
        return {
            "@selectionType": "RANDOM",
            "@label": "GLOBAL SEQUENCES",
            "@id": "folder_global_sequences",
            (0, "folder"): [
                UIActionsSequences.create(),
                OpeningSequences.create(),
                ClosingSequences.create(),
                RepairSequences.create(),
                SmallTalkSequences.create()
            ]
        }
