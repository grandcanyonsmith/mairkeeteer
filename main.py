import logging
from typing import List

from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import _openai_response


def configure_logging():
    logging.basicConfig(level=logging.DEBUG)


class EmailSequence:
    """
    Represents an email sequence.

    Attributes:
        background_information (List[str]): A list of strings representing the background information.
        desired_outcome (List[str]): A list of strings representing the desired outcome.
        num_emails (int): The number of emails in the sequence.
        steps (List[str]): A list of strings representing the steps in the email sequence.
    """

    def __init__(self, background_information: List[str], desired_outcome: List[str], num_emails: int):
        self.background_information = background_information
        self.desired_outcome = desired_outcome
        self.num_emails = num_emails
        self.steps = self.create_steps()

    def create_steps(self) -> List[str]:
        """
        Creates steps in email sequence using OpenAI.

        Returns:
            List[str]: A list of strings representing the steps in the email sequence.
        """
        def create_prompt() -> str:
            return (
                f"Background information:\n"
                f'"""\n{"".join(self.background_information)}\n"""\n\n'
                f"Desired Outcome:\n"
                f'"""\n{"".join(self.desired_outcome)}\n"""\n\n'
                f"Number of emails in the email sequence:\n"
                f'"""\n{self.num_emails}\n"""\n\n'
                f"Steps in email sequence\n"
                f'"""\n'
            )

        def get_steps_from_openai(prompt: str) -> List[str]:
            try:
                steps_string = _openai_response(prompt)
                steps = steps_string.split("\n")
                return steps
            except Exception as e:
                logging.error(f"Error occurred while creating steps: {e}")
                return []

        prompt = create_prompt()
        steps = get_steps_from_openai(prompt)

        return steps


if __name__ == "__main__":
    configure_logging()

    background_information = [
        "I sell online courses that teach people how to sell online courses",
        "It is called Course Creator Pro",
    ]
    desired_outcome = [
        "People just watched my webinar",
        "I want them to sign up for another webinar",
    ]
    num_emails = 5

    # Create email sequence
    email_sequence = EmailSequence(background_information, desired_outcome, num_emails)

    # Format the steps
    formatter = StringFormatter()
    formatted_steps = formatter.format_everything(email_sequence.steps)

    # Log the formatted steps
    logging.debug("Formatted Steps: %s", formatted_steps)
