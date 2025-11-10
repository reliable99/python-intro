# def per_1(name):
#     print(name + ": Hello, how can I help you?")
#
#
# def person_2_1(food, drink, dessert, name ):
#     name = input("What is your name? : ")
#     food = input("What do you want to eat? : ")
#     drink = input("What do you want to drink? : ")
#     dessert = input("What dessert do you want? : ")
#
#     print(name + ": I would like the " + food + ", I want to drink " + drink + ", and I want " + dessert + " as dessert.")
#
#
# def per_1_2(name):
#     print(name + ": Thank you!")
#
#
# # ---- Function Calls ----
# per_1("Cashier")
# person_2_1("food", "drink", "dessert", "name")
# per_1_2("Cashier")

def interviewer_intro(name):
    print(name + ": Good morning, welcome to the interview session for the Software Developer position.")
    print(name + ": Can you please introduce yourself?")


def candidate_intro():
    name = input("What is your name? : ")
    experience = input("How many years of experience do you have in software development? : ")
    tech_stack = input("Which programming languages or frameworks are you most comfortable with? : ")

    print(
        f"{name}: Good morning! My name is {name}. I have {experience} years of experience in software development, and I'm proficient in {tech_stack}.")
    return name


def interviewer_questions(name):
    print("Interviewer: Great! Let's continue with some questions.")
    reason = input("Why do you want to work with our company? : ")
    strength = input("What are your key strengths as a developer? : ")
    project = input("Can you briefly describe a project you’re proud of? : ")

    print(f"{name}: I want to work here because {reason}.")
    print(f"{name}: My strengths are {strength}.")
    print(f"{name}: One project I’m proud of is {project}.")


def interviewer_closing(name):
    print("Interviewer: That was a great discussion.")
    print(f"Interviewer: Thank you, {name}, for your time. We’ll get back to you after reviewing your application.")
    print(f"{name}: Thank you for the opportunity! I look forward to hearing from you.")


# ---- Interview Flow ----
interviewer_intro("Interviewer")
candidate_name = candidate_intro()
interviewer_questions(candidate_name)
interviewer_closing(candidate_name)
