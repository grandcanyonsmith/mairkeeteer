# # Imports the necessary modules.
# import sys
# import json
# import logging
# import unittest
# import typing

# # Adds higher directory to python modules path.
# sys.path.append("../..")

# # Imports utility functions from scripts.utils.
# from scripts.utils import formatter, get_values

# # Imports the classes from scripts.information.
# from scripts.information import (
#     CompanyInformation,
#     CustomerInformation,
#     EmailSequenceInformation,
# )

# # Imports functions from info.
# from info import intialize_background_info, format_background_info

# # Gets the path to the temp.jsonl file.
# temp_json_file = "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl"

# class EmailSequenceCreator:
#     """
#     Class for creating email sequences for abandoned carts.
#     """

#     def __init__(self, company_information: CompanyInformation, customer_information: CustomerInformation,
#                  email_sequence_information: EmailSequenceInformation):
#         """
#         Constructor for EmailSequenceCreator.

#         Args:
#             company_information (CompanyInformation): The company information to use.
#             customer_information (CustomerInformation): The customer information to use.
#             email_sequence_information (EmailSequenceInformation): The email sequence information to use.
#         """
#         # Initializes the formatter.
#         self.formatter = formatter.StringFormatter()

#         # Stores the company, customer, and email sequence information.
#         self.company_information = company_information
#         self.customer_information = customer_information
#         self.email_sequence_information = email_sequence_information

#         # Sets the default email count.
#         self.email_count = 3

#         # Sets the default desired outcome.
#         self.desired_outcome = ""

#     def create_steps(self) -> typing.List[str]:
#         """
#         Creates the steps for the email sequence.

#         Returns:
#             list: The list of steps for the email sequence.
#         """
#         # Logs the start of the Email Sequence Creator.
#         logging.info("Starting Email Sequence Creator")

#         # Creates the prompt for the OpenAI response.
#         prompt = "Background information: %s\n\nDesired Outcome: %s\n\nNumber of emails in the email sequence: %d\n\nSteps in email sequence:" % (
#             self._format_background_info(),
#             self.desired_outcome,
#             self.email_count,
#         )

#         # Gets the response from OpenAI.
#         response = get_values._openai_response(prompt)

#         # Splits the response into a list of steps.
#         steps = response.split("\n")

#         # Formats the steps.
#         steps = self.formatter.format_everything(steps)

#         # Logs that the Email Sequence Creator has finished.
#         logging.info("Email Sequence Creator finished")

#         return steps

#     def _format_background_info(self) -> str:
#         """
#         Formats the background info.

#         Returns:
#             str: The formatted background info.
#         """
#         return format_background_info(
#             self.company_information,
#             self.customer_information,
#             self.email_sequence_information,
#             "",
#         )

#     def save_steps(self, steps: typing.List[str]):
#         """
#         Saves the steps to the temp.jsonl file.

#         Args:
#             steps (list): The list of steps to save.
#         """
#         # Saves the steps to the temp.jsonl file.
#         get_values._add_steps_to_temp_json_file(steps, temp_json_file)


# if __name__ == "__main__":
#     # Sets the logging level to INFO.
#     logging.basicConfig(level=logging.INFO)

#     # Intializes the background info.
#     company_information, customer_information, email_sequence_information = intialize_background_info()

#     # Creates an EmailSequenceCreator object.
#     email_sequence = EmailSequenceCreator(
#         company_information, customer_information, email_sequence_information
#     )

#     # Sets the desired outcome.
#     email_sequence.desired_outcome = "\n".join(
#         [
#             "I need an Abandoned Cart Sequence To remind customers of items they left in their shopping cart and encourage them to complete their purchase.",
#         ]
#     )

#     # Creates the steps for the email sequence.
#     steps = email_sequence.create_steps()

#     # Saves the steps to the temp.jsonl file.
#     email_sequence.save_steps(steps)


# Imports the necessary modules.
import sys
import json
import logging
import unittest
import typing

# Adds higher directory to python modules path.


# Imports utility functions from scripts.utils.
from scripts.utils import formatter, get_values

# Imports the classes from scripts.information.
from scripts.information import (
    CompanyInformation,
    CustomerInformation,
    EmailSequenceInformation,
)

# Imports functions from info.
from info import intialize_background_info, format_background_info

# Gets the path to the temp.jsonl file.
temp_json_file = "/Users/canyonsmith/Documents/GitHub/autogluon/mairkeeteer/files/data/temp/temp.jsonl"


class EmailSequenceCreator:
    """
    Class for creating email sequences for abandoned carts.
    """

    def __init__(
        self,
        company_information: CompanyInformation,
        customer_information: CustomerInformation,
        email_sequence_information: EmailSequenceInformation,
    ):
        """
        Constructor for EmailSequenceCreator.

        Args:
            company_information (CompanyInformation): The company information to use.
            customer_information (CustomerInformation): The customer information to use.
            email_sequence_information (EmailSequenceInformation): The email sequence information to use.
        """
        # Initializes the formatter.
        self.formatter = formatter.StringFormatter()

        # Stores the company, customer, and email sequence information.
        self.company_information = company_information
        self.customer_information = customer_information
        self.email_sequence_information = email_sequence_information

        # Sets the default email count.
        self.email_count = 3

        # Sets the default desired outcome.
        self.desired_outcome = ""

    def create_steps(self) -> typing.List[str]:
        """
        Creates the steps for the email sequence.

        Returns:
            list: The list of steps for the email sequence.
        """
        # Logs the start of the Email Sequence Creator.
        logging.info("Starting Email Sequence Creator")

        # Creates the prompt for the OpenAI response.
        prompt = (
            "Background information: %s\n\nDesired Outcome: %s\n\nNumber of emails in the email sequence: %d\n\nSteps in email sequence:"
            % (
                self._format_background_info(),
                self.desired_outcome,
                self.email_count,
            )
        )

        # Gets the response from OpenAI.
        response = get_values._openai_response(prompt)

        # Splits the response into a list of steps.
        steps = response.split("\n")

        # Formats the steps.
        steps = self.formatter.format_everything(steps)

        # Logs that the Email Sequence Creator has finished.
        logging.info("Email Sequence Creator finished")

        return steps

    def _format_background_info(self) -> str:
        """
        Formats the background info.

        Returns:
            str: The formatted background info.
        """
        return format_background_info(
            self.company_information,
            self.customer_information,
            self.email_sequence_information,
            "",
        )

    def save_steps(self, steps: typing.List[str]):
        """
        Saves the steps to the temp.jsonl file.

        Args:
            steps (list): The list of steps to save.
        """
        # Saves the steps to the temp.jsonl file.
        get_values._add_steps_to_temp_json_file(steps, temp_json_file)


if __name__ == "__main__":
    # Sets the logging level to INFO.
    logging.basicConfig(level=logging.INFO)

    # Intializes the background info.
    (
        company_information,
        customer_information,
        email_sequence_information,
    ) = intialize_background_info()

    # Creates an EmailSequenceCreator object.
    email_sequence = EmailSequenceCreator(
        company_information, customer_information, email_sequence_information
    )

    # Sets the desired outcome.
    email_sequence.desired_outcome = "\n".join(
        [
            "I need an Abandoned Cart Sequence To remind customers of items they left in their shopping cart and encourage them to complete their purchase.",
        ]
    )

    # Creates the steps for the email sequence.
    steps = email_sequence.create_steps()

    # Saves the steps to the temp.jsonl file.
    email_sequence.save_steps(steps)
