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
        print(values)
        return (
            values["name"] if values["name"].strip() else input("What is your name? ")
        )

    def get_company_name(self):
        values = get_background_information(info_name="company_info")
        return (
            values["company_name"]
            if values["company_name"].strip()
            else input("What is the name of your company? ")
        )

    def get_product_name(self):
        values = get_background_information(info_name="company_info")
        return (
            values["product_name"]
            if values["product_name"].strip()
            else input("What is the name of your product? ")
        )

    def get_product_description(self):
        values = get_background_information(info_name="company_info")
        return (
            values["product_description"]
            if values["product_description"].strip()
            else input("What is the description of your product? ")
        )

    def get_desire(self):
        values = get_background_information(info_name="company_info")
        return (
            values["desire"]
            if values["desire"].strip()
            else input("What is the desire of your target market? ")
        )

    def get_common_mistake(self):
        values = get_background_information(info_name="company_info")
        return (
            values["common_mistake"]
            if values["common_mistake"].strip()
            else input("What is the most common mistake made by your target market? ")
        )

    def get_ideal_market_avatar(self):
        values = get_background_information(info_name="company_info")
        return (
            values["ideal_person"]
            if values["ideal_person"].strip()
            else input("Who is your ideal market avatar? ")
        )

    def get_common_enemy(self):
        values = get_background_information(info_name="company_info")
        return (
            values["common_enemy"]
            if values["common_enemy"].strip()
            else input("What is the common enemy of your target market? ")
        )

    def get_everyday_person(self):
        values = get_background_information(info_name="company_info")
        return (
            values["everyday_person"]
            if values["everyday_person"].strip()
            else input("Who is the everyday person in your target market? ")
        )

    def get_well_known_experts(self):
        values = get_background_information(info_name="company_info")
        return (
            values["well_known_experts"]
            if values["well_known_experts"].strip()
            else input("Who are the well-known experts in your target market? ")
        )

    def get_realistic_time_frame(self):
        values = get_background_information(info_name="company_info")
        return (
            values["realistic_time_frame"]
            if values["realistic_time_frame"].strip()
            else input(
                "What is the realistic time frame for achieving success in your target market? "
            )
        )

    def get_common_occurrence(self):
        values = get_background_information(info_name="company_info")
        return (
            values["common_occurrence"]
            if values["common_occurrence"].strip()
            else input("What is a common occurrence in your target market? ")
        )

    def get_consequence(self):
        values = get_background_information(info_name="company_info")
        return (
            values["consequence"]
            if values["consequence"].strip()
            else input("What is the consequence of this common occurrence? ")
        )

    def get_traditional_way(self):
        values = get_background_information(info_name="company_info")
        return (
            values["traditional_way"]
            if values["traditional_way"].strip()
            else input("What is the traditional way of solving this problem? ")
        )

    def get_ideal_person(self):
        values = get_background_information(info_name="company_info")
        return (
            values["ideal_person"]
            if values["ideal_person"].strip()
            else input("Who is the ideal person to solve this problem? ")
        )

    def get_painful_attempt(self):
        values = get_background_information(info_name="company_info")
        return (
            values["painful_attempt"]
            if values["painful_attempt"].strip()
            else input("What is a painful attempt to solve this problem? ")
        )

    def get_relatable_pain_point(self):
        values = get_background_information(info_name="company_info")
        return (
            values["relatable_pain_point"]
            if values["relatable_pain_point"].strip()
            else input("What is a relatable pain point in your target market? ")
        )

    def get_commonly_used_vehicles(self):
        values = get_background_information(info_name="company_info")
        return (
            values["commonly_used_vehicles"]
            if values["commonly_used_vehicles"].strip()
            else input("What are the commonly used vehicles in your target market? ")
        )

    def get_solution(self):
        values = get_background_information(info_name="company_info")
        return (
            values["solution"]
            if values["solution"].strip()
            else input("What is the solution? ")
        )

    def get_hack_tool_trick(self):
        values = get_background_information(info_name="company_info")
        return (
            values["hack_tool_trick"]
            if values["hack_tool_trick"].strip()
            else input("What is the hack/tool/trick? ")
        )

    def get_common_achievement(self):
        values = get_background_information(info_name="company_info")
        return (
            values["common_achievement"]
            if values["common_achievement"].strip()
            else input("What is a common achievement in your target market? ")
        )

    def get_perceived_experts(self):
        values = get_background_information(info_name="company_info")
        return (
            values["perceived_experts"]
            if values["perceived_experts"].strip()
            else input("Who are the perceived experts in your target market? ")
        )

    def get_current_year(self):
        values = get_background_information(info_name="company_info")
        return (
            values["current_year"]
            if values["current_year"].strip()
            else input("What is the current year? ")
        )

    def get_easy_task(self):
        values = get_background_information(info_name="company_info")
        return (
            values["easy_task"]
            if values["easy_task"].strip()
            else input("What is an easy task in your target market? ")
        )

    def get_biggest_objection(self):
        values = get_background_information(info_name="company_info")
        return (
            values["biggest_objection"]
            if values["biggest_objection"].strip()
            else input("What is the biggest objection in your target market? ")
        )
