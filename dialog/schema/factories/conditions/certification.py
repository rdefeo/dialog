from dialog.schema.elements import If, Condition, Goto

__author__ = 'robdefeo'


class CertificationsConditions:
    @staticmethod
    def is_blank():
        return Condition(name="Certification_Preference", operator="IS_BLANK")
