from dialog.elements import Condition

__author__ = 'robdefeo'


class StyleConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Style_Preference", operator="IS_BLANK")

    @staticmethod
    def has_value():
        return Condition(name="Style_Preference", operator="HAS_VALUE")
