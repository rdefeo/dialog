from dialog.schema.factories.action import GreetingAction, SmallTalkAction
from dialog.schema.factories.inputs import FavoritesInput, DetailsInput, MainSearchCriteriaInput

__author__ = 'robdefeo'


class BaseSequences:
    @staticmethod
    def create():
        return {
            "@label": "BASE SEQUENCES",
            "@id": "folder_base_sequences",
            (0, "action"): [
                GreetingAction.create_reset(),
                SmallTalkAction.set_to_zero()
            ],
            (1, "input"): [
                FavoritesInput.create(),
                DetailsInput.create(),
                # ShowtimesInput.create(),
                MainSearchCriteriaInput.create()
            ]
        }
