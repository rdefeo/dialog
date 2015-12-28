from dialog.elements import Output, Prompt, GetUserInput, Goto, Action, Input
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation


class OutputRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, output: Output):
        conversation.flow_position.append(output._id)
        goto_position = conversation.get_first_goto_position(output)
        if goto_position is not None:
            if goto_position == output._id:
                goto_position = conversation.get_first_goto_position(output)
            else:
                raise Exception()

        for index, child in enumerate(output.children):
            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                if isinstance(child, Prompt):
                    from dialog.runners.prompt import PromptRunner
                    PromptRunner.run(dialog, conversation, child)
                elif isinstance(child, GetUserInput):
                    from dialog.runners.get_user_input import GetUserInputRunner
                    GetUserInputRunner.run(dialog, conversation, child)
                elif isinstance(child, Output):
                    OutputRunner.run(dialog, conversation, child)
                elif isinstance(child, Goto):
                    from dialog.runners.goto import GotoRunner
                    GotoRunner.run(dialog, conversation, child)
                elif isinstance(child, Input):
                    from dialog.runners.input import InputRunner
                    InputRunner.run(dialog, conversation, child)
                elif isinstance(child, Action):
                    from dialog.runners.action import ActionRunner
                    ActionRunner.run(dialog, conversation, child)
                else:
                    raise NotImplementedError(child)
                conversation.flow_position.pop()

        conversation.flow_position.pop()
