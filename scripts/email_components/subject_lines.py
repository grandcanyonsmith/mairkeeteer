import openai
import sys
import logging

# Adds higher directory to python modules path.
sys.path.append("../..")

# Imports functions from scripts.utils.get_values
from scripts.utils.get_values import (
    get_hooks_examples_from_file,
    get_key_values_from_temp_json_file,
    append_key_value_to_json_file,
    _openai_response,
)

# Imports StringFormatter class from scripts.utils.formatter
from scripts.utils.formatter import StringFormatter


# Creates a class to create subject lines
class SubjectLineCreator:
    # Initializes the class
    def __init__(self):
        self.formatter = StringFormatter()

    # Creates subject lines based on background info, desired outcome, step, and total steps
    def create_subject_lines(
        self,
        background_info: str,
        desired_outcome: str,
        step: int,
        total_steps: int,
    ) -> str:
        """
        Creates subject lines based on background info, desired outcome, step, and total steps.

        Parameters:
        background_info (str): Background information.
        desired_outcome (str): Desired outcome.
        step (int): Step.
        total_steps (int): Total steps.

        Returns:
        str: Formatted subject lines.
        """
        logging.info("Creating subject lines")
        try:
            prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nStep:\n"""\n{step}\n"""\n\nTotal steps:\n"""\n{total_steps}\n"""\n\nCreate a subject line for this email\n"""\n'''
            response = _openai_response(prompt)
            formatted_response = self.formatter.format_everything(response.split("\n"))
            logging.info("Subject lines created")
            return formatted_response
        except Exception as e:
            logging.error(e)
            raise

    def main(self, background_info: str, desired_outcome: str) -> str:
        logging.info("Starting main function")
        steps = get_key_values_from_temp_json_file("step")

        for step in steps:
            subject_lines = self.create_subject_lines(
                background_info, desired_outcome, step, len(steps)
            )
            for subject_line in subject_lines:
                print(subject_line)
        logging.info("Main function finished")


if __name__ == "__main__":
    subject_lines_creator = SubjectLineCreator()
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
    try:
        subject_lines_creator.main(background_info, desired_outcome)
    except Exception as e:
        logging.error(e)
        raise
