

# class GotoException(Exception):
#     def __init__(self, conversation):
#         self.converstaion = conversation

#
# class GotoRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, goto: Goto):
#         from dialog.runners.action import ActionRunner
#         from dialog.runners.output import OutputRunner
#
#         conversation.flow_position = []
#         conversation.flow_goto_position = goto.ref
#         if goto.ref in dialog.ref_ids:
#             goto_object = dialog.ref_ids[goto.ref]
#             raise GotoException(conversation)
#
#
#         else:
#             raise Exception("can not find,id=%s" % goto.ref)
#