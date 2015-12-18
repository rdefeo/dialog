from unittest import TestCase

from dialog.elements import Flow, Folder

from dialog.elements.dialog import Dialog as Target


class init_Tests(TestCase):
    maxDiff = None

    def test_regular(self):
        actual = Target(Flow())

        self.assertEqual(
            actual,
            actual.flow.dialog
        )
