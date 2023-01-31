import json
import termcolor


def get_email_sequence_types():
    with open("email_sequence_types.jsonl", "r") as f:
        email_sequence_types = [json.loads(line) for line in f]
    return email_sequence_types


def print_email_sequence_types(email_sequence_types):
    email_sequence_types_list = []
    for email_sequence_type in email_sequence_types:
        purpose = email_sequence_type["purpose"]
        email_type = email_sequence_type["email_sequence_type"]
        email_sequence_types_list.append(f"{email_type} - {purpose}")
    add_numbers_to_list(email_sequence_types_list)
    for email_sequence_type in email_sequence_types_list:
        print(email_sequence_type)
    return email_sequence_types_list


def add_numbers_to_list(email_sequence_types_list):
    for i, email_sequence_type in enumerate(email_sequence_types_list):
        email_sequence_type = f"{i + 1}. {email_sequence_type}"
        email_sequence_types_list[i] = email_sequence_type
    return email_sequence_types_list


def get_email_sequence_type(email_sequence_types_list):
    email_sequence_type = input("What type of email sequence will you be creating? ")
    if email_sequence_type.isdigit():
        if int(email_sequence_type) <= len(email_sequence_types_list):
            return email_sequence_types_list[int(email_sequence_type) - 1]

    else:
        if email_sequence_type in email_sequence_types_list:
            return email_sequence_type
        print("Invalid email sequence type. Please try again.")
        return get_email_sequence_type(email_sequence_types_list)

def split_email_sequence_type(email_sequence_type):
    email_sequence_type = email_sequence_type.split(" - ")
    return email_sequence_type

def get_email_sequence_from_user():
    email_sequence_types = get_email_sequence_types()
    email_sequence_types_list = print_email_sequence_types(email_sequence_types)
    email_sequence_type = get_email_sequence_type(email_sequence_types_list)
    email_sequence_type = split_email_sequence_type(email_sequence_type)
    
    email_sequence_type_string = termcolor.colored(email_sequence_type[0], "green") + " - " + email_sequence_type[1]
    print(email_sequence_type_string)
    return email_sequence_type


 


if __name__ == "__main__":
    get_email_sequence_from_user()
