from dialog.schema.elements import Goto
from dialog.schema.factories.action import GreetingAction, SmallTalkAction, RecencyPreferenceAction
from dialog.schema.factories.grammar import GenericGrammar
from dialog.schema.factories.inputs import FavoritesInput, DetailsInput, ShowtimesInput, MainSearchCriteriaInput
from dialog.schema.factories.profile_checks import GenrePreferenceProfileCheck, CertificationPreferenceProfileCheck

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
