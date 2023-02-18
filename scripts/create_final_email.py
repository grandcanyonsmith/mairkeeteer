import json
import sys

import openai


# from scripts.utils.formatter import StringFormatter
from utils.formatter import StringFormatter
from utils.get_values import (
    _openai_response,
    append_key_value_to_json_file,
    get_key_values_from_temp_json_file,
)
from utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)

temp_json_file = (
    "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
)


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

    # convert to json
    def convert_to_json(self, final_email):
        print(final_email)
        return json.dumps({"Email": final_email})

    # add a new key value pair to the json file
    def append_to_file(self, final_email, temp_json_file):
        with open(temp_json_file, "a") as f:
            f.write(final_email)
            f.write("\n")


if __name__ == "__main__":
    final_email_creator = FinalEmailCreator()
    final_email = final_email_creator.create_final_email_from_temp_json_file(
        temp_json_file
    )
    print(final_email)
    # convert to json

    # write to file
    final_email = final_email_creator.convert_to_json(final_email)
    final_email = final_email_creator.append_to_file(final_email, temp_json_file)
<<<<<<< HEAD


# # {"step": "Reminder of items left in cart - this email should remind the customer of the items they left in their shopping cart and encourage them to complete their purchase.", "step_number": 1, "hook": "\nDon't Miss Out! Complete Your Purchase Now.", "value_proposition": "The value proposition for this email should be that course creator pro is the perfect solution for anyone looking to create and sell their own online courses. it provides step-by-step guidance and support to help you get started quickly and easily. plus, with our money-back guarantee, you can be sure that you're making a safe investment."}
# import json
# import sys
# import logging
# import openai
# import jinja2

# # Add higher directory to python modules path.
# sys.path.append("../..")
# # Import formatter class to format the output for better readability
# from scripts.utils.formatter import StringFormatter
# # Import utils functions to get values from OpenAI Secret Manager and temp JSON file
# from scripts.utils.get_values import (
#     get_openai_response,
#     append_key_value_to_json_file,
#     get_key_values_from_temp_json_file,
# )
# # Import OpenAI Secret Manager to get the values from the temp JSON file
# from scripts.utils.openai_secret_manager import (
#     OpenAiSecretManager as openai_secret_manager,
# )

# # File path to temp JSON file
# temp_json_file = (
#     "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
# )

# # This class is used to create the final email
# class FinalEmailCreator:
#     def __init__(self):
#         # Initialize formatter, logger, and required parameters
#         self.formatter = StringFormatter()
#         self.logger = logging.getLogger()
#         self.required_params = ["step", "hook", "value_proposition", "call_to_action"]

#     # create the prompt to pass to OpenAI
#     def create_prompt(self, step, hook, value_proposition):
#         return f'''Step in email sequence\n"""\n{step}\n"""\n\nHook:\n"""\n{hook}\n"""\n\nValue Proposition:\n"""\n{value_proposition}\n"""\n\nFinal Email\n"""\n'''

#     # Get response from OpenAI
#     def get_openai_response(self, prompt):
#         return get_openai_response(prompt)

#     # Check if all required parameters are present in the temp JSON file
#     def check_required_parameters(self):
#         required_params_present = True
#         for param in self.required_params:
#             if get_key_values_from_temp_json_file(param) is None:
#                 required_params_present = False
#                 self.logger.error(f"Error creating final email: Missing required parameter {param}")
#         return required_params_present

#     # Create the final email using jinja2 templating library
#     def create_final_email_from_template(self, temp_json_file):
#         # Get values from json file
#         json_values = []
#         for key in self.required_params:
#             value = get_key_values_from_temp_json_file(key)
#             if value is None:
#                 value = self.get_value_from_user(key)
#                 append_key_value_to_json_file(key, value, temp_json_file)
#             json_values.append(value)

#         # Create the final email using jinja2 templating library
#         template = jinja2.Template("""Step in email sequence:\n"""\n{{step}}\n"""\n\nHook:\n"""\n{{hook}}\n"""\n\nValue Proposition:\n"""\n{{value_proposition}}\n"""\n\nCall To Action:\n"""\n{{call_to_action}}\n"""\n\nFinal Email\n"""\n""")
#         return template.render(step=json_values[0], hook=json_values[1], value_proposition=json_values[2], call_to_action=json_values[3])

#     # Add a new key value pair to the json file
#     def append_key_value_to_file(self, final_email, temp_json_file):
#         try:
#             with open(temp_json_file, "a") as f:
#                 f.write(final_email)
#                 f.write("\n")
#         except Exception as e:
#             self.logger.error(f"Error appending to file: {e}")
#             raise e

#     # Convert to json
#     def convert_to_json(self, final_email):
#         return json.dumps({"Email": final_email})

#     # Format the output for better readability
#     def format_output(self, final_email):
#         return self.formatter.format_output(final_email)

# if __name__ == "__main__":
#     temp_json_file = (
#         "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
#     )
#     final_email_creator = FinalEmailCreator()
#     try:
#         # Check if all required parameters are present in the temp JSON file
#         if final_email_creator.check_required_parameters():
#             # Create prompt to pass to OpenAI
#             prompt = final_email_creator.create_prompt(
#                 get_key_values_from_temp_json_file("step"),
#                 get_key_values_from_temp_json_file("hook"),
#                 get_key_values_from_temp_json_file("value_proposition")
#             )
#             # Get response from OpenAI
#             final_email = final_email_creator.get_openai_response(prompt)
#             # Create the final email using jinja2 templating library
#             final_email = final_email_creator.create_final_email_from_template(temp_json_file)
#     except Exception as e:
#         final_email_creator.logger.error(f"Error creating final email from template: {e}")
#     else:
#         # Format the output for better readability
#         final_email = final_email_creator.format_output(final_email)
#         # Convert to json
#         final_email = final_email_creator.convert_to_json(final_email)
#         # Write to file
#         try:
#             final_email = final_email_creator.append_key_value_to_file(final_email, temp_json_file)
#         except Exception as e:
#             final_email_creator.logger.error(f"Error appending to file: {e}")
#         else:
#             print(final_email)
=======
>>>>>>> ac8678a8a1b0520cdbf89b558930048ee25cf6d5
