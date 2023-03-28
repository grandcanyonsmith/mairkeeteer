import json
import webbrowser
import openai


OPENAI_API_KEY = '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'
HTML_CSS_EXAMPLES_FILE = "/Users/canyons/mairkeeteer/files/data/examples/html_css_example.jsonl"
HTML_CSS_CODE_EXAMPLES_FILE = "/Users/canyons/mairkeeteer/files/data/examples/html_css_code_example.jsonl"


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


def get_last_line_of_file(file_path):
    with open(file_path, "r") as f:
        last_line = f.readlines()[-1]
    return last_line


def openai_complete(prompt, email):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}\n\n{email}",
        max_tokens=1200,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["}\n"],
    )
    return response["choices"][0]["text"]


def main():
    prompt = """
    Example HTML and CSS for a course that teaches you how to create courses. The HTML progressively gets more complex & the CSS progressively gets more stylish.
    """

    last_line = get_last_line_of_file(HTML_CSS_CODE_EXAMPLES_FILE)
    print(last_line) # print the last line to check its content
    email = json.loads(last_line)["Email"]
    code = openai_complete(prompt, email)

    last_line = json.loads(last_line)
    last_line["Code"] = code

    with open(HTML_CSS_CODE_EXAMPLES_FILE, "a") as f:
        f.write(json.dumps(last_line) + "\n")

    html_css_file = HTMLTemplateFile(HTML_CSS_CODE_EXAMPLES_FILE)
    html_css_file.render_html_in_browser(str(html_css_file.get_code_examples()[-1]))
    print("rendered")



if __name__ == "__main__":
    main()

