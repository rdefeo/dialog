from dialog.schema.elements import If, Condition, Goto
from dialog.schema.factories.variables import NAME_USER_NAME

__author__ = 'robdefeo'


class UserConditions:
    @staticmethod
    def is_blank():
        return Condition(name=NAME_USER_NAME, operator="IS_BLANK")
