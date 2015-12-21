from dialog.elements import Folder, Output
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.output import OutputRunner


class FolderRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, folder: Folder):
        for index, child in enumerate(folder.children):
            conversation.flow_position.append(index)
            if isinstance(child, Output):
                OutputRunner.run(dialog, conversation, child)
            else:
                raise NotImplemented(type(child))

            conversation.flow_position.pop()
