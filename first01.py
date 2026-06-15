print("---Area Calculator---")
print("1.Rectangle 2.Triangle 3.Circle")

choice = input("Select an option(1 or 2 or 3):")

if choice == "1":
    width = float(input("Enter the width:"))
    length = float(input("Enter the length"))
    area = width*length
    print(f"The area of the rectangle is:{area:.2f}square units")

elif choice == "2":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("The area of the triangle is:", 0.5 * base * height)

elif choice == "3":
    radius = float(input("Enter raduis: "))
    area = math.pi * (radius ** 2)
    print("The area of the circle is:", math.pi * (radius ** 2))

