import openai
from scripts.utils.formatter import StringFormatter
from scripts.utils.openai_secret_manager import OpenAiSecretManager as openai_secret_manager

class EmailSequence:
    def __init__(self):
        self.background_info = "\n".join([
            "I sell online courses that teach people how to sell online courses",
            "It is called Course Creator Pro",
        ])
        self.desired_outcome = "\n".join([
            "People just watched my webinar",
            "I want to send them an email sequence that will get them to buy my course",
        ])
        self.email_count = 3
        self.steps = []

    def create_steps(self):
        prompt = f'''Background information:\n"""\n{self.background_info}\n"""\n\nDesired Outcome:\n"""\n{self.desired_outcome}\n"""\n\nNumber of emails in the email sequence:\n"""\n{self.email_count}\n"""\n\nSteps in email sequence\n"""\n'''
        response = self._openai_response(prompt)
        self.steps = response.split("\n")
        return formatter.format_everything(self.steps)

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
    formatter = StringFormatter()
    email_sequence = EmailSequence()    
    steps = email_sequence.create_steps()
    for step in steps:
        print(step)
