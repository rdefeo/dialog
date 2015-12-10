from dialog.schema.elements import If, Condition, Goto

__author__ = 'robdefeo'


class StyleConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Style_Preference", operator="IS_BLANK")

