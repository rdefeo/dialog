# from dialog.elements import Flow
# from dialog.elements.dialog import Dialog
# from dialog.runners.conversation import Conversation
# from dialog.runners.folder import FolderRunner
#
#
# class FlowRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, flow: Flow):
#         # conversation.flow_position.append(flow._id)
#         goto_position = conversation.get_first_goto_position(flow)
#         for index, folder in enumerate(flow.folders):
#             if goto_position is None or index >= goto_position:
#                 conversation.flow_position.append(index)
#                 FolderRunner.run(dialog, conversation, folder)
#                 conversation.flow_position.pop()
#
#         # conversation.flow_position.pop()
