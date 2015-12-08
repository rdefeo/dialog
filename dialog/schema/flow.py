from dialog.schema.factories.folder.main import MainFolder
from dialog.schema.folder import LibraryFolder
from dialog.schema.factories.folder.concept import ConceptFolder
from dialog.schema.factories.folder.global_folder import GlobalFolder


class Flow:
    def create(self):
        return {
            "folder": [
                MainFolder.create(),
                LibraryFolder().create(),
                GlobalFolder.create(),
                ConceptFolder.create()

            ]
        }
