import os
from configparser import ConfigParser

CONFIG_FILE_NAME = "config.ini"
config = ConfigParser()


def create_config():
    OPENAI_API_KEY = get_openai_api_key()
    config["OPENAI"] = {
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "OPENAI_ENGINE": "text-davinci-003",
    }

    config["PATHS"] = {
        # "BACKGROUND_INFORMATION_FILE_PATH": "/workspaces/mairkeeteer/files/data/data/background_information.jsonl",
        "BACKGROUND_INFORMATION_FILE_PATH": "/Users/canyons/mairkeeteer/files/data/data/background_information.jsonl",
        # "TEMPORARY_FILE_PATH": "/workspaces/mairkeeteer/files/data/temp/temp.jsonl",
        "TEMPORARY_FILE_PATH": "/Users/canyons/mairkeeteer/files/data/temp/temp.jsonl",
        # "HOOKS_EXAMPLES_FILE_PATH": "/workspaces/mairkeeteer/files/data/examples/hook_examples.jsonl",
        "HOOKS_EXAMPLES_FILE_PATH": "/Users/canyons/mairkeeteer/files/data/examples/hook_examples.jsonl",
        # "EMAIL_SEQUENCE_TYPES_FILE_PATH": "/workspaces/mairkeeteer/files/data/examples/email_sequence_types.jsonl",
        "EMAIL_SEQUENCE_TYPES_FILE_PATH": "/Users/canyons/mairkeeteer/files/data/examples/email_sequence_types.jsonl",
    }

    with open(CONFIG_FILE_NAME, "w") as configfile:
        return config.write(configfile)


def ask_user_for_openai_api_key():
    """
    Ask the user for the OpenAI API key.
    """
    config.read(CONFIG_FILE_NAME)
    return input("Please enter your OpenAI API key: ")
    

def get_openai_api_key():
    if not os.path.exists(CONFIG_FILE_NAME):
        return ask_user_for_openai_api_key()

def get_config():
    config.read(CONFIG_FILE_NAME)
    return config


if __name__ == "__main__" and not os.path.exists(CONFIG_FILE_NAME):
    create_config()
    
    
