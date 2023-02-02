#!/usr/bin/env python3

import os
import openai

from information.company_information import CompanyInformation
from information.customer_information import CustomerInformation
from information.email_sequence_information import EmailSequenceInformation

from email_components.hooks import Hooks

openai.api_key = os.getenv("OPENAI_API_KEY")


def format_background_info(
    company_information, customer_information, email_sequence_information, email_prompt
):
    return f"""
    Company Information
    Name: {company_information.name}
    Company Name: {company_information.company_name}
    Product Name: {company_information.product_name}
    Product Description: {company_information.product_description}

    Customer Information
    Desires: {customer_information.desires}
    Target Audience: {customer_information.target_audience}
    Pains: {customer_information.pains}
    Target Demographic: {customer_information.target_demographic}

    Email Sequence Information
    Number of Emails: {email_sequence_information.number_of_emails}
    Type of Email Sequence: {email_sequence_information.type_of_email_sequence}
    Sequence Purpose: {email_sequence_information.sequence_purpose}
    {email_prompt}
    """


def generate_email(email_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=email_prompt,
        max_tokens=1000,
        temperature=0.7,
        top_p=0,
        n=1,
    )
    return response["choices"][0]["text"]


def create_prompt_for_openai_to_generate_prompt(
    company_information, customer_information, email_sequence_information
):
    prompt = """
    Using the information above, generate a prompt that will be used downstream for another AI to complete the task of creating an email sequence.
    """
    format_background_info(
        company_information, customer_information, email_sequence_information, prompt
    )
    email_prompt = generate_email(prompt)
    return email_prompt.replace("\n", " ")  # strip newlines


def create_email_sequence(
    company_information, customer_information, email_sequence_information, prompt
):
    email_prompt = format_background_info(
        company_information, customer_information, email_sequence_information, prompt
    )
    return generate_email(email_prompt)


def intialize_background_info():
    company_information = CompanyInformation()
    customer_information = CustomerInformation()
    email_sequence_information = EmailSequenceInformation()
    return company_information, customer_information, email_sequence_information


def create_hooks(company_information, customer_information, email_sequence_information):
    hooks = Hooks()
    return hooks.create_new_hooks(
        company_information,
        customer_information,
        email_sequence_information,
    )


def create_sequence(
    company_information, customer_information, email_sequence_information
):
    prompt = create_prompt_for_openai_to_generate_prompt(
        company_information, customer_information, email_sequence_information
    )
    email_sequence = create_email_sequence(
        company_information, customer_information, email_sequence_information, prompt
    )
    print(email_sequence)


def main():
    (
        company_information,
        customer_information,
        email_sequence_information,
    ) = intialize_background_info()
    hooks = create_hooks(
        company_information, customer_information, email_sequence_information
    )
    print(hooks)
    create_sequence(
        company_information, customer_information, email_sequence_information
    )


if __name__ == "__main__":
    main()
