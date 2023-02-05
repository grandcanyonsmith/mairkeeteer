import sys
import json

sys.path.append("../..")  # Adds higher directory to python modules path.

from scripts.utils.get_values import get_hooks_examples_from_file
from scripts.information.company_information import CompanyInformation
from scripts.information.customer_information import CustomerInformation
from scripts.information.email_sequence_information import EmailSequenceInformation


import openai


class Hooks:
    def __init__(self):
        self.hooks = []
        self.hooks_examples = get_hooks_examples_from_file()
        self.email_number = self.count_hooks() + 1

    def create_new_hooks(
        self, company_info, customer_info, email_sequence_info, step, email_number
    ):
        print("Creating new hooks...")

        prompt = f"""
        Example Hooks for a course that teaches you how to tune your car
        {self.hooks_examples}





        Company Information:
        Name: {company_info.name}
        Company Name: {company_info.company_name}
        Product Name: {company_info.product_name}
        Product Description: {company_info.product_description}
        Common Mistake People Make: {company_info.common_mistake}
        Ideal Customer Avatar: {company_info.ideal_market_avatar}
        Common Enemy: {company_info.common_enemy}
        Everyday Person: {company_info.everyday_person}
        Consequence of Not Solving Problem: {company_info.consequence}
        Traditional Way of Solving Problem: {company_info.traditional_way}
        Ideal Person: {company_info.ideal_person}
        Painful Attempt: {company_info.painful_attempt}
        Relatable Pain Point: {company_info.relatable_pain_point}
        Solution: {company_info.solution}
        Hack, Tool, or Trick: {company_info.hack_tool_trick}
        Common Achievement: {company_info.common_achievement}
        Perceived Experts: {company_info.perceived_experts}
        Current Year: {company_info.current_year}
        Easy Task: {company_info.easy_task}
        Biggest Objection: {company_info.biggest_objection}





        Background Information:
        Customer Desires: {customer_info.desires}
        Target Audience: {customer_info.target_audience}
        Customer Pains: {customer_info.pains}
        Target Demographic: {customer_info.target_demographic}
        

        We are creating an email sequence to {email_sequence_info.type_of_email_sequence} {email_sequence_info.sequence_purpose}. There are a total of {email_sequence_info.number_of_emails} emails in this sequence. This is email number {email_number}
        In this email, we are going to {step}. We need to write a 12-15 word hook that we will use for the subject line of the email. The hook should be written in a way that will get the target audience to do the desired outcome. The desired outcome is {email_sequence_info.sequence_purpose}.
        """
        # print(prompt)
        return self.get_hooks_from_openai(prompt)

    def count_hooks(self):
        return len(self.hooks)

    def get_hooks_from_openai(self, prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
            top_p=0,
            n=3,
        )
        return response["choices"][0]["text"]


if __name__ == "__main__":
    # create a function that creates a list of all steps in the temp.jsonl file
    temp_file = "../../files/data/temp/temp.jsonl"

    def create_steps_list():
        with open(temp_file, "r") as f:
            steps = [json.loads(line)["step"] for line in f]
        return steps

    steps = create_steps_list()
    print(steps, f"Total number of steps: {len(steps)}")
    company_info = CompanyInformation()
    customer_info = CustomerInformation()
    email_sequence_info = EmailSequenceInformation()
    hooks = Hooks()
    for step in steps:
        hook = hooks.create_new_hooks(
            company_info, customer_info, email_sequence_info, step, hooks.email_number
        )
        hooks.hooks.append(hook)
        hooks.email_number += 1
    hooks = hooks.hooks
