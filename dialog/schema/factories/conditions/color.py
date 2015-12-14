from dialog.schema.elements import Condition


class ColorConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Color_Preference", operator="IS_BLANK")

    @staticmethod
    def has_value():
        return Condition(name="Color_Preference", operator="HAS_VALUE")
