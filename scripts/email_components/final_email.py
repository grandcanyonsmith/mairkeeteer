# {"step": "Reminder of items left in cart - this email should remind the customer of the items they left in their shopping cart and encourage them to complete their purchase.", "step_number": 1, "hook": "\nDon't Miss Out! Complete Your Purchase Now.", "value_proposition": "The value proposition for this email should be that course creator pro is the perfect solution for anyone looking to create and sell their own online courses. it provides step-by-step guidance and support to help you get started quickly and easily. plus, with our money-back guarantee, you can be sure that you're making a safe investment."}
import json
import sys

import openai

sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import (_openai_response,
                                      append_key_value_to_json_file,
                                      get_key_values_from_temp_json_file)
from scripts.utils.openai_secret_manager import \
    OpenAiSecretManager as openai_secret_manager

temp_json_file = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
# This class is used to create the final email
class FinalEmailCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_final_email(self, step, hook, value_proposition, call_to_action):
        prompt = f'''Step in email sequence\n"""\n{step}\n"""\n\nHook:\n"""\n{hook}\n"""\n\nValue Proposition:\n"""\n{value_proposition}\n"""\n\nFinal Email\n"""\n'''
        return _openai_response(prompt)

    def create_final_email_from_temp_json_file(self, temp_json_file):
        keys = ["step", "hook", "value_proposition", "call_to_action"]
        for key in keys:
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

    # convert to json
    def convert_to_json(self, final_email):
        print(final_email)
        return json.dumps({"Email": final_email})

    # add a new key value pair to the json file
    def append_to_file(self, final_email, temp_json_file):
        temp_json_file = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
        with open(temp_json_file, "a") as f:
            f.write(final_email)
            f.write("\n")


if __name__ == "__main__":
    temp_json_file = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
    final_email_creator = FinalEmailCreator()
    final_email = final_email_creator.create_final_email_from_temp_json_file(
        temp_json_file
    )
    print(final_email)
    # convert to json

    # write to file
    final_email = final_email_creator.convert_to_json(final_email)
    final_email = final_email_creator.append_to_file(final_email, temp_json_file)
