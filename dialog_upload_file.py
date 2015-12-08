from os.path import join, dirname

from dialog.settings import WATSON_USERNAME, WATSON_PASSWORD, WATSON_DIALOG_ID
from watson_developer_cloud import DialogV1 as Dialog

dialog_service = Dialog(
    username=WATSON_USERNAME,
    password=WATSON_PASSWORD
)
dialog_id = WATSON_DIALOG_ID

with open(join(dirname(__file__), 'dialog_files/jemboo-dialog-file.xml'), mode="r") as dialog_file:
    dialog_service.update_dialog(dialog_file=dialog_file, dialog_id=dialog_id)


print("done")