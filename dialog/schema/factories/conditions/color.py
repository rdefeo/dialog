from dialog.schema.elements import Condition
from dialog.schema.factories.variables import NAME_COLOR_PREFERENCE


class ColorConditions:
    @staticmethod
    def is_blank():
        return Condition(name=NAME_COLOR_PREFERENCE, operator="IS_BLANK")

    @staticmethod
    def has_value():
        return Condition(name=NAME_COLOR_PREFERENCE, operator="HAS_VALUE")
