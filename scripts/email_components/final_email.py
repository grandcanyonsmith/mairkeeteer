# {"step": "Reminder of items left in cart - this email should remind the customer of the items they left in their shopping cart and encourage them to complete their purchase.", "step_number": 1, "hook": "\nDon't Miss Out! Complete Your Purchase Now.", "value_proposition": "The value proposition for this email should be that course creator pro is the perfect solution for anyone looking to create and sell their own online courses. it provides step-by-step guidance and support to help you get started quickly and easily. plus, with our money-back guarantee, you can be sure that you're making a safe investment."}
import json
import sys

import openai

sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.formatter import StringFormatter
from scripts.utils.get_values import (
    _openai_response,
    append_key_value_to_temp_json_file,
    get_key_values_from_temp_json_file,
)
from scripts.utils.openai_secret_manager import (
    OpenAiSecretManager as openai_secret_manager,
)


# This class is used to create the final email
class FinalEmailCreator:
    def __init__(self):
        self.formatter = StringFormatter()

    def create_final_email(self, step, hook, value_proposition, call_to_action):
        prompt = f'''Step in email sequence\n"""\n{step}\n"""\n\nHook:\n"""\n{hook}\n"""\n\nValue Proposition:\n"""\n{value_proposition}\n"""\n\nFinal Email\n"""\n'''
        return _openai_response(prompt)

    def create_final_email_from_temp_json_file(self, temp_json_file):
        keys = ["step", "hook", "value_proposition", "call_to_action"]
        for key in keys:
            value = get_key_values_from_temp_json_file(key)
            if value is None:
                value = self.get_value_from_user(key)
                append_key_value_to_temp_json_file(key, value)
        step = get_key_values_from_temp_json_file("step")
        hook = get_key_values_from_temp_json_file("hook")
        value_proposition = get_key_values_from_temp_json_file("value_proposition")
        call_to_action = get_key_values_from_temp_json_file("call_to_action")
        return self.create_final_email(step, hook, value_proposition, call_to_action)

    def get_value_from_user(self, key):
        print(f"Please enter the {key} for this email")
        return input()

    # convert to json
    def convert_to_json(self, final_email):
        print(final_email)
        return json.dumps({"Email": final_email})

    # add a new key value pair to the json file
    def append_to_file(self, final_email):
        filepath = "/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/html_css_example.jsonl"
        with open(filepath, "a") as f:
            f.write(final_email)
            f.write("\n")


if __name__ == "__main__":
    temp_json_file = "temp.jsonl"
    final_email_creator = FinalEmailCreator()
    final_email = final_email_creator.create_final_email_from_temp_json_file(
        temp_json_file
    )
    # convert to json

    # write to file
    final_email = final_email_creator.convert_to_json(final_email)
    final_email_creator.append_to_file(final_email)
