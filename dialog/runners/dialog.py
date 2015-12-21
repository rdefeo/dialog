from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.flow import FlowRunner


class DialogRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation):
        FlowRunner.run(dialog, conversation, dialog.flow)

    @staticmethod
    def write_to_user(conversation: Conversation, text):
        conversation.conversation_id
        pass
