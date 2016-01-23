import re

from dialog.elements.dialog import Dialog
from dialog.elements.grammar_item import RegExGrammarItem, EntityRegExGrammarItem, EntityGrammarItem
from dialog.runners.conversation import Conversation


# class RegExGrammarItemRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, grammar_item: RegExGrammarItem):
#         matches = re.findall(grammar_item.pattern, conversation.user_input, grammar_item.flags)
#         if not any(matches):
#             return False
#         elif any(matches) and grammar_item.dynamic_field_assignments is None:
#             return True
#         elif len(matches) == len(grammar_item.dynamic_field_assignments):
#             assignments = zip(grammar_item.dynamic_field_assignments, matches)
#             conversation.current_input_context = {}
#             for key, value in assignments:
#                 conversation.current_input_context[key] = value
#             return True
#         else:
#             return False


# class EntityGrammarItemRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, grammar_item: EntityGrammarItem):
#         if grammar_item.entity_id not in dialog.entity_dict:
#             raise Exception()
#         entity_grammar = dialog.entity_dict[grammar_item.entity_id]
#         search_term = conversation.user_input.strip().lower()
#         if search_term in entity_grammar:
#             conversation.current_input_context = {
#                 grammar_item.dynamic_field_assignment: entity_grammar[search_term].value
#             }
#             return True
#         else:
#             return False


# class EntityRegExGrammarItemRunner:
#     @staticmethod
#     def run(dialog: Dialog, conversation: Conversation, grammar_item: EntityRegExGrammarItem):
#         matches = re.findall(grammar_item.pattern, conversation.user_input, grammar_item.flags)
#         if not any(matches):
#             return False
#         elif any(matches) and grammar_item.dynamic_field_assignments is None:
#             return True
#         elif len(matches) == len(grammar_item.dynamic_field_assignments):
#             assignments = zip(grammar_item.dynamic_field_assignments, matches)
#             current_input_context = {}
#             for key, value in assignments:
#                 current_input_context[key] = value
#
#             grammar_item.entity_id
#             conversation.current_input_context = current_input_context
#             return True
#         else:
#             return False
