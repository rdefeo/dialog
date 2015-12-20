from dialog.process import GrammarProcessResponse, ProcessRequest
from dialog.process.grammar_response import GrammarMatchType
from dialog.process.response import ProcessResponseStatus

__author__ = 'robdefeo'
from unittest import TestCase
from unittest.mock import Mock

from dialog.elements.action import Action as Target, ACTION_SET_TO_NO, ACTION_SET_TO_YES


class process_Tests(TestCase):
    maxDiff = None

    def\
            test_set_to_no(self):
        target = Target(varName="test_var_name", operator=ACTION_SET_TO_NO)
        process_request = Mock(spec=ProcessRequest)
        process_request.profile = {
            "test": False
        }
        actual = target.process(process_request)
        self.assertDictEqual(
            {'var_value': False, 'var_name': 'test_var_name'},
            actual.__dict__
        )
        self.assertDictEqual(
            {'test': False, 'test_var_name': False},
            process_request.profile
        )

    def test_set_to_yes(self):
        target = Target(varName="test_var_name", operator=ACTION_SET_TO_YES)
        process_request = Mock(spec=ProcessRequest)
        process_request.profile = {
            "test": False
        }
        actual = target.process(process_request)
        self.assertDictEqual(
            {'var_value': True, 'var_name': 'test_var_name'},
            actual.__dict__
        )
        self.assertDictEqual(
            {'test': False, 'test_var_name': True},
            process_request.profile
        )

