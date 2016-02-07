from collections import deque



class Conversation:
    conversation_id = None
    flow_position = None
    flow_goto_position = None
    user_input = None
    current_input_context = None
    profile = {}
    default_get_user_input = None

    __goto_position = None

    @property
    def goto_position(self) -> deque:
        return self.__goto_position

    @goto_position.setter
    def goto_position(self, value):
        self.__goto_position = value

    def get_first_goto_position(self, element):
        from dialog.elements.get_user_input import GetUserInput

        # return self.goto_position.popleft() if self.goto_position is not None and any(self.goto_position) else None
        if self.goto_position is not None and any(self.goto_position):
            return self.goto_position.popleft()
        else:
            if isinstance(element, GetUserInput):
                self.default_get_user_input = element
            return None
