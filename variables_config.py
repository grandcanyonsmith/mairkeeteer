import os
from configparser import ConfigParser

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

    with open("config.ini", "w") as configfile:
        return config.write(configfile)


def get_config():
    config.read("config.ini")
    return config

if __name__ == "__main__" and not os.path.exists("config.ini"):
    create_config()