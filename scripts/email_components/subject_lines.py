import openai
import sys

sys.path.append("../..")  # Adds higher directory to python modules path.

from scripts.utils.get_values import get_hooks_examples_from_file
from scripts.utils.get_values import (
    get_key_values_from_temp_json_file,
    append_key_value_to_json_file,
    _openai_response,
)
from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


class SubjectLinesCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_subject_lines(self, background_info, desired_outcome, step, total_steps):
        prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nStep:\n"""\n{step}\n"""\n\nTotal steps:\n"""\n{total_steps}\n"""\n\nCreate a subject line for this email\n"""\n'''
        response = _openai_response(prompt)
        return self.formatter.format_everything(response.split("\n"))


if __name__ == "__main__":
    subject_lines_creator = SubjectLinesCreator()
    background_info = "\n".join(
        [
            "I sell online courses that teach people how to sell online courses",
            "It is called Course Creator Pro",
        ]
    )
    desired_outcome = "\n".join(
        [
            "People just watched my webinar",
            "I want to send them an email sequence that will get them to buy my course",
        ]
    )
    steps = get_key_values_from_temp_json_file("step")
    print(steps)
    for step in steps:
        subject_lines = subject_lines_creator.create_subject_lines(
            background_info, desired_outcome, step, len(steps)
        )
        for subject_line in subject_lines:
            print(subject_line)
