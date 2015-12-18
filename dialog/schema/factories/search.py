from dialog.elements import Goto

__author__ = 'robdefeo'


class PreliminarySequencesSearch:
    @staticmethod
    def _id():
        return "search_preliminary_sequences"

    @staticmethod
    def goto():
        return Goto(ref=PreliminarySequencesSearch._id())

    @staticmethod
    def create():
        from dialog.schema.factories.folder.sequences import PreliminarySequencesFolder

        return {
            "@id": PreliminarySequencesSearch._id(),
            "@ref": PreliminarySequencesFolder._id()
        }
