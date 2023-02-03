import openai
from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


class SubjectLinesCreator:
    def __init__(self):
        self.formatter = StringFormatter()
    def create_subject_lines(
            self, background_info, desired_outcome, step, total_steps):
        prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nStep:\n"""\n{step}\n"""\n\nTotal steps:\n"""\n{total_steps}\n"""\n\nCreate a subject line for this email\n"""\n'''
        response = self._openai_response(prompt)
        return self.formatter.format_everything(response.split("\n"))
    def _openai_response(self, prompt):
        secrets = openai_secret_manager.get_secret("openai")
        openai.api_key = secrets
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.2,
            presence_penalty=0,
        )
        return response["choices"][0]["text"]

if __name__ == "__main__":
    subject_lines_creator = SubjectLinesCreator()
    background_info = "\n".join([
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
    steps = [
            "email 1: introduce course creator pro and explain the benefits of taking the course.",
            "email 2: share success stories from people who have taken the course and achieved their desired outcomes.",
            "email 3: offer a special discount for those who purchase the course within a certain time frame.",
        ]
    for step in steps:
        subject_lines = subject_lines_creator.create_subject_lines(
            background_info, desired_outcome, step, len(steps)
        )
        for subject_line in subject_lines:
            print(subject_line)

