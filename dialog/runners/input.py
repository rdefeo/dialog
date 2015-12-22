from dialog.elements import Output, Prompt, GetUserInput, Input, Grammar
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.grammar import GrammarRunner

from dialog.runners.prompt import PromptRunner


class InputRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, _input: Input):
        conversation.flow_position.append(_input._id)
        goto_position = conversation.get_first_goto_position()
        if goto_position is not None:
            if goto_position == _input._id:
                goto_position = conversation.get_first_goto_position()
            else:
                raise Exception()

        for index, child in enumerate(_input.children):
            if goto_position is None or index >=goto_position :
                conversation.flow_position.append(index)
                if isinstance(child,  Grammar):
                    GrammarRunner.run(dialog, conversation, child)
                # elif isinstance(child,  GetUserInput):
                #     from dialog.runners.get_user_input import GetUserInputRunner
                #     GetUserInputRunner.run(dialog, conversation, child)
                else:
                    raise NotImplemented(type(child))
                conversation.flow_position.pop()

        conversation.flow_position.append(_input._id)

