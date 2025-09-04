import math 
# () We are helping people find the circumference and areao of a circle using python's math module

radius = float(input("Enter the radius of a circle: "))

circumferance = 2 * math.pi * radius
area = math.pi *pow(radius, 2)

print(f"The circumference is : {round(circumferance, 2)} cm")
print(f"The area of the circle is: {round(area, 2)}cm^2")

# () We are finding the hipotenuse of a right triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow (b,2))

print(f"Side C = {c}")
