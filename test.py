from dialog.elements import Folder
from dialog.elements.flow import Flow
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.dialog import DialogRunner
from dialog.schema.factories.folder._global import GlobalFolder
from dialog.schema.factories.folder.main import MainFolder
from dialog.schema.factories.folder.sequences import SystemInitiatedSequences, PreliminarySequencesFolder, \
    RoutingSequences, BaseSequences, GlobalSequences

dialog = Dialog(
    flow=Flow(
        folders=[
            MainFolder,
            Folder(
                label="Library",
                children=[
                    SystemInitiatedSequences,
                    GlobalSequences,
                    Folder(label="Storage")
                ]
            ),
            # {
            #     "@label": "Library",
            #     "folder": [
            #         # SystemInitiatedSequences.create(),
            #         # PreliminarySequencesFolder.create(),
            #         # RoutingSequences.create(),
            #         # BaseSequences.create(),
            #         # GlobalSequences.create(),
            #         # Folder(label="Storage").create()
            #     ]
            # },
            GlobalFolder,
        ]
        # {
        #     "folder": [
        #         MainFolder.create(),
        #         LibraryFolder.create(),
        #         GlobalFolder.create(),
        #         ConceptFolder.create()
        #     ]
        # }
    ),
    # Entities().create(),
    # Variables().create()
)


DialogRunner.run(dialog, Conversation())
