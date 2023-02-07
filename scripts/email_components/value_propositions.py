import json
import sys

# Adds higher directory to python modules path.
sys.path.append("../..")

# Imports from scripts.utils
from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import (
    append_key_value_to_json_file,
    get_key_values_from_temp_json_file,
    _openai_response,
)
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


class ValuePropositionCreator:
    """Creates value propositions for emails."""

    def __init__(self):
        self.formatter = StringFormatter()

    def create_value_propositions(
        self, background_info, desired_outcome, step, total_steps
    ):
        """
        Creates value propositions for emails.

        Args:
            background_info (str): Background information.
            desired_outcome (str): Desired outcome.
            step (int): Step in the email sequence.
            total_steps (int): Total number of emails in the sequence.

        Returns:
            list: List of value propositions.
        """
        prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{total_steps}\n"""\n\nStep:\n"""\n{step}\n"""\n\nWhat should the value proposition be for this email?\n"""\n''',
        response = _openai_response(prompt)
        return self.formatter.format_everything(response.split("\n"))


if __name__ == "__main__":
    # Path to temp json file
    TEMP_JSON_FILE = "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl"

    # Create ValuePropositionCreator object
    value_proposition_creator = ValuePropositionCreator()

    # Background information
    background_info = "\n".join(
        [
            "I sell online courses that teach people how to sell online courses",
            "It is called Course Creator Pro",
        ]
    )

    # Desired outcome
    desired_outcome = "\n".join(
        [
            "People just watched my webinar",
            "I want to send them an email sequence that will get them to buy my course",
        ]
    )

    # Get steps from temp json file
    steps = get_key_values_from_temp_json_file("step")
    print(len(steps))

    # Create value propositions
    value_propositions = []
    for step in steps:
        value_propositions += value_proposition_creator.create_value_propositions(
            background_info, desired_outcome, step, len(steps)
        )
    print(value_propositions)

    # Append value propositions to temp json file
    append_key_value_to_json_file(
        "value_proposition", value_propositions, TEMP_JSON_FILE
    )