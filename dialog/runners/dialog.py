from collections import deque
from copy import copy

from dialog.elements import Action, Output
from dialog.elements.dialog import Dialog
from dialog.get_user_input_exception import GetUserInputException
from dialog.runners.conversation import Conversation
from dialog.runners.flow import FlowRunner


class DialogRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation):
        print("U:%s" % conversation.user_input)
        if conversation.flow_position is not None:
            conversation.goto_position = deque(copy(conversation.flow_position))
        conversation.flow_position = []

        if conversation.flow_goto_position is not None:
            from dialog.runners.action import ActionRunner
            from dialog.runners.output import OutputRunner

            # conversation.goto_position = None
            goto_object = dialog.ref_ids[conversation.flow_goto_position]
            try:
                if isinstance(goto_object, Action):
                    ActionRunner.run(dialog, conversation, goto_object)
                elif isinstance(goto_object, Output):
                    OutputRunner.run(dialog, conversation, goto_object)
                else:
                    raise NotImplementedError(type(goto_object))
            except GetUserInputException as get_user_input:
                return get_user_input

        else:


            try:
                FlowRunner.run(dialog, conversation, dialog.flow)
            except GetUserInputException as get_user_input:
                return get_user_input

    @staticmethod
    def write_to_user(conversation: Conversation, text):
        print("J:"+ text.format(**conversation.profile))
        # conversation.conversation_id
        pass
