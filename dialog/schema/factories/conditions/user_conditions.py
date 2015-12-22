from dialog.elements import Condition
from dialog.schema.factories.variables import NAME_USER_NAME, NAME_FIRST_TIME, NAME_OUT_OF_SCOPE_COUNT

__author__ = 'robdefeo'


class UserNameConditions:
    @staticmethod
    def is_blank():
        return Condition(name=NAME_USER_NAME, operator="IS_BLANK")


class FirstTimeConditions:
    @staticmethod
    def is_yes():
        return Condition(name=NAME_FIRST_TIME, operator="EQUAL_TO_YES")


class OutOfScopeCountConditions:
    @staticmethod
    def is_greater_then(value):
        return Condition(name=NAME_OUT_OF_SCOPE_COUNT, operator="GREATER_THEN", root_text=value)
