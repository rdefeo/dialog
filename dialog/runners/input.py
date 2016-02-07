# from dialog.elements import Output, Input, Action, Goto
# from dialog.elements.dialog import Dialog
# from dialog.runners.conversation import Conversation
# from dialog.runners.grammar import GrammarRunner
#
#
# class InputRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, _input: Input):
#
#         handled = False
#         conversation.flow_position.append(_input._id)
#         goto_position = conversation.get_first_goto_position(_input)
#         if goto_position is not None:
#             if goto_position == _input._id:
#                 goto_position = conversation.get_first_goto_position(_input)
#             else:
#                 raise Exception()
#         if GrammarRunner.run(dialog, conversation, _input.grammar):
#             for index, child in enumerate(_input.children):
#                 if goto_position is None or index >= goto_position:
#                     conversation.flow_position.append(index)
#                     if isinstance(child, Action):
#                         from dialog.runners.action import ActionRunner
#                         ActionRunner.run(dialog, conversation, child)
#                     elif isinstance(child, Output):
#                         from dialog.runners.output import OutputRunner
#                         OutputRunner.run(dialog, conversation, child)
#                     elif isinstance(child, Goto):
#                         from dialog.runners.goto import GotoRunner
#                         GotoRunner.run(dialog, conversation, child)
#                     else:
#                         raise NotImplementedError(type(child))
#                     conversation.flow_position.pop()
#
#             handled = True
#
#         conversation.flow_position.pop()
#         return handled
