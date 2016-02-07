from unittest import TestCase

from dialog.elements.grammar_item import RegExGrammarItem
from dialog.runners.conversation import Conversation
from dialog.runners.grammar_item import RegExGrammarItemRunner as Target
from mock import Mock


class run_Tests(TestCase):
    maxDiff = None

    def test_exact_match(self):
        conversation = Conversation()
        conversation.user_input = "my name is Rob"
        actual = Target.run(
            Mock(),
            conversation,
            RegExGrammarItem(pattern=r"My name is (\w+)", dynamic_field_assignments=["user_known_as"])
        )
        self.assertTrue(actual)
        self.assertDictEqual(
            {'user_known_as': 'Rob'},
            conversation.current_input_context
        )

    def test_trailing_match(self):
        conversation = Conversation()
        conversation.user_input = "hi my name is Rob"
        actual = Target.run(
            Mock(),
            conversation,
            RegExGrammarItem(pattern=r"\w*My name is (\w+)", dynamic_field_assignments=["user_known_as"])
        )
        self.assertTrue(actual)
        self.assertDictEqual(
            {'user_known_as': 'Rob'},
            conversation.current_input_context
        )
