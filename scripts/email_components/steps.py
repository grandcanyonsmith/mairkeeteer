import openai
import sys
import json
import os

sys.path.append("../..")  # Adds higher directory to python modules path.


from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)
from scripts.utils.get_values import _openai_response


class EmailSequence:
    def __init__(self):
        self.background_info = "\n".join(
            [
                "I sell online courses that teach people how to sell online courses",
                "It is called Course Creator Pro",
            ]
        )
        self.desired_outcome = "\n".join(
            [
                "I need an Abandoned Cart Sequence To remind customers of items they left in their shopping cart and encourage them to complete their purchase.",
            ]
        )
        self.email_count = 3
        self.steps = []

    def create_steps(self):
        prompt = f'''Background information:\n"""\n{self.background_info}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.email_count}\n"""\n\nSteps in email sequence\n"""\n'''
        response = _openai_response(prompt)
        self.steps = response.split("\n")
        return formatter.format_everything(self.steps)


if __name__ == "__main__":
    formatter = StringFormatter()
    email_sequence = EmailSequence()
    steps = email_sequence.create_steps()

    temp_file = "temp.jsonl"

    with open(temp_file, "w") as f:
        for i, step in enumerate(steps):
            f.write(json.dumps({"step": step, "step_number": i + 1}) + "\n")
    print(f"Wrote email steps to {temp_file}")
