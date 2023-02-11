import sys
import logging
import openai

sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import (
    _openai_response,
    append_key_value_to_json_file,
    get_key_values_from_temp_json_file,
    get_temporary_file_path,
)
from scripts.utils.get_values import get_openai_api_key

logger = logging.getLogger(__name__)


class CallToActionCreator:
    """Creates call-to-actions (CTA) based on given information"""

    def __init__(self):
        """Initialize a CallToActionCreator object"""
        self.formatter = StringFormatter()

    def generate_prompt(
        self, background_info, desired_outcome, step, total_steps, length=None
    ):
        """
        Generate a prompt for the OpenAI API

        Args:
        - background_info (str): Background information about the product/service
        - desired_outcome (str): The desired outcome of the email sequence
        - step (int): The current step in the email sequence
        - total_steps (int): The total number of steps in the email sequence
        - length (int, optional): The length of the generated prompt

        Returns:
        - str: The generated prompt
        """
        return (
            f'''Background information:\n"""\n{background_info[:length]}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome[:length]}\n"""\n\nNumber of emails in the email sequence:\n"""\n{total_steps}\n"""\n\nStep:\n"""\n{step}\n"""\n\nWhat should the call to action be?\n"""\n'''
            if length
            else f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{total_steps}\n"""\n\nStep:\n"""\n{step}\n"""\n\nWhat should the call to action be?\n"""\n'''
        )

    def create_call_to_action(
        self, background_info, desired_outcome, step, total_steps
    ):
        """
        Generates a call-to-action (CTA) based on the given information

        Args:
        - background_info (str): Background information about the product/service
        - desired_outcome (str): The desired outcome of the email sequence
        - step (int): The current step in the email sequence
        - total_steps (int): The total number of steps in the email sequence

        Returns:
        - list of str: A list of generated CTAs
        """
        try:
            prompt = self.generate_prompt(
                background_info, desired_outcome, step, total_steps
            )
            response = _openai_response(prompt)
            return self.formatter.format_everything(response.split("\n"))
        except Exception as e:
            # Log more detailed information when an error occurs
            logger.exception(
                f"An error occurred while generating the call-to-action. Error: {e}"
            )
            raise


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
        logger.info(f"Generating call-to-action for step {step} of {len(steps)}")
        call_to_actions = call_to_action_creator.create_call_to_action(
            background_info, desired_outcome, step, len(steps)
        )
        for call_to_action in call_to_actions:
            logger.info(f"Generated call-to-action: {call_to_action}")
            ctas.append(call_to_action)
            print(call_to_action)
    logger.info(f"Generated call-to-actions: {ctas}")
    temp_json_file = get_temporary_file_path()
    append_key_value_to_json_file("call_to_action", ctas, temp_json_file)
