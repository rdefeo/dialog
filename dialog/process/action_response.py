from dialog.process.response import ProcessResponse, ProcessResponseStatus


class ActionProcessResponse(ProcessResponse):
    def __init__(self, var_name, var_value):
        super().__init__(ProcessResponseStatus.handled)
        self.var_value = var_value
        self.var_name = var_name
