from dialog.schema.elements import If, Condition, Goto
from dialog.schema.factories.variables import NAME_USER_NAME, NAME_FIRST_TIME

__author__ = 'robdefeo'


class UserNameConditions:
    @staticmethod
    def is_blank():
        return Condition(name=NAME_USER_NAME, operator="IS_BLANK")


class FirstTimeConditions:
    @staticmethod
    def is_yes():
        return Condition(name=NAME_FIRST_TIME, operator="EQUAL_TO_YES")
