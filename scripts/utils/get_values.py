import sys
sys.path.append("../..")  # Adds higher directory to python modules path.
import json
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)
import openai

def get_background_information(info_name):
    """
    Open the background information file and
    return the info_name
    :param info_name: the name of the information
    :return: a list
    """
    return list(
        _get_data_from_file(
            "files/data/examples/background_information.jsonl"
        )[info_name].values()
    )  # Get the values of the info_name


def get_hooks_examples_from_file():
    """
    Open the hook examples file and
    return the hooks
    :return: a string of hooks
    """
    return "\n".join(
        json.loads(line)["hook"]
        for line in open(
            "files/data/examples/hook_examples.jsonl",
            "r",
        )
    )  # Get the hook of each line


def _get_data_from_file(file_name):
    """
     Open a file and return the data
    :param file_name: the name of the file
    :return: the data of the file
    """
    return json.load(open(file_name))


def append_key_value_to_temp_json_file(key, values):
    temp_file = "../../files/data/temp/temp.jsonl"
    with open(temp_file, "r") as f:
        steps = [json.loads(line) for line in f]
    for i, step in enumerate(steps):
        step[key] = values[i]
    with open(temp_file, "w") as f:
        for step in steps:
            f.write(json.dumps(step) + "\n")


def get_key_values_from_temp_json_file(key):
    temp_file = "../../files/data/temp/temp.jsonl"
    with open(temp_file, "r") as f:
        values = [json.loads(line)[key] for line in f]
    return values

def _openai_response(prompt):
    secrets = openai_secret_manager.get_secret("openai")
    openai.api_key = secrets
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
    )
    return response["choices"][0]["text"]
