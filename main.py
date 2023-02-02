import json
#!/usr/bin/env python3
# import os
# import json
# import logging
# from typing import List
# from openai_secret_manager import OpenAiSecretManager as openai_secret_manager
# from utils.formatter import StringFormatter

# import openai  # Module for interacting with OpenAI's APIs


# class EmailSequence:
#     def __init__(self):
#         self.background_information = "I am a software engineer who is looking to sell my product to other software engineers."
#         self.desired_outcome = "Subscribe to my email list after watching my webinar."
#         self.number_of_emails = 4

#         self.steps = []
#         self.subject_lines = []
#         self.value_propositions = []
#         self.ctas = []
#         self.email_sequence = []

#         self.steps = self.create_steps()
#         self.subject_lines = self.create_subject_lines()
#         self.value_propositions = self.create_value_propositions()
#         self.ctas = self.create_ctas()
#         self.email_sequence = self.create_email_sequence()

#         self.logger = logging.getLogger(__name__)
#         logging.basicConfig(
#             level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(message)s"
#         )

#     def openai_generator(
#         self,
#         model,
#         prompt,
#         temperature,
#         max_tokens,
#         top_p,
#         frequency_penalty,
#         presence_penalty,
#     ):
#         # Use the openai_secret_manager library to access the API key
#         secrets = openai_secret_manager.get_secret("openai")
#         openai.api_key = secrets

#         response = openai.Completion.create(
#             engine=model,
#             prompt=prompt,
#             temperature=temperature,
#             max_tokens=max_tokens,
#             top_p=top_p,
#             frequency_penalty=frequency_penalty,
#             presence_penalty=presence_penalty,
#         )

#         # Return the generated text
#         return response["choices"][0]["text"]

#     def create_steps(self):
#         prompt = f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence\n"""\n'''
#         steps_text = self.openai_generator(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0,
#             max_tokens=500,
#             top_p=1,
#             frequency_penalty=0.2,
#             presence_penalty=0,
#         )
#         self.steps = steps_text.split("\n")
#         return formatter.format_everything([step for step in self.steps if step != ""])

#     def create_subject_lines(self):
#         prompt = f'''Steps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""'''
#         subject_lines_text = self.openai_generator(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0,
#             max_tokens=500,
#             top_p=1,
#             frequency_penalty=0.2,
#             presence_penalty=0,
#         )
#         self.subject_lines = subject_lines_text.split("\n")
#         return formatter.format_everything(
#             [subject_line for subject_line in self.subject_lines if subject_line != ""]
#         )

#     def create_value_propositions(self):
#         prompt = f'''Background information:\n"""\n{' '.join(self.background_information)}\n"""\n\nDesired Outcome:\n"""\n{' '.join(self.desired_outcome)}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nValue propositions for email sequence:\n"""'''
#         value_propositions_text = self.openai_generator(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0,
#             max_tokens=500,
#             top_p=1,
#             frequency_penalty=0.2,
#             presence_penalty=0,
#         )
#         self.value_propositions = value_propositions_text.split("\n")
#         return formatter.format_everything(
#             [
#                 value_proposition
#                 for value_proposition in self.value_propositions
#                 if value_proposition != ""
#             ]
#         )

#     def create_prompt(self):
#         return f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""\n{' '.join(self.subject_lines)}\n"""\n\nValue propositions for email sequence:\n"""\n{' '.join(self.value_propositions)}\n"""\n\nCTAs for email sequence:\n"""\n'''

#     def generate_ctas(self, prompt):
#         ctas_text = self.openai_generator(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0,
#             max_tokens=500,
#             top_p=1,
#             frequency_penalty=0.2,
#             presence_penalty=0,
#         )
#         self.ctas = ctas_text.split("\n")
#         return formatter.format_everything([cta for cta in self.ctas if cta != ""])

#     def create_ctas(self):
#         # self.validate_input()
#         prompt = self.create_prompt()
#         return self.generate_ctas(prompt)

#     def create_email_sequence(self):
#         self.generate_email_sequence()
#         return formatter.format_everything(
#             [email for email in self.email_sequence if email != ""]
#         )

#     def format_prompt(self):
#         return f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""\n{' '.join(self.subject_lines)}\n"""\n\nValue propositions for email sequence:\n"""\n{' '.join(self.value_propositions)}\n"""\n\nCTAs for email sequence:\n"""\n{' '.join(self.ctas)}\n"""\n\nEmail sequence:\n"""\n'''

#     def generate_email_sequence(self):
#         prompt = self.format_prompt()
#         email_sequence_text = self.openai_generator(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0,
#             max_tokens=500,
#             top_p=1,
#             frequency_penalty=0.2,
#             presence_penalty=0,
#         )
#         self.email_sequence = email_sequence_text.split("\n")

