from unittest import TestCase
from unittest.mock import Mock

from dialog.elements import Folder, Input, Output, Goto
from dialog.elements.folder import Folder as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(
            children=[
                Input(
                    Mock(),
                    children=[Mock()]
                ),
                Output(Mock(), children=[Mock()]),
                Goto()
            ]
        )

        folder = Folder(
            children=[actual]
        )
        dialog = Mock()
        folder._set_dialog(dialog)

        self.assertEqual(
            dialog,
            actual.children[0].dialog
        )
        self.assertEqual(
            dialog,
            actual.children[1].dialog
        )
        self.assertEqual(
            dialog,
            actual.children[2].dialog
        )
