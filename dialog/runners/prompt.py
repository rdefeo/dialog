# from random import choice
# from dialog.elements import Prompt
# from dialog.elements.dialog import Dialog
# from dialog.runners.conversation import Conversation
#
#
#
# class PromptRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, prompt: Prompt):
#         from dialog.runners.dialog import DialogRunner
#         if prompt.selection_type == "RANDOM":
#             DialogRunner.write_to_user(conversation, choice(prompt.items))
#         else:
#             raise NotImplemented()
#
