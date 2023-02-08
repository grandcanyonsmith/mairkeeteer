Flow of the project

1. Get the background information from the user
2. Get the company target demographic
3. Get the company target market
4. Use this infromation as the background info to be able to create the components of the email in the following order:
Steps > *Subject line/Hook* > Value Proposition > Call to Action > then create the whole email
5. After components of dictionaries are added to **mairkeeteer/files/data/temp/temp.jsonl* from step 4 add create the whol email and add it to **mairkeeteer/files/data/temp/temp_email.jsonl**
6. Then Convert that email into a markdown file and add it to **mairkeeteer/files/data/temp/temp_email.md**



Visualisation 

Below is a prompt that we sent to OPENAI/GPT-3. It shows how the order of operations listed above works.
""""
"""
<!-- Example Prompt: -->
{ 
  "company_info": {
    "name": "Stockton Walbeck",
    "company_name": "Course Creator Pro",
    "product_name": "Course Creator 360",
    "product_description": "We sell a platform that helps people sell their own courses online",
    "desire": "Course creation",
    "common_mistake": "Not having the right tools to create and sell courses",
    "ideal_market_avatar": "Business owners, entrepreneurs, and professional educators",
    "common_enemy": "Poor course creation platforms",
    "everyday_person": "People looking to create and sell courses online",
    "well_known_experts": "Course creation professionals, online entrepreneurs",
    "realistic_time_frame": "Varies depending on the complexity of the course",
    "common_occurrence": "Challenges with creating and selling courses online",
    "consequence": "Poorly designed courses that don't attract buyers",
    "traditional_way": "Developing courses through trial and error",
    "ideal_person": "Someone with experience in course creation and marketing",
    "painful_attempt": "Trying to create and market a course without the right tools",
    "relatable_pain_point": "Difficulty in finding the right tools to create and market courses",
    "commonly_used_vehicles": "Online course creation platforms, webinars, and eBooks",
    "solution": "Course Creator 360",
    "hack_tool_trick": "Creating courses quickly and easily with Course Creator 360",
    "common_achievement": "Successfully creating and selling a course online",
    "perceived_experts": "Course creators and marketers who have had success with their courses",
    "current_year": "2023",
    "easy_task": "Creating and selling a course with Course Creator 360",
    "biggest_objection": "Not having enough time or experience to create and market a course"
  }, 
  "target_audience": {
    "desires": "To learn new skills, gain knowledge, become an expert in a particular subject and/or topic.",
    "target_audience": "Males",
    "pains": "A lack of access to high-quality education, time constraints, and limited resources.",
    "target_demographic": "Individuals of all ages and backgrounds, with a particular focus on entrepreneurs and professionals."
  }
}


Write me a 5 sequence email campagin using the information above:

Write the steps of each email:

Step 1: Introduction
Step 2: Establish Credibility
Step 3: Explain the Problem
Step 4: Introduce the Solution
Step 5: Call to Action


Write a subjectline for each of those steps:

Step 1: Introduction - Welcome to Course Creator Pro!
Step 2: Establish Credibility - Unlock Your Course Creation Potential
Step 3: Explain the Problem - Overcome the Challenges of Course Creation
Step 4: Introduce the Solution - Introducing Course Creator 360
Step 5: Call to Action - Take Control of Your Course Creation Today!


Write a value propsotion for each email:

Step 1: Introduction - Get the tools you need to create and sell courses quickly and easily with Course Creator Pro.
Step 2: Establish Credibility - Learn from experienced course creators and marketers who have created successful courses.
Step 3: Explain the Problem - Stop wasting time and resources on traditional course creation methods and start using proven tools.
Step 4: Introduce the Solution - Get access to the Course Creator 360 platform, which allows you to create, market, and sell courses with ease. 
Step 5: Call to Action - Take control of your course creation today and unlock the potential of your knowledge and skills!


Write a CTA for each email:

Step 1: Introduction - Sign up for Course Creator Pro today!
Step 2: Establish Credibility - Learn from the experts!
Step 3: Explain the Problem - Start creating courses now!
Step 4: Introduce the Solution - Try Course Creator 360 today!
Step 5: Call to Action - Take control of your course creation!


Write each email below:

Email 1 - Introduction

Subject: Welcome to Course Creator Pro!

Hello, 

Are you looking to create and sell courses online with ease? Look no further than Course Creator Pro, the best platform for creating and selling courses quickly and easily. With Course Creator Pro, you will have all the tools you need to start creating amazing courses that will attract buyers. 

Sign up for Course Creator Pro today to get started on your journey to success! 

Cheers,
Stockton Walbeck
""""






<!-- Milestone 1: -->
Your file
**mairkeeteer/files/data/temp/temp.jsonl**
`Should look like this`
```
{"step": "Reminder of items left in the cart", "step_number": 1, "call_to_action": "Click the link below to complete your purchase of course creator pro and start learning how to create and sell online courses today!", "hook": "\n\"Unlock the Secrets to Course Creation and Selling!\"", "value_proposition": "With course creator pro, you can quickly and easily create high-quality online courses that will help you reach your goals and make more money. our course creator platform is designed to make the process of creating and selling courses easier than ever before. with our step-by-step guidance, you can create a course that will help you reach your goals faster and with less effort. invest in yourself today and start creating the course of your dreams with course creator pro."}
{"step": "Offer a discount or incentive to complete the purchase", "step_number": 2, "call_to_action": "Take advantage of this limited-time offer and get instant access to course creator pro today!", "hook": "\n\"Unlock the Secrets to Course Creation and Selling!\"", "value_proposition": "Are you ready to take your online course business to the next level? with course creator pro, you can create and launch your own online courses quickly and easily. plus, for a limited time, we're offering a special discount on our course so you can get started today!"}
{"step": "Final reminder and call to action to complete the purchase", "step_number": 3, "call_to_action": "Act now and get instant access to course creator pro! unlock the secrets to creating and selling successful online courses and start making money today!", "hook": "\n\"Unlock the Secrets to Course Creation and Selling!\"", "value_proposition": "With course creator pro, you can learn the skills and strategies you need to create and launch your own successful online course. get started today and start making money from your own online course!"}
```

<!-- Milestone 2: -->
Your file
**mairkeeteer/files/data/temp/temp_email.jsonl**
`Should look like this`
{"Email": "Dear [Name],\n\nWe hope you're doing well! We noticed that you left some items in your shopping cart and wanted to remind you that they're still there waiting for you. Don't miss out on this opportunity to get the perfect solution for creating and selling your own online courses. \n\nCourse Creator Pro provides step-by-step guidance, helpful resources, and expert advice to help you get started quickly and easily. Plus, with our money-back guarantee, you can be sure that you're making a safe investment. \n\nFor a limited time only, we are offering a discount on Course Creator Pro. Unlock your expertise now and get a discount on your purchase! \n\nDon't miss out! Complete your purchase now. \n\nSincerely, \n[Your Name]"}
{"Email": "Dear [Name],\n\nWe noticed that you left some items in your shopping cart and wanted to remind you that you can still complete your purchase. Don't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nCourse Creator Pro is the perfect solution for anyone looking to create and sell their own online courses. It provides step-by-step guidance, helpful resources, and expert advice to help you get started quickly and easily. Plus, with our money-back guarantee, you can be sure that you're making a safe investment.\n\nFor a limited time only, we are offering a discount on Course Creator Pro. Take advantage of this offer now and save money on your purchase.\n\nDon't miss out! Complete your purchase now and unlock your expertise with Course Creator Pro.\n\nSincerely, \n[Your Name]"}

<!-- Milestone 3: -->
Rendered Email Appears automatically when you click the button below
``