import json

import openai

from utils.formatter import StringFormatter
from utils.get_values import (
    _openai_response,
    append_key_value_to_json_file,
    get_key_values_from_temp_json_file,
)

TEMP_JSON_FILE = "/Users/canyons/mairkeeteer/files/data/temp/temp.jsonl"
KEYS = ["step", "hook", "value_proposition", "call_to_action"]


class FinalEmailCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_final_email(self, step, hook, value_proposition, call_to_action):
        prompt = f'Step in email sequence\n"""{step}"""\n\nHook:\n"""{hook}"""\n\nValue Proposition:\n"""{value_proposition}"""\n\nFinal Email\n"""'
        data = {"step": step, "hook": hook, "value_proposition": value_proposition, "call_to_action": call_to_action}
        with open(TEMP_JSON_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
        return _openai_response(prompt)

    def create_final_email_from_temp_json_file(self, TEMP_JSON_FILE):
        for key in KEYS:
            print(f"Getting {key} from temp json file")
            value = get_key_values_from_temp_json_file(key)
            if value is None:
                value = self.get_value_from_user(key)
                append_key_value_to_json_file(key, value, temp_json_file)
        step = get_key_values_from_temp_json_file("step")
        hook = get_key_values_from_temp_json_file("hook")
        value_proposition = get_key_values_from_temp_json_file("value_proposition")
        call_to_action = get_key_values_from_temp_json_file("call_to_action")
        return self.create_final_email(step, hook, value_proposition, call_to_action)

    def get_value_from_user(self, key):
        print(f"Please enter the {key} for this email")
        return input()

    def append_email_to_file(self, final_email, temp_json_file):
        with open(temp_json_file, "a") as f:
            f.write(final_email)
            f.write("\n")


if __name__ == "__main__":
    final_email_creator = FinalEmailCreator()
    final_email = final_email_creator.create_final_email_from_temp_json_file(
        TEMP_JSON_FILE
    )
    print(final_email)
    final_email = final_email_creator.append_email_to_file(final_email, TEMP_JSON_FILE)
