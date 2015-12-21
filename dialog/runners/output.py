from dialog.elements import Output, Prompt, GetUserInput
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation
from dialog.runners.get_user_input import GetUserInputRunner
from dialog.runners.prompt import PromptRunner


class OutputRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, output: Output):
        for index, child in enumerate(output.children):
            if isinstance(child,  Prompt):
                PromptRunner.run(dialog, conversation, child)
            elif isinstance(child,  GetUserInput):
                GetUserInputRunner.run(dialog, conversation, child)
            else:
                raise NotImplemented(type(child))

