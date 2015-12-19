from unittest import TestCase

from dialog.process import ProcessRequest
from dialog.process.grammar_response import GrammarMatchType
from dialog.elements.grammar import Grammar as Target


class process_Tests(TestCase):
    maxDiff = None

    def test_exact_match(self):
        target = Target(
            items=[
                "something",
                "oh no!"
            ]
        )

        actual = target.process(
            ProcessRequest("something", {})
        )
        self.assertEqual(
            GrammarMatchType.exact,
            actual.match_type
        )

    def test_none_match(self):
        target = Target(
            items=[
                "something",
                "oh no!"
            ]
        )

        actual = target.process(
            ProcessRequest("something", {})
        )
        self.assertEqual(
            GrammarMatchType.exact,
            actual.match_type
        )
