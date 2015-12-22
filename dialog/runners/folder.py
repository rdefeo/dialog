from dialog.elements import Folder, Output
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.output import OutputRunner


class FolderRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, folder: Folder):
        conversation.flow_position.append(folder._id)
        goto_position = conversation.get_first_goto_position()
        if goto_position is not None:
            if goto_position == folder._id:
                goto_position = conversation.get_first_goto_position()
            else:
                raise Exception()

        for index, child in enumerate(folder.children):
            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                if isinstance(child, Output):
                    OutputRunner.run(dialog, conversation, child)
                else:
                    raise NotImplemented(type(child))

                conversation.flow_position.pop()

        conversation.flow_position.pop()
