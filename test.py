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
            MainFolder.create(),
            Folder(
                label="Library",
                children=[
                    SystemInitiatedSequences.create(),
                    GlobalSequences.create(),
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
            GlobalFolder.create(),
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


user_input = DialogRunner.run(dialog, Conversation())

user_input.conversation.user_input = "My name is Rob"
test = DialogRunner.run(dialog, user_input.conversation)
pass
