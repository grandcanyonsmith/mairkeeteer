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
        
        return string[1:] if string[0].isdigit() or string.startswith(".") else string

    def format_everything(self, list_of_strings: list) -> list:
        """
        Formats each string in the given list by removing any 
        leading digit or period and capitalizing the first letter."""
        
        return [self.remove_digits_and_period_from_string(string).capitalize() for string in list_of_strings]
