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
                    PreliminarySequencesFolder.create(),
                    RoutingSequences.create(),
                    BaseSequences.create(),
                    GlobalSequences.create(),
                    Folder(label="Storage")
                ]
            ),
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
after_name_input = DialogRunner.run(dialog, user_input.conversation)
user_input.conversation.user_input = "Yes"
after_yes_shoes_input = DialogRunner.run(dialog, user_input.conversation)
pass
