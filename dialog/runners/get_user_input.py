from dialog.elements import GetUserInput
from dialog.elements.dialog import Dialog
from dialog.get_user_input_exception import GetUserInputException
from dialog.runners.conversation import Conversation


class GetUserInputRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, get_user_input: GetUserInput):
        raise GetUserInputException(conversation, get_user_input)