# {"Email": "Subject: Unock Your Course Creation Potential with Course Creator Pro\\Dear [Name],\\Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you.\\Introducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily.\\Learn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.\\Learn more about Course Creator Pro today and unlock your course creation potential.\\Sincerely, \\[Your Name]'", "Code":"<!DOCTYPE html> <html> <head> <style> .container { max-width: 600px;margin: 0 auto; padding: 20px; text-align: center; font-family: Arial, sans-serif; } h2 { font-size: 26px; font-weight: bold; margin-bottom: 20px; } p { font-size: 16px; line-height: 1.5; margin-bottom: 20px; } a {display: inline-block; padding: 10px 20px; background-color: #2ab27b; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 20px; }</style> </head> <body> <div class="container"> <h2>Unlock Your Course Creation Potential with Course Creator Pro</h2> <p>Dear [Name],</p><p>Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you. </p> <p>Introducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily. </p> <p>Learn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.</p> <a href="#">Learn More Today</a> </div></body> </html>"}
# ['<!DOCTYPE html> <html> <head> <style> .container { max-width: 600px;margin: 0 auto; padding: 20px; text-align: center; font-family: Arial, sans-serif; } h2 { font-size: 26px; font-weight: bold; margin-bottom: 20px; } p { font-size: 16px; line-height: 1.5; margin-bottom: 20px; } a {display: inline-block; padding: 10px 20px; background-color: #2ab27b; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 20px; }</style> </head> <body> <div class="container"> <h2>Unlock Your Course Creation Potential with Course Creator Pro</h2> <p>Dear [Name],</p><p>Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you. </p> <p>Introducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily. </p> <p>Learn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.</p> <a href="#">Learn More Today</a> </div></body> </html>', '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<style>\n\t\t\t.container {\n\t\t\t\tmax-width: 600px;\n\t\t\t\tmargin: 0 auto;\n\t\t\t\tpadding: 20px;\n\t\t\t\ttext-align: center;\n\t\t\t\tfont-family: Arial, sans-serif;\n\t\t\t}\n\t\t\th2 {\n\t\t\t\tfont-size: 26px;\n\t\t\t\tfont-weight: bold;\n\t\t\t\tmargin-bottom: 20px;\n\t\t\t}\n\t\t\tp {\n\t\t\t\tfont-size: 16px;\n\t\t\t\tline-height: 1.5;\n\t\t\t\tmargin-bottom: 20px;\n\t\t\t}\n\t\t\ta {\n\t\t\t\tdisplay: inline-block;\n\t\t\t\tpadding: 10px 20px;\n\t\t\t\tbackground-color: #333;\n\t\t\t\tcolor: #fff;\n\t\t\t\ttext-decoration: none;\n\t\t\t\tborder-radius: 5px;\n\t\t\t\tmargin-top: 20px;\n\t\t\t}\n\t\t</style>\n\t</head>\n\t<body>\n\t\t<div class="container">\n\t\t\t<h2>Get Started with Course Creator 360</h2>\n\t\t\t<p>Dear [Name],</p>\n\t\t\t<p>Are you ready to get started with Course Creator 360? We’re here to help you every step of the way.</p>\n\t\t\t<p>Course Creator 360 is a course creation platform that allows you to create and sell courses online. With our platform, you can easily create and manage courses, track student progress, and even monetize your courses.</p>\n\t\t\t<p>We understand that you may have limited time and resources, so we have designed our platform to be as user-friendly and efficient as possible. With Course Creator 360, you can quickly and easily create and manage courses, track student progress, and even monetize your courses.</p>\n\t\t\t<a href="#">Sign Up Today</a>\n\t\t</div>\n\t</body>\n</html>', '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<style>\n\t\t\t.container {\n\t\t\t\tmax-width: 600px;\n\t\t\t\tmargin: 0 auto;\n\t\t\t\tpadding: 20px;\n\t\t\t\ttext-align: center;\n\t\t\t\tfont-family: Arial, sans-serif;\n\t\t\t}\n\t\t\th2 {\n\t\t\t\tfont-size: 26px;\n\t\t\t\tfont-weight: bold;\n\t\t\t\tmargin-bottom: 20px;\n\t\t\t}\n\t\t\tp {\n\t\t\t\tfont-size: 16px;\n\t\t\t\tline-height: 1.5;\n\t\t\t\tmargin-bottom: 20px;\n\t\t\t}\n\t\t\ta {\n\t\t\t\tdisplay: inline-block;\n\t\t\t\tpadding: 10px 20px;\n\t\t\t\tbackground-color: #2ab27b;\n\t\t\t\tcolor: #fff;\n\t\t\t\ttext-decoration: none;\n\t\t\t\tborder-radius: 5px;\n\t\t\t\tmargin-top: 20px;\n\t\t\t}\n\t\t</style>\n\t</head>\n\t<body>\n\t\t<div class="container">\n\t\t\t<h2>Unlock Your Potential with Course Creator Pro and Course Creator 360</h2>\n\t\t\t<p>Dear [Name],</p>\n\t\t\t<p>Are you looking to unlock your potential and become an expert in a particular subject or topic? If so, then Course Creator Pro and Course Creator 360 are the perfect tools for you!</p>\n\t\t\t<p>Course Creator Pro and Course Creator 360 are course creation platforms that allow you to create and sell courses online. With Course Creator Pro and Course Creator 360, you can easily create and manage courses, track student progress, and even monetize your courses.</p>\n\t\t\t<p>Course Creator Pro and Course Creator 360 provide you with access to high-quality education, no matter your time constraints or resources. With our platform, you can learn new skills, gain knowledge, and become an expert in a particular subject or topic.</p>\n\t\t\t<a href="#">Get Started Today</a>\n\t\t</div>\n\t</body>\n</html>']
# ['Subject: Unock Your Course Creation Potential with Course Creator Pro\\Dear [Name],\\Are you looking to create and launch your own successful online course? If so, I have the perfect solution for you.\\Introducing Course Creator Pro – a comprehensive course that teaches you everything you need to know about creating and launching your own online course. With our step-by-step guide, templates, and resources, you’ll be able to get started quickly and easily.\\Learn how to create an engaging course that will attract students and generate revenue. Get access to our exclusive resources and learn from our experienced instructors. With Course Creator Pro, you’ll have all the tools you need to become a successful online course creator.\\Learn more about Course Creator Pro today and unlock your course creation potential.\\Sincerely, \\[Your Name]', 'Subject Line: Get Started with Course Creator 360\\Dear [Name],\\Are you ready to get started with Course Creator 360? We’re here to help you every step of the way.\\Course Creator 360 is a course creation platform that allows you to create and sell courses online. With our platform, you can easily create and manage courses, track student progress, and even monetize your courses.\\We understand that you may have limited time and resources, so we have designed our platform to be as user-friendly and efficient as possible. With Course Creator 360, you can quickly and easily create and manage courses, track student progress, and even monetize your courses.\\Take the first step towards unlocking your potential and sign up for Course Creator 360 today.\\Sincerely,\\Stockton Walbeck\\Course Creator Pro', 'Subject Line: Unlock Your Potential with Course Creator Pro and Course Creator 360\\Dear [Name],\\Are you looking to unlock your potential and become an expert in a particular subject or topic? If so, then Course Creator Pro and Course Creator 360 are the perfect tools for you!\\Course Creator Pro and Course Creator 360 are course creation platforms that allow you to create and sell courses online. With Course Creator Pro and Course Creator 360, you can easily create and manage courses, track student progress, and even monetize your courses.\\Course Creator Pro and Course Creator 360 provide you with access to high-quality education, no matter your time constraints or resources. With our platform, you can learn new skills, gain knowledge, and become an expert in a particular subject or topic.\\So, what are you waiting for? Unlock your potential and become an expert with Course Creator Pro and Course Creator 360 today!\\Sincerely,\\Stockton Walbeck']
