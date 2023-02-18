# Import statements
import os
import openai

# Import classes and functions
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation
from scripts.email_components.hooks import HookGenerator

# Define functions

def format_background_info(company_information, customer_information, email_sequence_information, email_prompt):
    """
    Returns a formatted string that contains the background information for the email sequence.
    This information will be used to create the email prompt for OpenAI.
    """
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
    """
    Uses OpenAI's API to generate an email based on the given email prompt.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=email_prompt,
        max_tokens=1000,
        temperature=0.7,
        top_p=0,
        n=1,
    )
    return response["choices"][0]["text"]

def create_prompt_for_openai_to_generate_prompt(company_information, customer_information, email_sequence_information):
    """
    Creates a prompt for OpenAI to generate an email prompt based on the background information.
    """
    prompt = """
    Using the information above, generate a prompt that will be used downstream for another AI to complete the task of creating an email sequence.
    """
    format_background_info(company_information, customer_information, email_sequence_information, prompt)
    email_prompt = generate_email(prompt)
    return email_prompt.replace("\n", " ")  # strip newlines

def create_email_sequence(company_information, customer_information, email_sequence_information, prompt):
    """
    Creates an email sequence based on the background information and the email prompt.
    """
    email_prompt = format_background_info(company_information, customer_information, email_sequence_information, prompt)
    return generate_email(email_prompt)

def intialize_background_info():
    company_information = CompanyInformation()
    customer_information = CustomerInformation()
    email_sequence_information = EmailSequenceInformation()
    return company_information, customer_information, email_sequence_information

def create_hooks(company_information, customer_information, email_sequence_information):
    """
    Creates the hooks for the email sequence based on the company, customer, and email sequence information.
    :param company_information: Dictionary containing information about the company
    :param customer_information: Dictionary containing information about the customer
    :param email_sequence_information: Dictionary containing information about the email sequence
    :return: The hooks for the email sequence
    """
    hooks = HookGenerator()
    return hooks.create_new_hooks(
        company_information,
        customer_information,
        email_sequence_information,
    )


def create_sequence(
    company_information, customer_information, email_sequence_information
):
    """
    Creates the email sequence based on the company, customer, and email sequence information.
    :param company_information: Dictionary containing information about the company
    :param customer_information: Dictionary containing information about the customer
    :param email_sequence_information: Dictionary containing information about the email sequence
    :return: The email sequence
    """
    prompt = create_prompt_for_openai_to_generate_prompt(
        company_information, customer_information, email_sequence_information
    )
    return create_email_sequence(
        company_information,
        customer_information,
        email_sequence_information,
        prompt,
    )


def main():
    try:
        (
            company_information,
            customer_information,
            email_sequence_information,
        ) = intialize_background_info()

        email_sequence = create_sequence(
            company_information, customer_information, email_sequence_information
        )

        # Print the generated email sequence
        print(email_sequence)

    except Exception as e:
        print("An error occurred:", e)

    # hooks = HookGenerator()
    # hooks = hooks.generate_hooks_main()

if __name__ == "__main__":
    main()
