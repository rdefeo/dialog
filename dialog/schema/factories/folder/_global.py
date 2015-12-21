from dialog.elements import Folder
from dialog.elements.search import Search


class GlobalFolder:
    @staticmethod
    def create():
        return Folder(
            label="Global",
            children=[
                Search(
                    ref="folder_global_sequences"
                )
            ]
        )
