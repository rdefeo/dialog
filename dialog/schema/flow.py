from dialog.schema.folder import ConceptFolder, GlobalFolder, MainFolder, LibraryFolder

__author__ = 'robdefeo'


class Flow:
    def create(self):
        return {
            "folder": [
                MainFolder().create(),
                LibraryFolder().create(),
                GlobalFolder().create(),
                ConceptFolder().create()

            ]
        }
