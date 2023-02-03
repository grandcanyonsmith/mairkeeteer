import sys

sys.path.append("../..")  # Adds higher directory to python modules path.
from scripts.utils.get_values import get_background_information


class CompanyInformation:
    def __init__(self):
        self.name = self.get_name()
        self.company_name = self.get_company_name()
        self.product_name = self.get_product_name()
        self.product_description = self.get_product_description()
        self.desire = self.get_desire()
        self.common_mistake = self.get_common_mistake()
        self.ideal_market_avatar = self.get_ideal_market_avatar()
        self.common_enemy = self.get_common_enemy()
        self.everyday_person = self.get_everyday_person()
        self.well_known_experts = self.get_well_known_experts()
        self.realistic_time_frame = self.get_realistic_time_frame()
        self.common_occurrence = self.get_common_occurrence()
        self.consequence = self.get_consequence()
        self.traditional_way = self.get_traditional_way()
        self.ideal_person = self.get_ideal_person()
        self.painful_attempt = self.get_painful_attempt()
        self.relatable_pain_point = self.get_relatable_pain_point()
        self.commonly_used_vehicles = self.get_commonly_used_vehicles()
        self.solution = self.get_solution()
        self.hack_tool_trick = self.get_hack_tool_trick()
        self.common_achievement = self.get_common_achievement()
        self.perceived_experts = self.get_perceived_experts()
        self.current_year = self.get_current_year()
        self.easy_task = self.get_easy_task()
        self.biggest_objection = self.get_biggest_objection()
        # self.display_information()

    def get_name(self):
        values = get_background_information(info_name="company_info")
        return values[0] if values[0].strip() else input("What is your name? ")

    def get_company_name(self):
        values = get_background_information(info_name="company_info")
        return (
            values[1]
            if values[1].strip()
            else input("What is the name of your company? ")
        )

    def get_product_name(self):
        values = get_background_information(info_name="company_info")
        return (
            values[2]
            if values[2].strip()
            else input("What is the name of your product? ")
        )

    def get_product_description(self):
        values = get_background_information(info_name="company_info")
        return (
            values[3]
            if values[3].strip()
            else input("What is the description of your product? ")
        )

    def get_desire(self):
        values = get_background_information(info_name="company_info")
        return (
            values[4]
            if values[4].strip()
            else input("What is the desire of your target market? ")
        )

    def get_common_mistake(self):
        values = get_background_information(info_name="company_info")
        return (
            values[5]
            if values[5].strip()
            else input("What is the most common mistake made by your target market? ")
        )

    def get_ideal_market_avatar(self):
        values = get_background_information(info_name="company_info")
        return (
            values[6]
            if values[6].strip()
            else input("Who is your ideal market avatar? ")
        )

    def get_common_enemy(self):
        values = get_background_information(info_name="company_info")
        return (
            values[7]
            if values[7].strip()
            else input("What is the common enemy of your target market? ")
        )

    def get_everyday_person(self):
        values = get_background_information(info_name="company_info")
        return (
            values[8]
            if values[8].strip()
            else input("Who is the everyday person in your target market? ")
        )

    def get_well_known_experts(self):
        values = get_background_information(info_name="company_info")
        return (
            values[9]
            if values[9].strip()
            else input("Who are the well-known experts in your target market? ")
        )

    def get_realistic_time_frame(self):
        values = get_background_information(info_name="company_info")
        return (
            values[10]
            if values[10].strip()
            else input(
                "What is the realistic time frame for achieving success in your target market? "
            )
        )

    def get_common_occurrence(self):
        values = get_background_information(info_name="company_info")
        return (
            values[11]
            if values[11].strip()
            else input("What is the most common occurrence in your target market? ")
        )

    def get_consequence(self):
        values = get_background_information(info_name="company_info")
        return (
            values[12]
            if values[12].strip()
            else input(
                "What is the consequence of the common occurrence in your target market? "
            )
        )

    def get_traditional_way(self):
        values = get_background_information(info_name="company_info")
        return (
            values[13]
            if values[13].strip()
            else input(
                "What is the traditional way of achieving success in your target market? "
            )
        )

    def get_ideal_person(self):
        values = get_background_information(info_name="company_info")
        return (
            values[14]
            if values[14].strip()
            else input(
                "Who is the ideal person to achieve success in your target market? "
            )
        )

    def get_painful_attempt(self):
        values = get_background_information(info_name="company_info")
        return (
            values[15]
            if values[15].strip()
            else input(
                "What is the most painful attempt to achieve success in your target market? "
            )
        )

    def get_relatable_pain_point(self):
        values = get_background_information(info_name="company_info")
        return (
            values[16]
            if values[16].strip()
            else input("What is the most relatable pain point in your target market? ")
        )

    def get_commonly_used_vehicles(self):
        values = get_background_information(info_name="company_info")
        return (
            values[17]
            if values[17].strip()
            else input(
                "What are the commonly used vehicles to achieve success in your target market? "
            )
        )

    def get_solution(self):
        values = get_background_information(info_name="company_info")
        return (
            values[18]
            if values[18].strip()
            else input("What is the solution to the pain point in your target market? ")
        )

    def get_hack_tool_trick(self):
        values = get_background_information(info_name="company_info")
        return (
            values[19]
            if values[19].strip()
            else input(
                "What is the hack, tool, or trick to achieve success in your target market? "
            )
        )

    def get_common_achievement(self):
        values = get_background_information(info_name="company_info")
        return (
            values[20]
            if values[20].strip()
            else input("What is the most common achievement in your target market? ")
        )

    def get_perceived_experts(self):
        values = get_background_information(info_name="company_info")
        return (
            values[21]
            if values[21].strip()
            else input("Who are the perceived experts in your target market? ")
        )

    def get_current_year(self):
        values = get_background_information(info_name="company_info")
        return values[22] if values[22].strip() else input("What is the current year? ")

    def get_easy_task(self):
        values = get_background_information(info_name="company_info")
        return (
            values[23]
            if values[23].strip()
            else input(
                "What is the easiest task to achieve success in your target market? "
            )
        )

    def get_biggest_objection(self):
        values = get_background_information(info_name="company_info")
        return (
            values[24]
            if values[24].strip()
            else input(
                "What is the biggest objection to achieving success in your target market? "
            )
        )

    # def display_information(self):
    #     print("Name:", self.name)
    #     print("Company Name:", self.company_name)
    #     print("Product Name:", self.product_name)
    #     print("Product Description:", self.product_description)
    #     print("Desire:", self.desire)
    #     print("Common Mistake:", self.common_mistake)
    #     print("Ideal Market Avatar:", self.ideal_market_avatar)
    #     print("Common Enemy:", self.common_enemy)
    #     print("Everyday Person:", self.everyday_person)
    #     print("Well-Known Experts:", self.well_known_experts)
    #     print("Realistic Time Frame:", self.realistic_time_frame)
    #     print("Common Occurrence:", self.common_occurrence)
    #     print("Consequence:", self.consequence)
    #     print("Traditional Way:", self.traditional_way)
    #     print("Ideal Person:", self.ideal_person)
    #     print("Painful Attempt:", self.painful_attempt)
    #     print("Relatable Pain Point:", self.relatable_pain_point)
    #     print("Commonly Used Vehicles:", self.commonly_used_vehicles)
    #     print("Solution:", self.solution)
    #     print("Hack/Tool/Trick:", self.hack_tool_trick)
    #     print("Common Achievement:", self.common_achievement)
    #     print("Perceived Experts:", self.perceived_experts)
    #     print("Current Year:", self.current_year)
    #     print("Easy Task:", self.easy_task)
    #     print("Biggest Objection:", self.biggest_objection)
