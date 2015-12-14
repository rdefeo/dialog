from dialog.schema.elements import Condition
from dialog.schema.factories.variables import NAME_RESULTS_COUNT


class ResultsCountConditions:
    @staticmethod
    def equals_zero():
        return Condition(name=NAME_RESULTS_COUNT, operator="EQUALS", root_text="0")

    # @staticmethod
    # def has_value():
    #     return Condition(name="Color_Preference", operator="HAS_VALUE")
