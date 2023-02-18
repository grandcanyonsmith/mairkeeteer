import os
from configparser import ConfigParser

CONFIG_FILE_NAME = "config.ini"
config = ConfigParser()


def create_config():
    config["OPENAI"] = {
        "OPENAI_API_KEY": "",
        "OPENAI_ENGINE": "text-davinci-003",
    }

    config["PATHS"] = {
        "BACKGROUND_INFORMATION_FILE_PATH": "/workspaces/mairkeeteer/files/data/data/background_information.jsonl",
        "TEMPORARY_FILE_PATH": "/workspaces/mairkeeteer/files/data/temp/temp.jsonl",
        "HOOKS_EXAMPLES_FILE_PATH": "/workspaces/mairkeeteer/files/data/examples/hook_examples.jsonl",
        "EMAIL_SEQUENCE_TYPES_FILE_PATH": "/workspaces/mairkeeteer/files/data/examples/email_sequence_types.jsonl",
    }

    with open(CONFIG_FILE_NAME, "w") as configfile:
        return config.write(configfile)


def get_config():
    config.read(CONFIG_FILE_NAME)
    return config

<<<<<<< HEAD
if __name__ == "__main__" and not os.path.exists("config.ini"):
    create_config()
=======

if __name__ == "__main__" and not os.path.exists(CONFIG_FILE_NAME):
    create_config()
>>>>>>> ac8678a8a1b0520cdbf89b558930048ee25cf6d5