#     def __getitem__(self, index):
#         return (
#             self.steps[index],
#             self.subject_lines[index],
#             self.value_propositions[index],
#             self.ctas[index],
#             self.email_sequence[index],
#         )

#     def __len__(self):
#         return len(self.steps)

#     def __repr__(self):
#         return f"EmailSequence(steps={self.steps}, subject_lines={self.subject_lines}, value_propositions={self.value_propositions}, ctas={self.ctas}, email_sequence={self.email_sequence})"

#     def __str__(self):
#         return f"EmailSequence(steps={self.steps}, subject_lines={self.subject_lines}, value_propositions={self.value_propositions}, ctas={self.ctas}, email_sequence={self.email_sequence})"

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self):
#             raise StopIteration
#         self.index += 1
#         return self[self.index - 1]

#     def __call__(self):
#         return self

#     def __add__(self, other):
#         return EmailSequence(
#             steps=self.steps + other.steps,
#             subject_lines=self.subject_lines + other.subject_lines,
#             value_propositions=self.value_propositions + other.value_propositions,
#             ctas=self.ctas + other.ctas,
#             email_sequence=self.email_sequence + other.email_sequence,
#         )


# if __name__ == "__main__":
#     formatter = StringFormatter()

#     email_sequence = EmailSequence()
#     print(email_sequence)


import logging

import openai  # Module for interacting with OpenAI's APIs

from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import \
    OpenAiSecretManager as openai_secret_manager


