from dialog.elements import Action
from dialog.schema.factories.variables import NAME_PAGE, NAME_CURRENT_INDEX, NAME_SEARCH_NOW, NAME_USER_NAME


class CertificationPreferenceAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Certification_Preference", operator="SET_TO_BLANK")

    @staticmethod
    def set_to_value():
        return Action(var_name="Certification_Preference", operator="SET_TO",
                      text="{Certification_Preference.value:main}")


class UserNameAction:
    @staticmethod
    def set_to_source():
        return Action(var_name=NAME_USER_NAME, operator="SET_TO", text="{User_Name.source}")


class PageAction:
    @staticmethod
    def set_to_new():
        return Action(var_name=NAME_PAGE, operator="SET_TO", text="new")

    @staticmethod
    def set_to_repeat():
        return Action(var_name=NAME_PAGE, operator="SET_TO", text="repeat")

    @staticmethod
    def set_to_previous():
        return Action(var_name=NAME_PAGE, operator="SET_TO", text="previous")

    @staticmethod
    def set_to_next():
        return Action(var_name=NAME_PAGE, operator="SET_TO", text="next")


class CurrentIndexAction:
    @staticmethod
    def set_to_zero():
        return Action(var_name=NAME_CURRENT_INDEX, operator="SET_TO", text="0")


# TODO delete me!
class RecencyPreferenceAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Recency_Preference", operator="SET_TO_BLANK")

    @staticmethod
    def create_set_to_value():
        return Action(var_name="Recency_Preference", operator="SET_TO", text="{Recency_Preference.value:main}")

    @staticmethod
    def create_set_to_upcoming():
        return Action(var_name="Recency_Preference", operator="SET_TO", text="Upcoming")

    @staticmethod
    def set_to_current():
        return Action(var_name="Recency_Preference", operator="SET_TO", text="Current")


class StylePreferenceAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Style_Preference", operator="SET_TO_BLANK")

    @staticmethod
    def set_to_value():
        return Action(var_name="Style_Preference", operator="SET_TO", text="{Style_Preference.value:main}")


class ColorPreferenceAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Color_Preference", operator="SET_TO_BLANK")

    @staticmethod
    def set_to_value():
        return Action(var_name="Color_Preference", operator="SET_TO", text="{Color_Preference.value:main}")


class GreetingAction:
    @staticmethod
    def reset():
        return Action(var_name="Greeting_Count", operator="SET_TO", text="0")

    @staticmethod
    def create_increment():
        return Action(var_name="Greeting_Count", operator="INCREMENT_BY", text="1")


class SearchNowAction:
    @staticmethod
    def set_to_no():
        return Action(var_name=NAME_SEARCH_NOW, operator="SET_TO_NO")

    @staticmethod
    def set_to_yes():
        return Action(var_name=NAME_SEARCH_NOW, operator="SET_TO_YES")


class TerminalExchangeAction:
    @staticmethod
    def set_to_no():
        return Action(var_name="Terminal_Exchange", operator="SET_TO_NO")

    @staticmethod
    def set_to_yes():
        return Action(var_name="Terminal_Exchange", operator="SET_TO_YES")

    @staticmethod
    def set_to_blank():
        return Action(var_name="Terminal_Exchange", operator="SET_TO_BLANK")


class TopicAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Topic", operator="SET_TO_BLANK")

    @staticmethod
    def set_to_value():
        return Action(var_name="Topic", operator="SET_TO", text="{Topic.value:main}")

    @staticmethod
    def set_to_shoes():
        return Action(var_name="Topic", operator="SET_TO", text="shoes")


class RequestSuccessAction:
    @staticmethod
    def set_to_blank():
        return Action(var_name="Request_Success", operator="SET_TO_BLANK")

    @staticmethod
    def set_to_yes():
        return Action(var_name="Request_Success", operator="SET_TO_YES")

    @staticmethod
    def set_to_no():
        return Action(var_name="Request_Success", operator="SET_TO_NO")


class SmallTalkAction:
    @staticmethod
    def set_to_zero():
        return Action(var_name="Small_Talk_Count", operator="SET_TO", text="0")

    @staticmethod
    def create_increment():
        return Action(var_name="Small_Talk_Count", operator="INCREMENT_BY", text="1")
