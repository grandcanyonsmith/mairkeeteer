import sys


import json
import pathlib
import webbrowser


FILE_PATH = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/html_css_example_email.jsonl"
import openai


def openai_complete(prompt):
    all_text = pathlib.Path(
        "../../../files/data/examples/html_css_example_email.jsonl"
    ).read_text()
    # get the value of the 'Email' key of the last line
    all_text = json.loads(all_text)["Email"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{prompt}\n\n{all_text}",
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
    with open(
        "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/html_css_example_email.jsonl",
    ) as f:
        lines = f.readlines() + [openai_complete(prompt)]

        with open(
            "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/html_css_example_email.jsonl",
            "w",
        ) as f:
            f.writelines(lines)


def render_html_in_browser(html):
    html_css_file = HTMLTemplateFile(
        "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/html_css_example_email.jsonl"
    )
    html_css_file.render_html_in_browser(str(html_css_file.get_code_examples()[-1]))
    print("rendered")


# create a function to get the last line of the file
def get_last_line_of_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return lines[-1]


def get_key_from_last_line_of_file(last_line, key):
    return json.loads(last_line)[key]


# have openai complete the prompt
def openai_complete(prompt, last_line):
    all_text = pathlib.Path(
        "/Users/bottega/Desktop/mairket/mairkeeteer/files/data/examples/html_css_example.jsonl"
    ).read_text()
    prompt = (
        f"""Example of converting Email into HTML/CSS\nEmail:\nSubject: Unock Your Course Creation Potential with Course Creator Pro\n\n\\Dear [Name],\n\n\n\Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you\n\n\nIntroducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily.\n\n\nLearn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.\n\n\nLearn more about Course Creator Pro today and unlock your course creation potential.\n\n\nSincerely, \n\n\n[Your Name]\nCode:\n<!DOCTYPE html> <html> <head> <style> .container max-width: 600px;margin: 0 auto; padding: 20px; text-align: center; font-family: Arial, sans-serif;  h2  font-size: 26px; font-weight: bold; margin-bottom: 20px;  p  font-size: 16px; line-height: 1.5; margin-bottom: 20px; a display: inline-block; padding: 10px 20px; background-color: #2ab27b; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 20px; </style> </head> <body> <div class=\"container\"> <h2>Unlock Your Course Creation Potential with Course Creator Pro</h2> <p>Dear [Name],</p><p>Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you. </p> <p>Introducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily. </p> <p>Learn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.</p> <a href=\#\>Learn More Today</a> </div></body> </html>\n\n\nNew Email\n{last_line}\n\n\nNew Code\n""",
    )
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1200,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["}\n"],
    )
    return response["choices"][0]["text"]


# {"Email": "Dear [Name],\n\nWe noticed that you left some items in your shopping cart and wanted to remind you that you can still complete your purchase. Don't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nCourse Creator Pro is the perfect solution for anyone looking to create and sell their own online courses. It provides step-by-step guidance, helpful resources, and expert advice to help you get started quickly and easily. Plus, with our money-back guarantee, you can be sure that you're making a safe investment.\n\nFor a limited time only, we are offering a discount on Course Creator Pro. Take advantage of this offer now and save money on your purchase.\n\nDon't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nSincerely, \n[Your Name]"}{"Email": "Dear [Name],\n\nWe noticed that you left some items in your shopping cart and wanted to remind you that you can still complete your purchase. Don't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nCourse Creator Pro is the perfect solution for anyone looking to create and sell their own online courses. It provides step-by-step guidance, helpful resources, and expert advice to help you get started quickly and easily. Plus, with our money-back guarantee, you can be sure that you're making a safe investment.\n\nFor a limited time only, we are offering a discount on Course Creator Pro. Take advantage of this offer now and save money on your purchase.\n\nDon't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nSincerely, \n[Your Name]", "Code": "<!DOCTYPE html> <html> <head> <style> .container max-width: 600px;margin: 0 auto; padding: 20px; text-align: center; font-family: Arial, sans-serif;  h2  font-size: 26px; font-weight: bold; margin-bottom: 20px;  p  font-size: 16px; line-height: 1.5; margin-bottom: 20px; a display: inline-block; padding: 10px 20px; background-color: #2ab27b; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 20px; </style> </head> <body> <div class=\"container\"> <h2>Unlock Your Expertise with Course Creator Pro</h2> <p>Dear [Name],</p><p>We noticed that you left some items in your shopping cart and wanted to remind you that you can still complete your purchase. Don't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro. </p> <p>Course Creator Pro is the perfect solution for anyone looking to create and sell their own online courses. It provides step-by-step guidance, helpful resources, and expert advice to help you get started quickly and easily. Plus, with our money-back guarantee, you can be sure that you're making a safe investment. </p> <p>For a limited time only, we are offering a discount on Course Creator Pro. Take advantage of this offer now and save money on your purchase.</p> <a href=\\#\\>Complete Your Purchase Now</a> </div></body> </html>"}
import os

print(os.getcwd())
last_line = get_last_line_of_file(
    "/Users/bottega/Desktop/mairket/mairkeeteer/files/data/examples/html_css_code_example.jsonl"
)
print(last_line)
# convert the last line to a dictionary
last_line = str(last_line)

string_of_code = json.loads(last_line)
print(string_of_code["Code"])


def get_key_from_last_line_of_file(last_line, key):
    last_line = json.loads(last_line)
    return last_line[key]


print(get_key_from_last_line_of_file(last_line, "Code"))
if __name__ == "__main__":
    prompt = """
    Example HTML and CSS for a course that teaches you how to create courses. The HTML progressively gets more complex & the CSS progressively gets more stylish.
    """

    # get the last line of the file
    last_line = get_last_line_of_file(
        "/Users/bottega/Desktop/mairket/mairkeeteer/files/data/examples/html_css_example.jsonl"
    )

    # get the value of the 'Email' key of the last line
    last_line_email = get_key_from_last_line_of_file(last_line, "Email")

    code = openai_complete(prompt, last_line_email)

    # append ['Code'] to the last line of the file as a new key Code
    last_line = json.loads(last_line)
    last_line["Code"] = code
    print(last_line, "LASTLINE")
    last_line = json.dumps(last_line)
    new_file_path = (
        "/Users/bottega/Desktop/mairket/mairkeeteer/files/data/examples/html_css_code_example_new.jsonl",
    )
    last_line = json.dumps({"Code": last_line})
    print(last_line, "YO")
    with open(new_file_path, "w") as f:
        f.write(last_line)


def get_last_line_of_file(file_path):
    with open(file_path, "r") as f:
        last_line = f.readlines()[-1]
    return last_line
