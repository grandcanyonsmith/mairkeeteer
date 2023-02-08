import sys

sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.get_values import get_background_information


class CustomerInformation:
    def __init__(self):
        self.desires = self.get_desires()
        self.target_audience = self.get_target_audience()
        self.pains = self.get_pains()
        self.target_demographic = self.get_target_demographic()
        self.display_information()

    def get_desires(self):
        values = get_background_information(info_name="target_audience")
        return (
            values["desires"]
            if values["desires"].strip()
            else input("What are the desires of your target audience? ")
        )

    def get_target_audience(self):
        values = get_background_information(info_name="target_audience")
        return (
            values["target_audience"]
            if values["target_audience"].strip()
            else input("Who is your target audience? ")
        )

    def get_pains(self):
        values = get_background_information(info_name="target_audience")
        return (
            values["pains"]
            if values["pains"].strip()
            else input("What are the pains of your target audience? ")
        )

    def get_target_demographic(self):
        values = get_background_information(info_name="target_audience")
        return (
            values["target_demographic"]
            if values["target_demographic"].strip()
            else input("What is the target demographic of your target audience? ")
        )

    def display_information(self):
        print("Target Audience: ", self.target_audience)
        print("Target Demographic: ", self.target_demographic)
        print("Desires: ", self.desires)
        print("Pains: ", self.pains)


if __name__ == "__main__":
    CustomerInformation()