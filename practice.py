# In this lesson we are going to create a small app that will allow us to calculate the
# price of each product and the quantity of the product bought


# create all the variable needed
price_product_1 =input("what is the price of the product 1:")
Quantity_product_1 = input("what will the the quantity of the product 1:")
price_product_2 = input("what is the price of the product 2:")
Quantity_product_2 = input("what will the the quantity of the product 2:")
price_product_3 = input("what is the price of the product 3:")
Quantity_product_3 = input("what will the the quantity of the product 3:")

result_product_1=float(price_product_1)*float(Quantity_product_1)
result_product_2=float(price_product_2)*float(Quantity_product_2)
result_product_3=float(price_product_3)*float(Quantity_product_3)
result = result_product_1+result_product_2+result_product_3
print("your total price is "+str(result))