class EmailSequence:
    def __init__(self):
        self.background_information = [
            "I sell online courses that teach people how to sell online courses",
            "It is called Course Creator Pro",
        ]
        self.desired_outcome = [
            "People just watched my webinar",
            "I want them to sign up for my course",
        ]
        self.number_of_emails = 2

        self.steps = []
        self.subject_lines = []
        self.value_propositions = []
        self.ctas = []
        self.email_sequence = []

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(message)s"
        )

    def openai_generator(
        self,
        model,
        prompt,
        temperature,
        max_tokens,
        top_p,
        frequency_penalty,
        presence_penalty,
    ):
        secrets = openai_secret_manager.get_secret("openai")
        openai.api_key = secrets

        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
        # Return the generated text
        return response["choices"][0]["text"]

    def create_steps(self):
        prompt = f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence\n"""\n'''  # noqa
        steps_text = self.openai_generator(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        self.steps = [step for step in steps_text.split("\n") if step]
        return formatter.format_everything(self.steps)

    def create_subject_lines(self):
        prompt = f'''Steps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""\n'''
        subject_lines_text = self.openai_generator(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        self.subject_lines = [
            subject_line
            for subject_line in subject_lines_text.split("\n")
            if subject_line != ""
        ]
        return formatter.format_everything(self.subject_lines)

    def create_value_propositions(self):
        prompt = f'''Background information:\n"""\n{' '.join(self.background_information)}\n"""\n\nDesired Outcome:\n"""\n{' '.join(self.desired_outcome)}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nValue propositions for email sequence:\n"""\n'''  # noqa
        value_propositions_text = self.openai_generator(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        self.value_propositions = [
            value_proposition
            for value_proposition in value_propositions_text.split("\n")
            if value_proposition
        ]
        return formatter.format_everything(self.value_propositions)

    def create_prompt(self):
        return f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""\n{' '.join(self.subject_lines)}\n"""\n\nValue propositions for email sequence:\n"""\n{' '.join(self.value_propositions)}\n"""\n\nCTAs for email sequence:\n"""\n'''

    def generate_ctas(self, prompt, model="text-davinci-003"):
        ctas_text = self.openai_generator(
            model=model,
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        self.ctas = [cta for cta in ctas_text.split("\n") if cta != ""]
        return formatter.format_everything(self.ctas)

    def create_ctas(self):
        prompt = self.create_prompt()
        return self.generate_ctas(prompt)

    def format_prompt(self):
        return f'''Background information:\n"""\n{self.background_information}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.number_of_emails}\n"""\n\nSteps in email sequence:\n"""\n{' '.join(self.steps)}\n"""\n\nSubject lines for email sequence:\n"""\n{' '.join(self.subject_lines)}\n"""\n\nValue propositions for email sequence:\n"""\n{' '.join(self.value_propositions)}\n"""\n\nCTAs for email sequence:\n"""\n{' '.join(self.ctas)}\n"""\n\nEmail sequence:\n"""\n'''

    def generate_email_sequence(self):
        prompt = self.format_prompt()
        email_sequence_text = self.openai_generator(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        self.email_sequence = email_sequence_text.split("\n")

    def create_email_sequence(self):
        self.generate_email_sequence()
        self.email_sequence = [email for email in self.email_sequence if email != ""]
        return formatter.format_everything(self.email_sequence)

    def __getitem__(self, index):
        return (
            self.steps[index],
            self.subject_lines[index],
            self.value_propositions[index],
            self.ctas[index],
            self.email_sequence[index],
        )

    def __len__(self):
        return len(self.steps)

    def __repr__(self):
        return f"EmailSequence(steps={self.steps}, subject_lines={self.subject_lines}, value_propositions={self.value_propositions}, ctas={self.ctas}, email_sequence={self.email_sequence})"

    def __str__(self):
        self.index = 0
        return f"EmailSequence(steps={self.steps}, subject_lines={self.subject_lines}, value_propositions={self.value_propositions}, ctas={self.ctas}, email_sequence={self.email_sequence})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        self.index += 1
        return self[self.index - 1]

    def __call__(self):
        return self

    def __add__(self, other):
        return EmailSequence(
            steps=self.steps + other.steps,
            subject_lines=self.subject_lines + other.subject_lines,
            value_propositions=self.value_propositions + other.value_propositions,
            ctas=self.ctas + other.ctas,
            email_sequence=self.email_sequence + other.email_sequence,
        )


if __name__ == "__main__":
    formatter = StringFormatter()

    email_sequence = EmailSequence()

    # Create the steps
    steps = email_sequence.create_steps()
    for step in steps:
        print("Step:", step, end="\n\n")

    # Create the subject lines
    subject_lines = email_sequence.create_subject_lines()
    for subject_line in subject_lines:
        print("Subject Line:", subject_line, end="\n\n")

    # Create the value propositions
    value_propositions = email_sequence.create_value_propositions()
    for value_proposition in value_propositions:
        print("Value Proposition:", value_proposition, end="\n\n")
        
    # Create the CTAs
    ctas = email_sequence.create_ctas()
    for cta in ctas:
        print("CTA:", cta, end="\n\n")

    # Create the email sequence
    email_sequences = email_sequence.create_email_sequence()
    for email in email_sequences:
        print("Email:", email, end="\n\n")


# class DataLoader:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def load_data(self):
#         with open(self.file_path, 'r') as file:
#             data = json.load(file)
#         return data

# class DataPreprocessor:
#     def __init__(self, data):
#         self.data = data

#     def preprocess_data(self):
#         data = self.data.copy()
#         # preprocessing steps
#         return data

# class EmailStepCreator:
#     def __init__(self, data):
#         self.data = data

#     def create_email_step(self, step_num):
#         email_step = self.data.get(f'step_{step_num}')
#         return email_step

# class SubjectLineCreator:
#     def __init__(self, data):
#         self.data = data

#     def create_subject_line(self):
#         subject_line = self.data.get('subject_line')
#         return subject_line

# class ValuePropositionCreator:
#     def __init__(self, data):
#         self.data = data

#     def create_value_proposition(self):
#         value_proposition = self.data.get('value_proposition')
#         return value_proposition

# class CallToActionCreator:
#     def __init__(self, data):
#         self.data = data

#     def create_call_to_action(self):
#         call_to_action = self.data.get('call_to_action')
#         return call_to_action

# class EmailSequenceCreator:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def create_email_sequence(self):
#         data_loader = DataLoader(self.file_path)
#         data = data_loader.load_data()
#         data_preprocessor = DataPreprocessor(data)
#         data = data_preprocessor.preprocess_data()

#         email_sequence = []
#         print(data)
#         num_steps = data.get('num_steps')
#         num_steps = int(num_steps)
        
#         for step_num in range(1, num_steps + 1):
#             email_step_creator = EmailStepCreator(data)
#             email_step = email_step_creator.create_email_step(step_num)

#             subject_line_creator = SubjectLineCreator(email_step)
#             subject_line = subject_line_creator.create_subject_line()

#             value_proposition_creator = ValuePropositionCreator(email_step)
#             value_proposition = value_proposition_creator.create_value_proposition()

#             call_to_action_creator = CallToActionCreator(email_step)
#             call_to_action = call_to_action_creator.create_call_to_action()
#             print(call_to_action)
#             email = {
#                 'subject_line': subject_line,
#                 'value_proposition': value_proposition,
#                 'call_to_action': call_to_action
#             }
#             email_sequence.append(email)
#         return email_sequence

# if __name__ == "__main__":
#     file_path = 'data.json'
#     email_sequence_creator = EmailSequenceCreator(file_path)
#     email_sequence = email_sequence_creator.create_email_sequence()
#     print(email_sequence)