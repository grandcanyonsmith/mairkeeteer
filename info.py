import os

from typing import Optional
import openai

from scripts.email_components.hooks import HookGenerator
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation

openai.api_key = os.environ.get("OPENAI_API_KEY")

MODEL_NAME = "text-davinci-003"


def create_completion(
    prompt: str, max_tokens: int, temperature: float, top_p: float, n: int
) -> dict:
    """
    Creates a completion using the OpenAI API based on the given prompt and parameters.

    :return: A dictionary containing the generated completions.
    """
    return openai.Completion.create(
        model=MODEL_NAME,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        n=n,
    )


def extract_first_choice(response: dict) -> str:
    """f
    Extracts the first choice text from the given OpenAI API response.

    :return: The generated text from the AI (first choice of the generated completions).
    """
    return response["choices"][0]["text"]


def call_api(
    prompt: str,
    max_tokens: int = 1000,
    temperature: float = 0.7,
    top_p: float = 1,
    n: int = 1,
) -> str:
    """
    Calls the OpenAI API to generate a completion based on the given prompt using the specified parameters.
    This function creates a completion using the OpenAI API and extracts the first choice from the generated completions.
    :return: The generated text from the AI (first choice of the generated completions).
    """
    response = create_completion(prompt, max_tokens, temperature, top_p, n)
    return extract_first_choice(response)


def generate_email_content(email_prompt: str) -> Optional[str]:
    """
    Generates email content based on the given email_prompt using OpenAI API.

    :return: Generated email content or None if an error occurs.
    """
    try:
        return call_api(email_prompt)
    except openai.OpenAIError as e:
        print(f"Error generating email: {e}")
        return None


def format_info_for_prompt(
    company_info, customer_info, email_sequence_info, email_prompt
):
    """
    Formats the information for the prompt to be used in OpenAI API.

    :return: A formatted string with all the information.
    """
    return f"""
Company Information
Name: {company_info.name}
Company Name: {company_info.company_name}
Product Name: {company_info.product_name}
Product Description: {company_info.product_description}

Customer Information
Desires: {customer_info.desires}
Target Audience: {customer_info.target_audience}
Pains: {customer_info.pains}
Target Demographic: {customer_info.target_demographic}

Email Sequence Information
Number of Emails: {email_sequence_info.number_of_emails}
Type of Email Sequence: {email_sequence_info.type_of_email_sequence}
Sequence Purpose: {email_sequence_info.sequence_purpose}
{email_prompt}
"""


def create_openai_prompt(company_info, customer_info, email_sequence_info):
    """
    Creates a prompt for OpenAI API based on the company, customer, and email sequence information.

    :return: A generated prompt for OpenAI API.
    """
    prompt = "Using the information above, generate a prompt that will be used downstream for another AI to complete the task of creating an email sequence.\n"
    formatted_info = format_info_for_prompt(
        company_info, customer_info, email_sequence_info, prompt
    )
    email_prompt = generate_email_content(formatted_info)
    return email_prompt.strip()


def create_email_sequence(company_info, customer_info, email_sequence_info, prompt):
    """
    Creates an email sequence based on the given prompt and the company, customer, and email sequence information.

    :return: A generated email sequence.
    """
    email_prompt = format_info_for_prompt(
        company_info, customer_info, email_sequence_info, prompt
    )
    return generate_email_content(email_prompt)


def initialize_info():
    """
    Initializes the company, customer, and email sequence information.

    :return: Tuple containing instances of CompanyInformation, CustomerInformation, and EmailSequenceInformation.
    """
    company_info = CompanyInformation()
    customer_info = CustomerInformation()
    email_sequence_info = EmailSequenceInformation()
    return company_info, customer_info, email_sequence_info


def generate_sequence(company_info, customer_info, email_sequence_info):
    """
    Generates an email sequence based on the given company, customer, and email sequence information.

    :return: A generated email sequence.
    """
    prompt = create_openai_prompt(company_info, customer_info, email_sequence_info)
    return create_email_sequence(
        company_info, customer_info, email_sequence_info, prompt
    )


def main():
    """
    The main function to execute the email sequence generation.
    """
    openai.api_key = "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"
    company_info, customer_info, email_sequence_info = initialize_info()
    email_sequence = generate_sequence(company_info, customer_info, email_sequence_info)
    print(email_sequence)


if __name__ == "__main__":
    main()
