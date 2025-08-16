# This is a temperature conversion program

temp = float(input("Enter the current weather outside: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): ")

if unit == "F":
    temp = (temp - 32) *5/9
    unit = "Celsius"
    print(f"Your current temperature converted to {unit} is {round(temp, 2)}")
elif unit == "C":
    temp = (temp *9/5) + 32
    unit = "Degrees"
    print(f"Your current temperature converted to {unit} is {round(temp, 2)}")

else: 
    print(f"{unit} is an invalid unit of measurement")
