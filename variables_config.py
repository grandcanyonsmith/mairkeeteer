from configparser import ConfigParser

config = ConfigParser()


def create_config():
    config["OPENAI"] = {
        "OPENAI_API_KEY": "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",
        "OPENAI_ENGINE": "text-davinci-003",
    }

    config["PATHS"] = {
        "BACKGROUND_INFORMATION_FILE_PATH": "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/examples/background_information.jsonl",
        "TEMPORARY_FILE_PATH": "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl",
        "HOOKS_EXAMPLES_FILE_PATH": "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/examples/hook_examples.jsonl",
    }

    with open("config.ini", "w") as configfile:
        return config.write(configfile)


def get_config():
    config.read("config.ini")
    return config
