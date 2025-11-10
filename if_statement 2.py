
# var1=3
# var2=3
# var3=2
#
# if var1==var2!=var3:
#     print("yes")
# else:
#     print("no")
#
# var1="blue"
# var2="red"
# var3="black"
# var4="yellow"
#
# if var1 == var2:
#     print("yes it's true")
# else:
#     print("no it's not true")

# ask user to enter there name and enter how much they have


pers1_name=input(" what is your name: ")
pers1_wallet=input(" how much money do you have : ")


pers2_name=input(" what is your name: ")
pers2_wallet=input(" how much money do you have : ")

pers3_name=input(" what is your name: ")
pers3_wallet=input(" how much money do you have : ")

if float(pers1_wallet)>float(pers2_wallet) and float(pers1_wallet) >float(pers2_wallet):
    print(pers1_name+ "is the richest")
elif float(pers2_wallet)>float(pers1_wallet) and float(pers2_wallet) >float(pers1_wallet):
    print(pers2_name+ "is the richest")
elif float(pers3_wallet) > float(pers1_wallet) and float(pers3_wallet) > float(pers1_wallet):
    print(pers3_name + "is the richest")
