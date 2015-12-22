from collections import deque
from copy import copy

from dialog.elements.dialog import Dialog
from dialog.get_user_input_exception import GetUserInputException
from dialog.runners.conversation import Conversation
from dialog.runners.flow import FlowRunner


class DialogRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation):
        if conversation.flow_position is not None:
            conversation.goto_position = deque(copy(conversation.flow_position))

        conversation.flow_position = []

        try:
            FlowRunner.run(dialog, conversation, dialog.flow)
        except GetUserInputException as get_user_input:
            return get_user_input

    @staticmethod
    def write_to_user(conversation: Conversation, text):
        print(text)
        # conversation.conversation_id
        pass
