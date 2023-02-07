import sys
import json

sys.path.append("../..")  # Adds higher directory to python modules path.


from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import _openai_response, _add_steps_to_temp_json_file

from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation
from info import intialize_background_info, format_background_info


class EmailStepsCreator:
    def __init__(self):
        self.formatter = StringFormatter()
        self.email_count = 3  # default

    def create_steps(self):
        prompt = f'''
        Background information:
        """
        {self.background_info}
        """

        Desired Outcome:
        """
        {self.desired_outcome}
        """

        Number of emails in the email sequence:
        """
        {self.email_count}
        """

        Steps in email sequence:
        """
        '''
        response = _openai_response(prompt)
        steps = response.split("\n")
        return self.formatter.format_everything(steps)


if __name__ == "__main__":

    temp_json_file = "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl"

    email_sequence = EmailStepsCreator()

    (
        company_information,
        customer_information,
        email_sequence_information,
    ) = intialize_background_info()
    email_sequence.background_info = format_background_info(
        company_information, customer_information, email_sequence_information, ""
    )

    email_sequence.desired_outcome = "\n".join(
        [
            "I need an Abandoned Cart Sequence To remind customers of items they left in their shopping cart and encourage them to complete their purchase.",
        ]
    )

    steps = email_sequence.create_steps()

    _add_steps_to_temp_json_file(steps, temp_json_file)
