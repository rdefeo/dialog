from dialog.elements import Goto
from dialog.elements.search import Search


class PreliminarySequencesSearch:
    @staticmethod
    def _id():
        return "search_preliminary_sequences"

    @staticmethod
    def goto():
        from dialog.schema.factories.inputs.how_can_i_help_you import folder_how_can_i_help_sequences
        return Goto(ref=folder_how_can_i_help_sequences.settings["id"])

    @staticmethod
    def create():
        from dialog.schema.factories.folder.sequences import PreliminarySequencesFolder

        return Search(
            _id=PreliminarySequencesSearch._id(),
            ref=PreliminarySequencesFolder._id()
        )
