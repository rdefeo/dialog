from dialog.elements.output import Output
from dialog.elements.default import Default
from dialog.elements.element import Element
from dialog.elements.search import Search
from dialog.runners.conversation import Conversation
from typing import Iterable


class Folder(Element):
    from dialog.elements.dialog import Dialog
    _element_name = "folder"

    def __init__(self, _id: str = None, label: str = None, selection_type=None, children: Iterable[Element] = None):
        """
        Node groups content.
        :param _id: Specifies a unique ID that is used as an anchor point.
        :param label: Specifies a unique name for a node.
        :param children: action | autoLearnVariations | concept | default | folder | function | getUserInput | goto | if | input | output | random | search
        """
        settings = {}
        if selection_type is not None:
            settings["selection_type"] = selection_type
        if label is not None:
            settings["label"] = label
        if _id is not None:
            settings["id"] = _id

        super().__init__(settings, list(children if children is not None else []))

    def _set_dialog(self, value):
        self.dialog = value
        if "id" in self.settings:
            self.dialog.ref_ids[self.settings["id"]] = self
        for child in iter(self.children):
            child._set_dialog(value)

    def create(self):
        doc = {}

        if "id" in self.settings:
            doc["@id"] = self.settings["id"]

        if "label" in self.settings:
            doc["@label"] = self.settings["label"]

        if "selection_type" in self.settings:
            doc["@selectionType"] = self.settings["selection_type"]

        if any(self.children):
            for i, child in enumerate(self.children):
                assert not isinstance(child, dict), child
                doc[(i, child._element_name)] = child

        return doc

    def run(self, conversation: Conversation):
        conversation.flow_position.append(self._id)
        goto_position = conversation.get_first_goto_position(self)
        if goto_position is not None:
            if goto_position == self._id:
                goto_position = conversation.get_first_goto_position(self)
            else:
                raise Exception()
        print("start_folder_runner,_id=%s" % (self._id))
        for index, child in enumerate(self.children):

            if goto_position is None or index >= goto_position:
                conversation.flow_position.append(index)
                if isinstance(child, Output):
                    child.run(conversation)
                elif isinstance(child, Search):
                    child.run(conversation)
                elif isinstance(child, Default):
                    child.run(conversation)
                else:
                    raise NotImplementedError(type(child))

                conversation.flow_position.pop()

        conversation.flow_position.pop()