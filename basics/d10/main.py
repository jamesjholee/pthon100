# D10 Exercise 1
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#         else:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     idx = month - 1
#     if if_leap(year) and month == 2:
#         return 29
#     else:
#         return month_days[idx]
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# D10 Project Calculator
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation")
        num2 = float(input("What's the second  number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}: ") == "y"
            num1 = answer
        else: 
            should_continue = False
            calculator()
calculator()