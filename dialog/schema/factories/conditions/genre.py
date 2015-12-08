from dialog.schema.elements import If, Condition, Goto

__author__ = 'robdefeo'


class GenreConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Genre_Preference", operator="IS_BLANK")

    @staticmethod
    def has_value():
        return Condition(name="Genre_Preference", operator="HAS_VALUE")
