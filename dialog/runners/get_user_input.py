from dialog.elements import GetUserInput, Input
from dialog.elements.dialog import Dialog
from dialog.get_user_input_exception import GetUserInputException
from dialog.runners.conversation import Conversation

from dialog.runners.input import InputRunner


class GetUserInputRunner(Exception):
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, get_user_input: GetUserInput):
        conversation.flow_position.append(get_user_input._id)
        goto_position = conversation.get_first_goto_position()
        if goto_position is None:
            raise GetUserInputException(conversation, get_user_input)
        else:
            if goto_position == get_user_input._id:
                # so now it needs to look through the possible responses
                goto_position = conversation.get_first_goto_position()
            else:
                raise Exception()

            for index, child in enumerate(get_user_input.children):
                if goto_position is None or index >=goto_position :
                    conversation.flow_position.append(index)
                    if isinstance(child, Input):
                        InputRunner.run(dialog, conversation, child)
                    else:
                        raise NotImplemented(type(child))

                    conversation.flow_position.pop()

            conversation.flow_position.pop()


