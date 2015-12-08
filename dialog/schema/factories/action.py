from dialog.schema.elements import Action

__author__ = 'robdefeo'


class RecencyPreferenceAction:
    @staticmethod
    def create_reset():
        return Action(varName="Recency_Preference", operator="SET_TO_BLANK").create()

    @staticmethod
    def create_set_to_value():
        return Action(varName="Recency_Preference", operator="SET_TO", text="{Recency_Preference.value:main}").create()

    @staticmethod
    def create_set_to_upcoming():
        return Action(varName="Recency_Preference", operator="SET_TO", text="Upcoming").create()

    @staticmethod
    def create_set_to_current():
        return Action(varName="Recency_Preference", operator="SET_TO", text="Current").create()


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
