import json
import sys

# Add higher directory to python modules path
sys.path.append("../..")

# Import from scripts.utils
from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import (
    append_key_value_to_json_file,
    get_key_values_from_temp_json_file,
    _openai_response,
)

from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation


class ValuePropositionCreator:
    """Creates value propositions for emails."""

    def __init__(self, company_information, customer_information):
        self.formatter = StringFormatter()
        self.company_information = company_information
        self.customer_information = customer_information

    def create_value_propositions(self, step: int, total_steps: int):
        """
        Creates value propositions for emails.

        Args:
            step (int): Step in the email sequence.
            total_steps (int): Total number of emails in the sequence.

        Returns:
            list: List of value propositions.
        """
        prompt = f'''Company Information:\n"""\n{self.company_information}\n"""\n\nCustomer Information:\n"""\n{self.customer_information}\n"""\n\nStep:\n"""\n{step}\n"""\n\nTotal steps:\n"""\n{total_steps}\n"""\n\nCreate a value proposition for this email\n"""\n'''
        response = _openai_response(prompt)
        return self.formatter.format_everything(response.split("\n"))


if __name__ == "__main__":
    TEMP_JSON_FILE = "/Users/canyons/mairkeeteer/files/data/temp/temp_email.jsonl"
    company_information = CompanyInformation()
    customer_information = CustomerInformation()
    value_prop_creator = ValuePropositionCreator(company_information, customer_information)
    desired_outcome = "I want to sell my product"
    step = 1
    total_steps = 5
    value_propositions = value_prop_creator.create_value_propositions(step, total_steps)
    print(value_propositions)