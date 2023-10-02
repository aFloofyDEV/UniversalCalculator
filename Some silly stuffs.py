# Some silly stuffs

def func(option):
    pi = 3.14159265358979
    if option == 2:
        radius = float(input("Input the circles radius: "))
        circumference = 2 * pi * radius
        print("The circumference is equal to:", round(circumference, 2))
    if option == 1:
        circumference = float(input("Input the circles circumference: "))
        radius = circumference / (2 * pi)
        print("The radius is equal to:", round(radius, 2))

print("Welcome to Floof's universal calculator\u2122 Prototype 1\n\n")
optionOut = int(input("1: Calculate radius from circumference\n2: Calculate circumference from radius\nOption: "))
func(optionOut)

input()
