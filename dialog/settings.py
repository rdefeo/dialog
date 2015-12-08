import os


def get_env_setting(env_variable_name, default):
    if env_variable_name in os.environ:
        return os.environ[env_variable_name]
    else:
        return default


WATSON_USERNAME = get_env_setting("WATSON_USERNAME", "USERNAME")
WATSON_PASSWORD = get_env_setting("WATSON_PASSWORD", "PASSWORD")
WATSON_DIALOG_ID = get_env_setting("WATSON_DIALOG_ID", "DIALOG_ID")
