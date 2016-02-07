# from collections import deque
# from copy import copy
#
# from dialog.elements import Action, Output, GetUserInput, Folder
# from dialog.elements.dialog import Dialog
# from dialog.elements.search import Search
# from dialog.get_user_input_exception import GetUserInputException
# from dialog.runners.conversation import Conversation
# from dialog.runners.flow import FlowRunner
# from dialog.runners.get_user_input import GetUserInputRunner
# from dialog.runners.goto import GotoException
#
#
# class DialogRunner:
#     @staticmethod
#     def entry_point(dialog: Dialog, conversation: Conversation):
#         print("U:%s" % conversation.user_input)
#         dialog_runner_result = DialogRunner.run(dialog, conversation)
#         if dialog_runner_result is None and conversation.default_get_user_input is not None:
#             return conversation.default_get_user_input
#         else:
#             return dialog_runner_result
#
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation):
#         if conversation.flow_position is not None:
#             conversation.goto_position = deque(copy(conversation.flow_position))
#         conversation.flow_position = []
#
#         if conversation.flow_goto_position is not None:
#             # conversation.goto_position = None
#             goto_object = dialog.ref_ids[conversation.flow_goto_position]
#             try:
#                 if isinstance(goto_object, Action):
#                     from dialog.runners.action import ActionRunner
#                     ActionRunner.run(dialog, conversation, goto_object)
#                 elif isinstance(goto_object, Output):
#                     from dialog.runners.output import OutputRunner
#                     OutputRunner.run(dialog, conversation, goto_object)
#                 elif isinstance(goto_object, GetUserInput):
#                     GetUserInputRunner.run(dialog, conversation, goto_object)
#                 elif isinstance(goto_object, Folder):
#                     from dialog.runners.folder import FolderRunner
#                     FolderRunner.run(dialog, conversation, goto_object)
#                 elif isinstance(goto_object, Search):
#                     from dialog.runners.search import SearchRunner
#                     SearchRunner.run(dialog, conversation, goto_object)
#                 else:
#                     raise NotImplementedError(type(goto_object))
#             except GetUserInputException as get_user_input:
#                 return get_user_input
#             except GotoException as goto_exception:
#                 return DialogRunner.run(dialog, conversation)
#             pass
#             # raise NotImplementedError()
#
#         else:
#
#             try:
#                 FlowRunner.run(dialog, conversation, dialog.flow)
#             except GotoException as goto_exception:
#                 return DialogRunner.run(dialog, conversation)
#             except GetUserInputException as get_user_input:
#                 return get_user_input
#
#     @staticmethod
#     def write_to_user(conversation: Conversation, text):
#         print("J:" + text.format(**conversation.profile))
#         # conversation.conversation_id
#         pass
