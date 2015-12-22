from dialog.elements import Action
from dialog.elements.action import ACTION_SET_TO
from dialog.elements.dialog import Dialog
from dialog.runners.conversation import Conversation


class ActionRunner:
    @staticmethod
    def run(dialog: Dialog, conversation: Conversation, action: Action):
        if action.operator == ACTION_SET_TO:
            if "{" in action.settings["text"] and "}" in action.settings["text"]:
                input_context_key = action.settings["text"].strip("{").strip("}").strip(".source")
                conversation.profile[action.var_name] = conversation.current_input_context[action.var_name]
            else:
                raise NotImplemented()

            pass
        else:
            raise NotImplemented()

