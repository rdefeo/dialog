from dialog.process.response import ProcessResponse


class ActionProcessResponse(ProcessResponse):
    def __init__(self, var_name, var_value):
        self.var_value = var_value
        self.var_name = var_name
