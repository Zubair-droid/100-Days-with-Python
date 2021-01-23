
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

operations = { 
 "+" : add,
 "-" : subtract,
 "*" : multiply,
 "/" : divide
 }

def calculator():
  print(logo)
  num1 = float(input("What is your first number?: \n"))
  for operator in operations:
    print (operator) # this piece of code targets the key

  to_continue = True
  while to_continue:
    operator = input("Which operation you want to carry?:\n ")
    num2 = float(input("What is your next number?: \n "))
    calculation_function = operations[operator] # this piece targets the value
    answer = calculation_function(num1, num2)
      
    print(f"{num1} {operator} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculator:\n ") == "y":
      num1 = answer
    else:
      to_continue = False
      calculator()
      

calculator()