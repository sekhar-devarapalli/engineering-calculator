import math

def convert_units():
    print("\n1) mm to inches")
    print("2) inches to mm")
    print("3) kg to Newtons")
    choice = input("Choose: ")
    value = float(input("Enter value: "))
    if choice == "1":
        print(f"{value} mm = {value / 25.4:.3f} inches")
    elif choice == "2":
        print(f"{value} inches = {value * 25.4:.3f} mm")
    elif choice == "3":
        print(f"{value} kg = {value * 9.81:.2f} N")
    else:
        print("Invalid choice")

def stress():
    force = float(input("Force in Newtons: "))
    area = float(input("Area in mm^2: "))
    print(f"Stress = {force / area:.2f} MPa")

def circle_area():
    d = float(input("Diameter in mm: "))
    print(f"Area = {math.pi * (d / 2) ** 2:.2f} mm^2")

while True:
    print("\n--- Engineering Calculator ---")
    print("1) Unit converter")
    print("2) Stress calculator")
    print("3) Circle area")
    print("4) Exit")
    option = input("Choose: ")
    if option == "1":
        convert_units()
    elif option == "2":
        stress()
    elif option == "3":
        circle_area()
    elif option == "4":
        break
    else:
        print("Invalid choice")
