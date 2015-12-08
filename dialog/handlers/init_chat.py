from tornado.web import RequestHandler
from watson_developer_cloud import DialogV1 as Dialog


class InitChat(RequestHandler):
    def initialize(self, dialog_service: Dialog, dialog_id):
        self.dialog_service = dialog_service
        self.dialog_id = dialog_id

    def on_finish(self):
        pass

    def get(self, *args, **kwargs):
        """
        Initializes chat with WDS This initiates the chat with WDS by requesting for a client id and conversation id(to be used in subsequent API calls) and a
        response message to be displayed to the user. If it's a returning user, it sets the First_Time profile variable to "No" so that the user is not taken
        through the hand-holding process.

        query_param firstTimeUser specifies if it's a new user or a returning user(true/false). If it is a returning user WDS is notified via profile var.

        :param args:
        :param kwargs:
        :return: a response containing either of these two entities- {@code WDSConversationPayload} or {@code ServerErrorPayload}
        """
        conversation = self.dialog_service.conversation(self.dialog_id)
        first_time_user = self.get_argument("firstTimeUser", True)
        if not first_time_user:
            self.dialog_service.update_profile(
                self.dialog_id,
                conversation["conversation_id"],
                [
                    {
                        "name": "First_Time",
                        "value": "No"
                    }
                ]
            )
        self.finish(
            {
                "conversationId": conversation["conversation_id"],
                "clientId": conversation["client_id"],
                "input": conversation["input"],
                "wdsResponse": " ".join(conversation["response"])
            }
        )
