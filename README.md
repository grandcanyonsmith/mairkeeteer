### Example desired output
# self.steps = ["Introduction", "Features", "Benefits", "Call to Action"]
# self.subject_lines = ["Introducing Our New Product", "Discover the Features of Our Product", "Unlock the Benefits of Our Product", "Take Action Now and Try Our Product"]
# self.value_propositions = ["Save Time and Increase Efficiency", "Improve Quality and Reduce Costs", "Get Ahead of the Competition", "Experience Exceptional Customer Service"]
# self.ctas = ["Sign Up Now", "Learn More", "Try it for Free", "Buy Now"]

# After all the those lists are created, you can use them to create a dictionary of lists like this:
# self.emails = { "steps": self.steps, "subject_lines": self.subject_lines, "value_propositions": self.value_propositions, "ctas": self.ctas }

# Then you can use the dictionary to create a list of dictionaries like this:
# self.emails = [ { "step": self.steps[i], "subject_line": self.subject_lines[i], "value_proposition": self.value_propositions[i], "cta": self.ctas[i] } for i in range(len(self.steps)) ]

# this will then be used to create however many emails the user requests





# TODO: Create a list of dictionaries that contains the email content for each email
# HINT: The list of dictionaries should look like this:
# [
#     {
#         "step": "Introduction",
#         "subject_line": "Introducing Our New Product",
#         "value_proposition": "Save Time and Increase Efficiency",
#         "cta": "Sign Up Now"
#     },
#     { 
#         "step": "Features",
#         "subject_line": "Discover the Features of Our Product",
#         "value_proposition": "Improve Quality and Reduce Costs",
#         "cta": "Learn More"
#     },
#     {
#         "step": "Benefits",
#         "subject_line": "Unlock the Benefits of Our Product",
