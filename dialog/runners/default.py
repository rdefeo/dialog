# from dialog.elements import Output, Prompt, GetUserInput, Goto
# from dialog.elements.default import Default
# from dialog.elements.dialog import Dialog
# from dialog.runners.conversation import Conversation
# from dialog.runners.get_user_input import GetUserInputRunner
# from dialog.runners.goto import GotoRunner
# from dialog.runners.prompt import PromptRunner
#
#
# class DefaultRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, default: Default):
#         conversation.flow_position.append(default._id)
#         goto_position = conversation.get_first_goto_position(default)
#         if goto_position is not None:
#             if goto_position == default._id:
#                 goto_position = conversation.get_first_goto_position(default)
#             else:
#                 raise Exception()
#
#         for index, child in enumerate(default.children):
#             if goto_position is None or index >= goto_position:
#                 conversation.flow_position.append(index)
#                 if isinstance(child, Output):
#                     from dialog.runners.output import OutputRunner
#                     OutputRunner.run(dialog, conversation, child)
#                 else:
#                     # for now seems important to only have default on here
#                     raise NotImplementedError(child)
#                 conversation.flow_position.pop()
#
#         conversation.flow_position.pop()
