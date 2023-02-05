import openai
import sys
sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.get_values import (
   get_key_values_from_temp_json_file,
    append_key_value_to_temp_json_file, _openai_response
)
from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


class CallToActionCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_call_to_action(
        self, background_info, desired_outcome, step, total_steps
    ):
        prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{total_steps}\n"""\n\nStep:\n"""\n{step}\n"""\n\nWhat should the call to action be?\n"""\n'''
        response = _openai_response(prompt)
        return self.formatter.format_everything(response.split("\n"))


if __name__ == "__main__":
    call_to_action_creator = CallToActionCreator()
    background_info = "\n".join(
        [
            "I sell online courses that teach people how to sell online courses",
            "It is called Course Creator Pro",
        ]
    )
    desired_outcome = "\n".join(
        [
            "People just watched my webinar",
            "I want to send them an email sequence that will get them to buy my course",
        ]
    )
    steps = get_key_values_from_temp_json_file("step")
    ctas = []
    for step in steps:
        call_to_actions = call_to_action_creator.create_call_to_action(
            background_info, desired_outcome, step, len(steps)
        )
        for call_to_action in call_to_actions:
            print(call_to_action)
            ctas.append(call_to_action)

    print(ctas)

    append_key_value_to_temp_json_file("call_to_action", ctas)