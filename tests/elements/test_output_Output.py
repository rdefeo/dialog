from unittest import TestCase
from unittest.mock import Mock

from dialog.elements import Folder, Goto, Grammar, Action, Prompt
from dialog.elements.output import Output as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(
            Prompt(
                items=[Mock()]
            ),
            children=[
                Action("var_name_value", "operator_value"),
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
