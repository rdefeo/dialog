from dialog.elements import Goto, Action, Output
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation


class GotoRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, goto: Goto):
        from dialog.runners.action import ActionRunner
        from dialog.runners.output import OutputRunner

        # conversation.flow_position.append(goto._id)
        # goto_position = conversation.get_first_goto_position()
        # if goto_position is not None:
        #     if goto_position == goto._id:
        #         goto_position = conversation.get_first_goto_position()
        #     else:
        #         raise Exception()
        # think it just does this instead
        conversation.flow_position = []
        conversation.flow_goto_position = goto.ref
        if goto.ref in dialog.ref_ids:
            goto_object = dialog.ref_ids[goto.ref]
            if isinstance(goto_object,  Action):
                ActionRunner.run(dialog, conversation, goto_object)
            elif isinstance(goto_object,  Output):
                OutputRunner.run(dialog, conversation, goto_object)
            else:
                raise NotImplementedError(type(goto_object))

        else:
            raise NotImplementedError()
        conversation.flow_position.pop()
