from dialog.elements import Goto, Action, Output, GetUserInput
from dialog.elements.dialog import Dialog
from dialog.elements.search import Search
from dialog.runners.conversation import Conversation
from dialog.runners.get_user_input import GetUserInputRunner
from dialog.runners.search import SearchRunner

class GotoException(Exception):
    def __init__(self, conversation):
        self.converstaion = conversation


class GotoRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, goto: Goto):
        from dialog.runners.action import ActionRunner
        from dialog.runners.output import OutputRunner

        conversation.flow_position = []
        conversation.flow_goto_position = goto.ref
        if goto.ref in dialog.ref_ids:
            goto_object = dialog.ref_ids[goto.ref]
            raise GotoException(conversation)


        else:
            raise Exception("can not find,id=%s" % goto.ref)
    # @staticmethod
    # def run(dialog: Dialog, conversation: Conversation, goto: Goto):
    #     from dialog.runners.action import ActionRunner
    #     from dialog.runners.output import OutputRunner
    #
    #     conversation.flow_position = []
    #     conversation.flow_goto_position = goto.ref
    #     if goto.ref in dialog.ref_ids:
    #         goto_object = dialog.ref_ids[goto.ref]
    #         if isinstance(goto_object, Action):
    #             ActionRunner.run(dialog, conversation, goto_object)
    #         elif isinstance(goto_object, Output):
    #             OutputRunner.run(dialog, conversation, goto_object)
    #         elif isinstance(goto_object, GetUserInput):
    #             GetUserInputRunner.run(dialog, conversation, goto_object)
    #         elif isinstance(goto_object, Search):
    #             SearchRunner.run(dialog, conversation, goto_object)
    #         else:
    #             raise NotImplementedError(type(goto_object))
    #
    #     else:
    #         raise Exception("can not find,id=%s" % goto.ref)
