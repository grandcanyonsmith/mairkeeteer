import sys
import json
import os

sys.path.append("../..")  # Adds higher directory to python modules path.

from scripts.utils.get_values import get_hooks_examples_from_file
from scripts.utils.get_values import (
    get_key_values_from_temp_json_file,
    append_key_value_to_json_file,
    _openai_response,
)
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation


import openai


class Hooks:
    def __init__(self):
        self.hooks = []
        self.hooks_examples = get_hooks_examples_from_file()
        self.email_number = self.count_hooks() + 1

    def create_new_hooks(self, company_info, customer_info, email_sequence_info):
        print("Creating new hooks...")

        prompt = f"""
        Example Hooks for a course that teaches you how to tune your car
        {self.hooks_examples}





        Company Information:
        Name: {company_info.name}
        Company Name: {company_info.company_name}
        Product Name: {company_info.product_name}
        Product Description: {company_info.product_description}





        Background Information:
        Desires: {customer_info.desires}
        Target Audience: {customer_info.target_audience}
        Pains: {customer_info.pains}
        Target Demographic: {customer_info.target_demographic}


        We are going to create a {email_sequence_info.type_of_email_sequence} email {email_sequence_info.sequence_purpose}. There are a total of {email_sequence_info.number_of_emails} emails in this sequence. This is email number {self.email_number}.
        In this email, we are going to {email_sequence_info.sequence_purpose}. Write a hook that we will use for the subject line of the email. The hook should be written in a way that will get the target audience to do the desired outcome. The desired outcome is {email_sequence_info.sequence_purpose}.
        Write a 12-15 word hook that will be used to get your target audience to do the desired outcome:
        """
        print(prompt)
        return _openai_response(prompt)

    def count_hooks(self):
        return len(self.hooks)

    def main(self):
        temp_json_file = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/temp/temp.jsonl"
        company_info = CompanyInformation()
        customer_info = CustomerInformation()
        email_sequence_info = EmailSequenceInformation()
        steps = range(1, email_sequence_info.number_of_emails + 1)
        for step in steps:
            self.hooks.append(
                self.create_new_hooks(company_info, customer_info, email_sequence_info)
            )
            self.email_number += 1
        append_key_value_to_json_file("hook", self.hooks, temp_json_file)


if __name__ == "__main__":
    hooks = Hooks()
    hooks.main()
    print(hooks)