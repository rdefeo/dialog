from dialog.elements import Condition
from dialog.schema.factories.variables import NAME_TERMINAL_EXCHANGE

__author__ = 'robdefeo'


class TerminalExchangeConditions:
    @staticmethod
    def is_yes():
        return Condition(name=NAME_TERMINAL_EXCHANGE, operator="EQUAL_TO_YES")

    @staticmethod
    def is_no():
        return Condition(name=NAME_TERMINAL_EXCHANGE, operator="EQUAL_TO_NO")

