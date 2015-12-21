from dialog.elements import Goto
from dialog.elements.search import Search

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

        return Search(
            _id=PreliminarySequencesSearch._id(),
            ref=PreliminarySequencesFolder._id()
        )
