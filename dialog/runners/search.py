from dialog.elements import Output, Prompt, GetUserInput, Goto, Action, Input
from dialog.elements.dialog import Dialog
from dialog.elements.search import Search
from dialog.runners.action import ActionRunner
from dialog.runners.conversation import Conversation
from dialog.runners.get_user_input import GetUserInputRunner
from dialog.runners.input import InputRunner
from dialog.runners.prompt import PromptRunner


class SearchRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, search: Search):
        from dialog.runners.goto import GotoRunner
        from dialog.runners.output import OutputRunner

        conversation.flow_position.append(search._id)
        goto_position = conversation.get_first_goto_position(search)
        if goto_position is not None:
            if goto_position == search._id:
                goto_position = conversation.get_first_goto_position(search)
            else:
                raise Exception()

        search_object = dialog.ref_ids[search.ref]
        input_handled = False
        for index, child in enumerate(search_object.children):
            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                if isinstance(child, Prompt):
                    PromptRunner.run(dialog, conversation, child)
                elif isinstance(child, GetUserInput):
                    GetUserInputRunner.run(dialog, conversation, child)
                elif isinstance(child, Output):
                    OutputRunner.run(dialog, conversation, child)
                elif isinstance(child, Goto):
                    GotoRunner.run(dialog, conversation, child)
                elif isinstance(child, Action):
                    ActionRunner.run(dialog, conversation, child)
                elif isinstance(child, Input):
                    if not input_handled:
                        input_handled = InputRunner.run(dialog, conversation, child)
                else:
                    raise NotImplementedError(child)
                conversation.flow_position.pop()

        conversation.flow_position.pop()
