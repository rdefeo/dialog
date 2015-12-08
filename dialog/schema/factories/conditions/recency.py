from dialog.schema.elements import If, Condition, Goto

__author__ = 'robdefeo'


class RecencyConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Recency_Preference", operator="IS_BLANK")

