#!/usr/bin/python3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Enter the operator(+, -, *, /, %): ")

match operator:
  case '+':
      print(f"The sum of both number are: {num1+num2}")
  case '-':
      print(f"The sum of both number are: {num1-num2}")
  case '*':
      print(f"The sum of both number are: {num1*num2}")
  case '/':
      print(f"The sum of both number are: {num1/num2}")
  case '%':
      print(f"The sum of both number are: {num1%num2}")
  case _:
      print("Invalid Operator.")