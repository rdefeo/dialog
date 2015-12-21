from dialog.elements import Flow
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.folder import FolderRunner


class FlowRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, flow: Flow):
        for index, folder in enumerate(flow.folders):
            conversation.flow_position.append(index)
            FolderRunner.run(dialog, conversation, folder)
            conversation.flow_position.pop()
