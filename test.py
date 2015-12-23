from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.dialog import DialogRunner
from dialog.schema.entities import Entities
from dialog.schema.flow import Flow
from dialog.schema.variables import Variables

dialog = Dialog(
    flow=Flow().create(),
    entities=Entities().create(),
    variables=Variables().create()

    # {
    #     "folder": [
    #         MainFolder.create(),
    #         LibraryFolder.create(),
    #         GlobalFolder.create(),
    #         ConceptFolder.create()
    #     ]
    # }
    # ),
    # Entities().create(),
    # Variables().create()
)

user_input = DialogRunner.entry_point(dialog, Conversation())

user_input.conversation.user_input = "My name is Rob"
after_name_input = DialogRunner.entry_point(dialog, user_input.conversation)
user_input.conversation.user_input = "Yes"
after_yes_shoes_input = DialogRunner.entry_point(dialog, user_input.conversation)
user_input.conversation.user_input = "high heels"
after_style_input = DialogRunner.entry_point(dialog, user_input.conversation)
pass
