import json
import pathlib
import webbrowser
import openai


def openai_complete(prompt):

    all_text = pathlib.Path("/Users/canyonsmith/Desktop/mairkeeteer/examples/html_css_example.jsonl").read_text()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'{prompt}\n\n{all_text}',
        max_tokens=1200,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["}\n"],
    )
    return response["choices"][0]["text"]


class HTMLTemplateFile:

    def __init__(self, path):
        self.path = path
        self.examples = self._read_json_lines()

    def _read_json_lines(self):
        with open(self.path) as file:
            return [json.loads(line) for line in file]

    def get_code_examples(self):
        return [example["Code"] for example in self.examples]

    def get_email_examples(self):
        return [example["Email"] for example in self.examples]

    def render_html_in_browser(self, html):
        with open("/tmp/example.html", "w") as f:
            f.write(html)
        webbrowser.open("file:///tmp/example.html")


def generate_new_html_css():
    prompt = """
    Example HTML and CSS for a course that teaches you how to create courses. The HTML progressively gets more complex & the CSS progressively gets more stylish.
    """
    with open("/Users/canyonsmith/Desktop/mairkeeteer/examples/html_css_example.jsonl") as f:
        lines = f.readlines() + [openai_complete(prompt)]

        with open("/Users/canyonsmith/Desktop/mairkeeteer/examples/html_css_example.jsonl", "w") as f:
            f.writelines(lines)


def render_html_in_browser(html):
    html_css_file = HTMLTemplateFile("/Users/canyonsmith/Desktop/mairkeeteer/examples/html_css_example.jsonl")
    print(html_css_file.get_code_examples())
    print(html_css_file.get_email_examples())
    html_css_file.render_html_in_browser(str(html_css_file.get_code_examples()[-1]))
    print("rendered")


if __name__ == "__main__":

    generate_new_html_css()
    render_html_in_browser("")
