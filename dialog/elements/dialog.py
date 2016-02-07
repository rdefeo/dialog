from collections import deque
from copy import copy

from dialog.elements.element import Element
from dialog.elements.goto import GotoException
from dialog.runners.conversation import Conversation


class Dialog(Element):
    from dialog.elements.entities import Entities
    from dialog.elements.flow import Flow
    _element_name = "dialog"
    entity_dict = {}

    def __init__(self, flow: Flow = None, entities: Entities = None, variables=None):
        """
            Node defines a top-level container for the dialog that you design.
            :param flow: flow
            :param entities: entities
             # |  | reports | settings | variables
            """
        settings = {
            "@xsi:noNamespaceSchemaLocation": "WatsonDialogDocument_1.0.xsd",
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        }

        super().__init__(settings, [flow, entities])
        self.variables = variables

        if entities is not None:
            self.entities = entities.entities
            for entity in self.entities:
                self.entity_dict[entity.name] = {}
                for value in entity.values:
                    for x in value.grammar.items:
                        self.entity_dict[entity.name][x] = value

        self.ref_ids = {}
        if flow is not None:
            self.flow = flow
            self.flow._set_dialog(self)
        else:
            raise Exception("flow needed")

    def entry_point(self, conversation: Conversation):
        print("U:%s" % conversation.user_input)
        dialog_runner_result = self.run(conversation)
        if dialog_runner_result is None and conversation.default_get_user_input is not None:
            return conversation.default_get_user_input
        else:
            return dialog_runner_result

    def run(self, conversation: Conversation):
        from dialog.elements.action import Action
        from dialog.elements.output import Output
        from dialog.elements.get_user_input import GetUserInput
        from dialog.elements.folder import Folder
        from dialog.elements.search import Search
        from dialog.elements.get_user_input import GetUserInputException

        if conversation.flow_position is not None:
            conversation.goto_position = deque(copy(conversation.flow_position))
        conversation.flow_position = []

        if conversation.flow_goto_position is not None:
            # conversation.goto_position = None
            goto_object = self.ref_ids[conversation.flow_goto_position]
            try:
                goto_object.run(conversation)
            except GetUserInputException as get_user_input:
                return get_user_input
            except GotoException as goto_exception:
                return self.run(conversation)
            pass
            # raise NotImplementedError()

        else:

            try:
                self.flow.run(conversation)
            except GotoException as goto_exception:
                return self.run(conversation)
            except GetUserInputException as get_user_input:
                return get_user_input

    @staticmethod
    def write_to_user(conversation: Conversation, text):
        print("J:" + text.format(**conversation.profile))
        # conversation.conversation_id
        pass
