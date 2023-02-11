import sys
import json
import os
import logging

# Add higher directory to python modules path
sys.path.append("../..")

# Import necessary functions
from scripts.utils.get_values import get_hooks_examples_from_file
from scripts.utils.get_values import (
    get_key_values_from_temp_json_file,
    append_key_value_to_json_file,
    _openai_response,
    get_hooks_examples_from_file,
    get_openai_api_key,
)

# Import necessary classes
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation

# Import OpenAI
import openai

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define constants
TEMP_JSON_FILE = "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl"


# Define Hooks class
class HookGenerator:
    """Class to generate hooks for email subject lines"""

    def __init__(self) -> None:
        self.hooks: List[str] = []
        self.hooks_examples: str = get_hooks_examples_from_file()
        self.email_number: int = self.count_hooks() + 1

    # Count hooks
    def count_hooks(self) -> int:
        """Count the number of hooks

        Returns:
            int: Number of hooks
        """
        return len(self.hooks)

    # Create new hooks
    def generate_new_hook(
        self,
        company_info: CompanyInformation,
        customer_info: CustomerInformation,
        email_sequence_info: EmailSequenceInformation,
    ) -> str:
        """Create new hook"""

        logging.info("Generating new hook...")

        prompt: str = f"""
        Example Hooks for a course that teaches you how to tune your car:
        {self.hooks_examples}








        Company Information
        Product Name: {company_info.product_name}
        Product Description: {company_info.product_description}
        Common Mistake of Target Audience: {company_info.common_mistake}
        Ideal Customer: {company_info.ideal_market_avatar}








        Background Information
        Target Audience: {customer_info.target_audience}
        Pains: {customer_info.pains}
        Target Demographic: {customer_info.target_demographic}




        We are going to create a {email_sequence_info.type_of_email_sequence} email sequence for the purpose of {email_sequence_info.sequence_purpose}. 
        There are a total of {email_sequence_info.number_of_emails} emails in this sequence. 
        This is email number {self.email_number}. 
        In this email, we are going to {email_sequence_info.sequence_purpose}. 
        Write a hook that we will use for the subject line of the email. 
        The hook should be written in a way that will get the target audience to do the desired outcome. 
        The desired outcome is {email_sequence_info.sequence_purpose}. 
        Write a 12-15 word hook that will be used to get your target audience to do the desired outcome:
        """
        logging.info(prompt)
        return _openai_response(prompt)

    # Generate hooks
    def generate_hooks(
        self,
        company_info: CompanyInformation,
        customer_info: CustomerInformation,
        email_sequence_info: EmailSequenceInformation,
    ) -> None:
        """Generate hooks for email subject lines"""

        try:
            steps = range(1, int(email_sequence_info.number_of_emails) + 1)
            for step in steps:
                self.hooks.append(
                    self.generate_new_hook(
                        company_info, customer_info, email_sequence_info
                    )
                )
                self.email_number += 1
        except Exception as e:
            logging.error("An error occurred while generating hooks: %s", e)

    # Main function
    def generate_hooks_main(self) -> None:
        """Main function to generate hooks"""

        try:
            company_info = CompanyInformation()
            customer_info = CustomerInformation()
            email_sequence_info = EmailSequenceInformation()
            self.generate_hooks(company_info, customer_info, email_sequence_info)
            append_key_value_to_json_file("hook", self.hooks, TEMP_JSON_FILE)
        except Exception as e:
            logging.error("An error occurred while running the main function: %s", e)


# Run main function
if __name__ == "__main__":
    hook_generator = HookGenerator()
    hook_generator.generate_hooks_main()
    print(hook_generator)
