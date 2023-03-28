import sys
import json
import os
import logging
from typing import List, Tuple

# Add higher directory to python modules path
sys.path.append("../..")

# Import necessary functions
from scripts.utils.get_values import (
    get_hooks_examples_from_file,
    get_key_values_from_temp_json_file,
    append_key_value_to_json_file,
    _openai_response,
    get_openai_api_key,
)

# Import necessary classes
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation


# Define constants
TEMP_JSON_FILE = "/Users/canyons/mairkeeteer/files/data/temp/temp.jsonl"


class HookGenerator:
    """Class to generate hooks for email subject lines."""

    def __init__(self) -> None:
        self.hooks: List[str] = []
        self.hooks_examples: str = get_hooks_examples_from_file()
        self.email_number: int = self.count_hooks() + 1

    def count_hooks(self) -> int:
        """Count the number of hooks.

        Returns:
            int: Number of hooks.
        """
        return len(self.hooks)
    
    def generate_new_hook(self,
                          company_info: CompanyInformation, 
                          customer_info: CustomerInformation, 
                          email_sequence_info: EmailSequenceInformation, 
                          email_number: int) -> str:
        """Create a hook for a specific email in an email sequence."""
        
        # Format the prompt string using f-strings for readability
        prompt = f"""Example Hooks for a course that teaches you how to tune your car:
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
    This is email number {email_number}. 
    In this email, we are going to {email_sequence_info.sequence_purpose}. 
    Write a hook that we will use for the subject line of the email. 
    The hook should be written in a way that will get the target audience to do the desired outcome. 
    The desired outcome is {email_sequence_info.sequence_purpose}. 
    Write a 12-15 word hook that will be used to get your target audience to do the desired outcome:
    """
        
        # Log the prompt string for debugging purposes
        logging.debug(prompt)
        
        # Use the _openai_response function to generate a response using the prompt
        response = _openai_response(prompt)
        
        # Log the response string for debugging purposes
        logging.debug(response)
        
        # Return the response string
        return response


    def validate_company_info(self, company_info: CompanyInformation) -> Tuple[bool, str]:
        """Validate company information input."""
        # Validate the company information parameter
        if not isinstance(company_info, CompanyInformation):
            return False, "company_info must be a CompanyInformation object"
        elif not company_info.product_name or not company_info.product_description:
            return False, "product_name and product_description are required fields"
        else:
            return True, ""
        

    def validate_customer_info(self, customer_info: CustomerInformation) -> Tuple[bool, str]:
        """Validate customer_info input."""
        # Validate the customer information parameter
        if not isinstance(customer_info, CustomerInformation):
            return False, "customer_info must be a CustomerInformation object"
        elif not customer_info.target_audience or not customer_info.pains or not customer_info.target_demographic:
            return False, "target_audience, pains, and target_demographic are required fields"
        else:
            return True, ""

    def validate_email_sequence_info(self, email_sequence_info: EmailSequenceInformation) -> Tuple[bool, str]:
        """Validate email sequence information input."""
        # Validate the email sequence information parameter
        if not isinstance(email_sequence_info, EmailSequenceInformation):
            return False, "email_sequence_info must be an EmailSequenceInformation object"
        elif not email_sequence_info.type_of_email_sequence or not email_sequence_info.sequence_purpose or not email_sequence_info.number_of_emails:
            return False, "type_of_email_sequence, sequence_purpose, and number_of_emails are required fields"
        else:
            return True, ""


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
                        company_info, customer_info, email_sequence_info, step
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
            with open(TEMP_JSON_FILE, "a") as f:
                for hook in self.hooks:
                    f.write(json.dumps({"hook": hook}) + "\n")
        except Exception as e:
            logging.error("An error occurred while running the main function: %s", e)

if __name__ == "__main__":
    hook_generator = HookGenerator()
    print(hook_generator.generate_hooks_main())