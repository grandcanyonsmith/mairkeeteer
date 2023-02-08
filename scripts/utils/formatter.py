class StringFormatter:
    """
    A class that contains functions to format strings.
    """

    def __init__(self):
        pass

    def remove_digits_and_period_from_string(self, string: str) -> str:
        """
        Removes any leading digit or period from the given string and
        returns the modified string.
        """
        return string[2:] if string[0].isdigit() and string[1] == "." else string

    # if there is a number and : remove everything before the : for example: 1. hello -> hello
    def remove_colon_from_string(self, string: str) -> str:
        """
        Removes any leading colon from the given string and
        returns the modified string.
        """

        return string[string.index(":") + 1 :] if ":" in string else string

    def strip_string(self, string: str) -> str:
        """
        Strips the given string of any leading or trailing whitespace.
        """
        return string.strip()

    # remove empty strings
    def remove_empty_strings(self, list_of_strings: list) -> list:
        """
        Removes any empty strings from the given list of strings.
        """
        return [string for string in list_of_strings if string]

    def format_everything(self, list_of_strings: list) -> list:
        """
        Formats each string in the given list by removing any
        leading digit or period and capitalizing the first letter."""
        list_of_strings = self.remove_empty_strings(list_of_strings)
        list_of_strings = [
            self.remove_colon_from_string(string) for string in list_of_strings
        ]
        list_of_strings = [
            self.remove_digits_and_period_from_string(string)
            for string in list_of_strings
        ]
        list_of_strings = [self.strip_string(string) for string in list_of_strings]
        if "" in list_of_strings:
            list_of_strings.remove("")
        return [string.capitalize() for string in list_of_strings]
