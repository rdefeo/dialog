from dialog.elements import Folder
from dialog.schema.factories.folder.library import LibraryFolder
from dialog.schema.factories.folder.main import MainFolder
from dialog.schema.factories.folder.concept import ConceptFolder
from dialog.schema.factories.folder._global import GlobalFolder


class Flow:
    def create(self):
        return Folder(
            children=[
                MainFolder.create(),
                LibraryFolder.create(),
                GlobalFolder.create(),
                ConceptFolder.create()
            ]
        )
