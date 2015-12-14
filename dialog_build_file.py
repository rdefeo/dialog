from os.path import join
from os.path import dirname
from time import sleep
from xml.etree import cElementTree as ET

from dialog.schema.root import Dialog
from dialog.schema.helper import dict_to_etree


def build():
    dialog_schema = Dialog().create()

    dialog_string = ET.tostring(dict_to_etree(dialog_schema))

    with open(join(dirname(__file__), 'dialog_files/jemboo-dialog-file.xml'), mode="w") as dialog_file:
        dialog_file.write(dialog_string.decode("utf-8"))
        dialog_file.close()

    print("file built")


if __name__ == "__main__":
    build()
