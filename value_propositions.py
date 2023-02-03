import openai
from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


class ValuePropositionsCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_value_propositions(
        self, background_info, desired_outcome, step, total_steps
    ):
        prompt = f'''Background information:\n"""\n{background_info}\n"""\n\nDesired Outcome:\n"""\n{desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{total_steps}\n"""\n\nStep:\n"""\n{step}\n"""\n\nWhat should the value proposition be for this email?\n"""\n'''  # noqa: E501  # noqa: E501
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
    value_propositions_creator = ValuePropositionsCreator()
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
    steps = [
        "email 1: introduce course creator pro and explain the benefits of taking the course.",  # noqa: E501
        "email 2: share success stories from people who have taken the course and achieved their desired outcomes.",  # noqa: E501
        "email 3: offer a special discount for those who purchase the course within a certain time frame.",  # noqa: E501
    ]
    for step in steps:
        value_propositions = value_propositions_creator.create_value_propositions(
            background_info, desired_outcome, step, len(steps)
        )
        for value_proposition in value_propositions:
            print(value_proposition)
