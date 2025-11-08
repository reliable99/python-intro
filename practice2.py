name_1=input("what is your name?:")
name_2=input("what is your name?:")
name_3=input("what is your name?:")

Slices_in_the_pizza=input("How many slices in the pizza?:")
Price_of_the_pizza=input("What's the price of the pizza?:")

Percentage_ate_by_person_1=input(name_1+"What percentage of the pizza you have ate?")
Percentage_ate_by_person_2=input(name_2+"What percentage of the pizza you have ate?")
Percentage_ate_by_person_3=input(name_3+"What percentage of the pizza you have ate?")


# percentage of slices ate by each person
number_of_slices_ate_person_1=float(Percentage_ate_by_person_1)*float(Slices_in_the_pizza)
number_of_slices_ate_person_2=float(Percentage_ate_by_person_2)*float(Slices_in_the_pizza)
number_of_slices_ate_person_3=float(Percentage_ate_by_person_3)*float(Slices_in_the_pizza)

# Prices paid by each person
Price_paid_by_name_1= float(Percentage_ate_by_person_1)*float(Price_of_the_pizza)
Price_paid_by_name_2= float(Percentage_ate_by_person_2)*float(Price_of_the_pizza)
Price_paid_by_name_3= float(Percentage_ate_by_person_3)*float(Price_of_the_pizza)

print(name_1 + " has eaten " + str(number_of_slices_ate_person_1) +
      " slices and has paid " + str(Price_paid_by_name_1) + " $ for this meal.")

print(name_2 + " has eaten " + str(number_of_slices_ate_person_2) +
      " slices and has paid " + str(Price_paid_by_name_2) + " $ for this meal.")

print(name_3 + " has eaten " + str(number_of_slices_ate_person_3) +
      " slices and has paid " + str(Price_paid_by_name_3) + " $ for this meal.")
