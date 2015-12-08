from dialog.schema.elements import Action

__author__ = 'robdefeo'


class GreetingAction:
    @staticmethod
    def create_reset():
        return Action(varName="Greeting_Count", operator="SET_TO", text="0").create()

    @staticmethod
    def create_increment():
        return Action(varName="Greeting_Count", operator="INCREMENT_BY", text="1").create()


class TerminalExchangeAction:
    @staticmethod
    def create_no():
        return Action(varName="Terminal_Exchange", operator="SET_TO_NO").create()

    @staticmethod
    def create_yes():
        return Action(varName="Terminal_Exchange", operator="SET_TO_YES").create()


class SmallTalkAction:
    @staticmethod
    def create_reset():
        return Action(varName="Small_Talk_Count", operator="SET_TO", text="0").create()

    @staticmethod
    def create_increment():
        return Action(varName="Small_Talk_Count", operator="INCREMENT_BY", text="1").create()


