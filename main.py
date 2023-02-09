import openai

from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import get_background_information_file_path
from scripts.utils.get_values import _openai_response


class EmailSequence:
    def __init__(self, background_information, desired_outcome, number_of_emails):
        self.background_information = background_information
        self.desired_outcome = desired_outcome
        self.number_of_emails = number_of_emails

        self.steps = []

    def create_steps(self):
        prompt = f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence\n"""\n'''  # noqa
        steps_text = _openai_response(prompt)
        self.steps = steps_text.split("\n")
        return self.steps


if __name__ == "__main__":
    background_information = [
        "I sell online courses that teach people how to sell online courses",
        "It is called Course Creator Pro",
    ]
    desired_outcome = [
        "People just watched my webinar",
        "I want them sign up for another webinar",
    ]
    number_of_emails = 5

    email_sequence = EmailSequence(
        background_information, desired_outcome, number_of_emails
    )
    steps = email_sequence.create_steps()
    formatter = StringFormatter()
    steps = formatter.format_everything(steps)
    print("Steps:", steps)
