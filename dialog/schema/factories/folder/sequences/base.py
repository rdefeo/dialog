from dialog.elements import Folder
from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.inputs import FavoritesInput, DetailsInput, MainSearchCriteriaInput

__author__ = 'robdefeo'


class BaseSequences:
    @staticmethod
    def create():
        return Folder(
            label="BASE SEQUENCES",
            _id="folder_base_sequences",
            children=[
                GreetingAction.reset(),
                SmallTalkAction.set_to_zero(),
                FavoritesInput.create(),
                DetailsInput.create(),
                # ShowtimesInput.create(),
                MainSearchCriteriaInput.create()
            ]
        )
