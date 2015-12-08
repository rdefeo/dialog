from os.path import join, dirname

import tornado.web
import tornado.options
from tornado.web import url

# from web.handlers import IndexHandler, DetailProductIdHandler, DetailSequenceHandler, ResultsHandler, BoringStuffHandler
from watson_developer_cloud import DialogV1 as Dialog
from dialog.handlers.init_chat import InitChat
from dialog.handlers.conversation import Conversation
from dialog.settings import WATSON_USERNAME, WATSON_PASSWORD, WATSON_DIALOG_ID


class Application(tornado.web.Application):
    def __init__(self):
        dialog_service = Dialog(
            username=WATSON_USERNAME,
            password=WATSON_PASSWORD
        )
        dialog_id = WATSON_DIALOG_ID

        # # CREATE A DIALOG
        # with open(join(dirname(__file__), '../dialog_files/jemboo-dialog-file.xml')) as dialog_file:
        #     create_dialog_response = dialog_service.update_content(dialog_file=dialog_file, name='jemboo-dialog')

        # UPDATE A DIALOG
        # with open(join(dirname(__file__), '../dialog_files/jemboo-dialog-file.xml')) as dialog_file:
        #
        #     create_dialog_response = dialog_service.update_dialog(dialog_file=dialog_file, dialog_id=dialog_id)


        handlers = [
            url(r"/api/bluemix/initChat", InitChat, dict(dialog_service=dialog_service, dialog_id=dialog_id),
                name="root"),
            url(r"/api/bluemix/postConversation", Conversation,
                dict(dialog_service=dialog_service, dialog_id=dialog_id), name="conversation"),
            (r'/()', tornado.web.StaticFileHandler, {'path': "static/index.html"}),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': "static/"}),
            # (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),

        ]

        settings = dict(
            template_path=join(dirname(__file__), "../templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "../static"),
            debug=tornado.options.options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
