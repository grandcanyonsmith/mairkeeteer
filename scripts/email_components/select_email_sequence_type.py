import json


def get_email_sequence_types():
    """
    Reads the email sequence types from the file.
    """
    with open("/Users/canyons/Documents/GitHub/mairkeeteer/files/data/examples/email_sequence_types.jsonl", "r") as f:
        return [json.loads(line) for line in f]
    


def print_email_sequence_types(email_sequence_types):
    """
    Prints the email sequence types to the console.
    """
    email_sequence_types = [f"{i + 1}. {email_sequence_type['email_sequence_type']} - {email_sequence_type['purpose']}" for i, email_sequence_type in enumerate(email_sequence_types)]
    print("\n".join(email_sequence_types))
    return email_sequence_types


def get_email_sequence_type(email_sequence_types):
    """
    Gets the email sequence type from the user.
    """
    while True:
        email_sequence_type = input("What type of email sequence will you be creating? ")
        if email_sequence_type.isdigit():
            if int(email_sequence_type) <= len(email_sequence_types):
                return email_sequence_types[int(email_sequence_type) - 1]
        elif email_sequence_type in email_sequence_types:
            return email_sequence_type
        print("Invalid email sequence type. Please try again.\n")


def split_email_sequence_type(email_sequence_type):
    """
    Splits the email sequence type into a list.
    """
    return email_sequence_type.split(" - ")


def get_email_sequence_from_user():
    """
    Gets the email sequence type from the user.
    """
    email_sequence_types = get_email_sequence_types()
    email_sequence_types = print_email_sequence_types(email_sequence_types)
    email_sequence_type = get_email_sequence_type(email_sequence_types)
    email_sequence_type = split_email_sequence_type(email_sequence_type)
    email_sequence_type_string = f"{email_sequence_type[0]} - {email_sequence_type[1]}"
    print(email_sequence_type_string)
    return email_sequence_type


if __name__ == "__main__":
    get_email_sequence_from_user()
