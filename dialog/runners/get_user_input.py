from dialog.elements import GetUserInput, Input, Goto, Folder
from dialog.elements.dialog import Dialog
from dialog.get_user_input_exception import GetUserInputException
from dialog.runners.conversation import Conversation


class GetUserInputRunner(Exception):
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, get_user_input: GetUserInput):
        goto_position = conversation.get_first_goto_position(get_user_input)
        conversation.flow_position.append(get_user_input._id)
        if goto_position is None:
            raise GetUserInputException(conversation, get_user_input)
        else:
            if goto_position == get_user_input._id:
                # so now it needs to look through the possible responses
                goto_position = conversation.get_first_goto_position(get_user_input)
            else:
                raise Exception()

            for index, child in enumerate(get_user_input.children):
                if goto_position is None or index >= goto_position:
                    conversation.flow_position.append(index)
                    if isinstance(child, Input):
                        from dialog.runners.input import InputRunner
                        InputRunner.run(dialog, conversation, child)
                    elif isinstance(child, Goto):
                        from dialog.runners.goto import GotoRunner
                        GotoRunner.run(dialog, conversation, child)
                    elif isinstance(child, Folder):
                        from dialog.runners.folder import FolderRunner
                        FolderRunner.run(dialog, conversation, child)
                    else:
                        raise NotImplementedError(type(child))

                    conversation.flow_position.pop()

            conversation.flow_position.pop()
