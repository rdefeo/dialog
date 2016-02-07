from unittest import TestCase
from unittest.mock import Mock

from dialog.elements import Flow, Folder

from dialog.elements.dialog import Dialog as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(Flow(folders=[Mock()]))

        self.assertEqual(
            actual,
            actual.flow.dialog
        )
