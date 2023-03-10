import sys

sys.path.append("../..")  # Adds higher directory to python modules path.

from scripts.utils.select_email_sequence_type import (
    get_email_sequence_from_user,
)
from scripts.utils.formatter import StringFormatter


class EmailSequenceInformation:
    def __init__(self):
        self.number_of_emails = self.get_number_of_emails_from_user()
        (
            self.type_of_email_sequence,
            self.sequence_purpose,
        ) = self.get_sequence_type_and_purpose_from_user()

    def get_number_of_emails_from_user(self):
        return input("How many emails will be in your sequence? ")

    def get_sequence_type_and_purpose_from_user(self):
        list_of_user_email_info = get_email_sequence_from_user()
        formatter = StringFormatter()
        type_of_email_sequence, sequence_purpose = formatter.format_everything(
            list_of_user_email_info
        )
        return type_of_email_sequence, sequence_purpose

if __name__ == "__main__":
    email_sequence_info = EmailSequenceInformation()
    print(email_sequence_info.number_of_emails)
    print(email_sequence_info.type_of_email_sequence)
    print(email_sequence_info.sequence_purpose)