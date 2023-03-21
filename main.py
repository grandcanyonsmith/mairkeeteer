import openai

from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import get_background_information_file_path, _openai_response


class EmailSequence:
    def __init__(self, background_information, desired_outcome, number_of_emails):
        self.background_information = background_information
        self.desired_outcome = desired_outcome
        self.number_of_emails = number_of_emails
        self.steps = []

    def create_steps(self):
        # Create the prompt for OpenAI
        prompt = (
            f"Background information:\n"
            f'"""\n{self.background_information}\n"""\n\n'
            f"Desired Outcome:\n"
            f'"""\n{self.desired_outcome}\n"""\n\n'
            f"Number of emails in the email sequence:\n"
            f'"""\n{self.number_of_emails}\n"""\n\n'
            f"Steps in email sequence\n"
            f'"""\n'
        )
        
        # Get OpenAI response
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

    # Create email sequence
    email_sequence = EmailSequence(
        background_information, desired_outcome, number_of_emails
    )
    steps = email_sequence.create_steps()
    
    # Format the steps
    formatter = StringFormatter()
    steps = formatter.format_everything(steps)
    
    # Print the formatted steps
    print("Steps:", steps)
