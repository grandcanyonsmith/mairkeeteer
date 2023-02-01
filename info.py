import os
import openai
from temp import get_email_sequence_from_user
from formatter import StringFormatter
from get_values import open_info_json, open_info_json_target_demographic, get_hooks_examples_from_file

openai.api_key = os.getenv("OPENAI_API_KEY")


class CompanyInformation:
    def __init__(self, name, company_name, product_name, product_description):
        self.name = name
        self.company_name = company_name
        self.product_name = product_name
        self.product_description = product_description
        
    
    def get_name(self):
        if open_info_json()[0] != "":
            return open_info_json()[0]
        return input("What is your name? ")

    def get_company_name(self):
        if open_info_json()[1] != "":
            return open_info_json()[1]
        return input("What is the name of your company? ")

    def get_product_name(self):
        if open_info_json()[2] != "":
            return open_info_json()[2]
        return input("What is the name of your product? ")

    def get_product_description(self):
        if open_info_json()[3] != "":
            return open_info_json()[3]
        return input("What is the description of your product? ")

    def display_information(self):
        print("Name:", self.name)
        print("Company Name:", self.company_name)
        print("Product Name:", self.product_name)
        print("Product Description:", self.product_description)


class CustomerInformation:
    def __init__(self, desires, target_audience, pains, target_demographic):
        self.desires = desires
        self.target_audience = target_audience
        self.pains = pains
        self.target_demographic = target_demographic

    def get_desires(self):
        if open_info_json_target_demographic()[0] != "":
            return open_info_json_target_demographic()[0]
        return input("What are the desires of your target audience? ")

    def get_target_audience(self):
        if open_info_json_target_demographic()[1] != "":
            return open_info_json_target_demographic()[1]
        return input("What is the target audience of your product? ")

    def get_pains(self):
        if open_info_json_target_demographic()[2] != "":
            return open_info_json_target_demographic()[2]
        return input("What are the pains of your target audience? ")
    
    def get_target_demographic(self):
        if open_info_json_target_demographic()[3] != "":
            return open_info_json_target_demographic()[3]
        return input("What is the target demographic of your target audience? ")
    

    def display_information(self):
        print("Desires:", self.desires)
        print("Target Audience:", self.target_audience)
        print("Pains:", self.pains)
        print("Target Demographic:", self.target_demographic)


class EmailSequenceInformation:
    def __init__(self):
        self.number_of_emails = self.get_number_of_emails()
        self.type_of_email_sequence, self.sequence_purpose = self.get_sequence_type_and_purpose()

    def get_number_of_emails(self):
        return input("How many emails will be in your sequence? ")

    def get_sequence_type_and_purpose(self):
        list_of_user_email_info = get_email_sequence_from_user()
        formatter = StringFormatter()
        type_of_email_sequence, sequence_purpose = formatter.format_everything(
            list_of_user_email_info
        )
        print(type_of_email_sequence, sequence_purpose)
        return type_of_email_sequence, sequence_purpose

    def display_information(self):
        print("Number of Emails:", self.number_of_emails)
        print("Type of Email Sequence:", self.type_of_email_sequence)
        print("Sequence Purpose:", self.sequence_purpose)


def generate_prompt(company_info, customer_info, email_sequence_info, start_sequence, restart_sequence, instructions):
    prompt=f"""
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

{instructions}
    """
    print(prompt)
    start_sequence = start_sequence
    restart_sequence = restart_sequence
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=0,
        n=1,
    )
    return response["choices"][0]["text"]


def main():
    instructions = """
    Please write a brief email sequence that will be sent to your target audience. 
    The sequence should be based on the information provided above.
    """

    company_info = CompanyInformation(
        CompanyInformation.get_name(CompanyInformation),
        CompanyInformation.get_company_name(CompanyInformation),
        CompanyInformation.get_product_name(CompanyInformation),
        CompanyInformation.get_product_description(CompanyInformation),
    )
    company_info.display_information()

    customer_info = CustomerInformation(
        CustomerInformation.get_desires(CustomerInformation),
        CustomerInformation.get_target_audience(CustomerInformation),
        CustomerInformation.get_pains(CustomerInformation),
        CustomerInformation.get_target_demographic(CustomerInformation),
    )

    email_sequence_info = EmailSequenceInformation()

    prompt = generate_prompt(
        company_info=company_info,
        customer_info=customer_info,
        email_sequence_info=email_sequence_info,
        start_sequence = "\n\nPrompt\n",
        restart_sequence = "\n",
        instructions="Using the information above, generate a prompt that will be used downstream for another AI to complete the task of creating an email sequence.",
    )
    # strip newlines
    prompt = prompt.replace("\n", " ")
    print(f'#{prompt}#')
    prompt = generate_prompt(
        company_info=company_info,
        customer_info=customer_info,
        email_sequence_info=email_sequence_info,
        start_sequence = None,
        restart_sequence = None,
        instructions=f'{prompt}',
    )
    print(prompt)
    hooks = get_hooks_examples_from_file()
    def create_new_hooks(hooks):
        prompt = f"""
Example Hooks for a course that teaches you how to tune your car
{hooks}

Company Information
Name: {company_info.name}
Company Name: {company_info.company_name}
Product Name: {company_info.product_name}
Product Description: {company_info.product_description}

Background Information
Desires: {customer_info.desires}
Target Audience: {customer_info.target_audience}
Pains: {customer_info.pains}
Target Demographic: {customer_info.target_demographic}

Hook Information
Number of Hooks: {email_sequence_info.number_of_emails}
Type of Hook: {email_sequence_info.type_of_email_sequence}
Desired Outcome: {email_sequence_info.sequence_purpose}


Write a 12-15 word hook that will be used to get your target audience to do the desired outcome
"""
        print(prompt)
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        top_p=0,
        n=1,
        )
        return response["choices"][0]["text"]
    print(create_new_hooks(hooks))

# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    main()

