from unittest import TestCase
from unittest.mock import Mock

from dialog.elements import Folder
from dialog.elements.dialog import Dialog
from dialog.elements.flow import Flow as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(
            folders=[
                Folder(children=[Mock()]),
                Folder(children=[Mock()])
            ]
        )

        dialog = Dialog(
            flow=actual
        )

        self.assertEqual(
            dialog,
            actual.folders[0].dialog
        )
        self.assertEqual(
            dialog,
            actual.folders[1].dialog
        )
