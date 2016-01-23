# from dialog.elements import Folder, Output
# from dialog.elements.default import Default
# from dialog.elements.dialog import Dialog
# from dialog.elements.search import Search
# from dialog.runners.conversation import Conversation
#
#
# class FolderRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, folder: Folder):
#         conversation.flow_position.append(folder._id)
#         goto_position = conversation.get_first_goto_position(folder)
#         if goto_position is not None:
#             if goto_position == folder._id:
#                 goto_position = conversation.get_first_goto_position(folder)
#             else:
#                 raise Exception()
#         print("start_folder_runner,_id=%s" % (folder._id))
#         for index, child in enumerate(folder.children):
#
#             if goto_position is None or index >= goto_position:
#                 conversation.flow_position.append(index)
#                 if isinstance(child, Output):
#                     from dialog.runners.output import OutputRunner
#                     OutputRunner.run(dialog, conversation, child)
#                 elif isinstance(child, Search):
#                     from dialog.runners.search import SearchRunner
#                     SearchRunner.run(dialog, conversation, child)
#                 elif isinstance(child, Default):
#                     from dialog.runners.default import DefaultRunner
#                     DefaultRunner.run(dialog, conversation, child)
#                 else:
#                     raise NotImplementedError(type(child))
#
#                 conversation.flow_position.pop()
#
#         conversation.flow_position.pop()
