from dialog.elements import GetUserInput
from dialog.runners.conversation import Conversation

__author__ = 'robdefeo'


class GetUserInputException(Exception):
    def __init__(self, conversation: Conversation, get_user_input: GetUserInput):
        self.get_user_input = get_user_input
        self.conversation = conversation
