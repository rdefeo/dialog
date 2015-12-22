from dialog.elements import Output, Prompt, GetUserInput
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.get_user_input import GetUserInputRunner
from dialog.runners.prompt import PromptRunner


class OutputRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, output: Output):
        conversation.flow_position.append(output._id)
        goto_position = conversation.get_first_goto_position()
        if goto_position is not None:
            if goto_position == output._id:
                goto_position = conversation.get_first_goto_position()
            else:
                raise Exception()

        for index, child in enumerate(output.children):
            if goto_position is None or index >=goto_position :
                conversation.flow_position.append(index)
                if isinstance(child,  Prompt):
                    PromptRunner.run(dialog, conversation, child)
                elif isinstance(child,  GetUserInput):
                    GetUserInputRunner.run(dialog, conversation, child)
                else:
                    raise NotImplemented(type(child))
                conversation.flow_position.pop()

        conversation.flow_position.append(output._id)

