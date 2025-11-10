# return practically ends the execution of function

def calculate(a, b, c):
    print(a + b + c)
    print("This is a calculation")
    return print(a - b - c)
    print(a * b / c)

calculate(1, 2, 3)
