# practicing if-statement with function

def question():
    rules = input("You need to answer every question by yes or no. Do you understand? : ")
    if rules.lower() != "yes":
        print("Try again.")
        return  # stop and exit the function
    else:
        print("Next question.")

    quest1 = input("Are you hungry? : ")
    if quest1.lower() != "yes":
        print("Then let's go for a walk.")
        return
    else:
        print("Next question.")

    quest2 = input("Do you want to eat at a restaurant? : ")
    if quest2.lower() != "yes":
        print("Come eat at my place.")
        return
    else:
        print("Next question.")

    quest3 = input("Do you want to eat a pizza? : ")
    if quest3.lower() != "yes":
        print("Let's go eat a burger then.")
    else:
        print("Let's go eat a pizza!")


# Call the function once
question()
