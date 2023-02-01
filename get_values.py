import json


def open_info_json():
    with open("info.jsonl") as json_file:
        data = json.load(json_file)
        name = data["company_info"]["name"]
        company_name = data["company_info"]["company_name"]
        product_name = data["company_info"]["product_name"]
        product_description = data["company_info"]["product_description"]
        return name, company_name, product_name, product_description
    
def open_info_json_target_demographic():
    with open("info.jsonl") as json_file:
        data = json.load(json_file)
        desires = data["target_audience"]["desires"]
        target_audience = data["target_audience"]["target_audience"]
        pains = data["target_audience"]["pains"]
        target_demographic = data["target_audience"]["target_demographic"]
        return desires, target_audience, pains, target_demographic

def get_hooks_examples_from_file():
    questions = []

    with open("hook_examples.jsonl", "r") as f:
        for line in f:
            data = json.loads(line)
            questions.append(data["hook"])

    return "\n".join(questions)

