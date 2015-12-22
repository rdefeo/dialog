from collections import deque


class Conversation:
    conversation_id = None
    flow_position = None
    user_input = None

    __goto_position = None

    @property
    def goto_position(self) -> deque:
        return self.__goto_position

    @goto_position.setter
    def goto_position(self, value):
        self.__goto_position = value

    def get_first_goto_position(self):
        return self.goto_position.popleft() if self.goto_position is not None and any(self.goto_position) else None

        # def create_goto_position(self):
        #     self.goto_position = deque(copy(self.flow_position))
        #     self.flow_position = []
