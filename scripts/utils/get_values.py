import sys
import os
from pathlib import Path

import json
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)
import openai


def _openai_response(prompt):
    """
    Get the response from openai
    :param prompt: the prompt to send to openai
    :return: the response from openai
    """

    openai.api_key = openai_secret_manager.get_secret("openai")

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


def get_temporary_file_path():
    """
    Get the temporary file path
    :return: the temporary file path
    """
    return os.environ.get("TEMPORARY_FILE_PATH")


def get_background_information_file_path():
    """
    Get the background information file path
    :return: the background information file path
    """
    return os.environ.get("BACKGROUND_INFORMATION_FILE_PATH")


def get_key_values_from_temp_json_file(key):
    """
    Get the values from the temp json file
    :param key: the key of the value
    :return: the value
    """
    temp_file = get_temporary_file_path()
    with open(temp_file, "r") as f:
        steps = [json.loads(line) for line in f if key in json.loads(line)]
    return [step[key] for step in steps]


def get_background_information(info_name):
    """
    Open the background information file and
    return the info_name
    :param info_name: the name of the information
    :return: a list
    """
    return _get_data_from_file(get_background_information_file_path())[info_name]


def get_hooks_examples_from_file():
    """
    Open the hook examples file and
    return the hooks
    :return: a string of hooks
    """
    return "\n".join(
        json.loads(line)["hook"]
        for line in open(
            os.environ.get("HOOKS_EXAMPLES_FILE_PATH"),
            "r",
        )
    )


def _get_data_from_file(file_name):
    """
     Open a file and return the data
    :param file_name: the name of the file
    :return: the data of the file
    """
    return json.load(open(file_name))


def read_lines_from_file(file_path):
    """
    Read the lines from the file
    :param file_path: the file path
    :return: the lines
    """
    with open(file_path, "r") as f:
        return f.readlines()


def append_key_value_to_json_file(key, values, temp_json_file):
    """
    Append the key value to the json file
    :param key: the key
    :param values: the values
    :param json_file: the json file
    :return: None
    """

    with open(temp_json_file, "r") as f:
        steps = [json.loads(line) for line in f]

    for i, step in enumerate(steps):
        step[key] = values[i]

    with open(temp_json_file, "w") as f:
        for step in steps:
            f.write(json.dumps(step) + "\n")

def _add_steps_to_temp_json_file(steps, temp_json_file):
    """
    Add the steps to the temp json file
    :param steps: the steps
    :param temp_json_file: the temp json file
    :return: None
    """
    with open(temp_json_file, "w") as f:
        for i, step in enumerate(steps):
            f.write(json.dumps({"step": step, "step_number": i + 1}) + "\n")
    print(f"Wrote email steps to {temp_json_file}")
