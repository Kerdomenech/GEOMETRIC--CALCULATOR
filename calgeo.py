# Manual constants
PI_VALUE = 3.14159

# Main Control Flag
is_active = True
print(" --- GEOMETRIC CALCULATOR ---")

while is_active:
    print("\n1. 2D Shapes")
    print("2. 3D Shapes")
    print("3. Exit")
    
    menu_choice = input("Select an option (1-3): ")

    if menu_choice == "1":
        print("\n--- 2D Shapes ---")
        print("a. Rectangle\nb. Right Triangle\nc. Circle\nd. Trapezoid\ne. Triangle")
        shape = input("Select a shape: ")
        
        # a. Rectangle
        if shape == "a":
            print(">> Rectangle Calculator")
            calc_type = input("Enter 'i' for area or 'ii' for perimeter: ")
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            if base > 0 and height > 0:
                if calc_type == "i":
                    print(f">> i. Area: {base * height:.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Perimeter: {2 * (base + height):.2f}")

        # b. Right Triangle
        elif shape == "b":
            print(">> Right Triangle Calculator")
            calc_type = input("Enter 'i' for Pythagorean theorem or 'ii' for perimeter: ")
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            if base > 0 and height > 0:
                hypotenuse = (base**2 + height**2) ** 0.5
                if calc_type == "i":
                    print(f">> i. Pythagorean Result (Hypotenuse): {hypotenuse:.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Perimeter: {base + height + hypotenuse:.2f}")

        # c. Circle
        elif shape == "c":
            print(">> Circle Calculator")
            calc_type = input("Enter 'i' for diameter or 'ii' for perimeter: ")
            radius = float(input("Enter Radius: "))
            if radius > 0:
                if calc_type == "i":
                    print(f">> i. Diameter: {2 * radius:.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Perimeter (Circumference): {2 * PI_VALUE * radius:.2f}")

        # d. Trapezoid
        elif shape == "d":
            print(">> Trapezoid Calculator")
            calc_type = input("Enter 'i' for area or 'ii' for perimeter: ")
            b1 = float(input("Enter Base A (Top): "))
            b2 = float(input("Enter Base B (Bottom): "))
            h = float(input("Enter Height: "))
            if b1 > 0 and b2 > 0 and h > 0:
                if calc_type == "i":
                    print(f">> i. Area: {((b1 + b2) / 2) * h:.2f}")
                elif calc_type == "ii":
                    side_slant = (h**2 + (abs(b1 - b2) / 2)**2)**0.5
                    print(f">> ii. Perimeter: {b1 + b2 + (2 * side_slant):.2f}")

        # e. General Triangle
        elif shape == "e":
            print(">> General Triangle Calculator")
            calc_type = input("Enter 'i' for area or 'ii' for perimeter: ")
            if calc_type == "i":
                base = float(input("Enter Base: "))
                height = float(input("Enter Height: "))
                print(f">> i. Area: {(base * height) / 2:.2f}")
            elif calc_type == "ii":
                s1 = float(input("Side 1: "))
                s2 = float(input("Side 2: "))
                s3 = float(input("Side 3: "))
                print(f">> ii. Perimeter: {s1 + s2 + s3:.2f}")

    elif menu_choice == "2":
        print("\n--- 3D Shapes ---")
        print("a. Prism (Rectangular)\nb. Sphere\nc. Cylinder\nd. Cone")
        shape_3d = input("Select a shape: ")

        # a. Prism
        if shape_3d == "a":
            l = float(input("Enter Length: "))
            w = float(input("Enter Width: "))
            h = float(input("Enter Height: "))
            calc_type = input("Enter 'i' for volume or 'ii' for surface area: ")
            if l > 0 and w > 0 and h > 0:
                if calc_type == "i":
                    print(f">> i. Volume: {l * w * h:.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Surface Area: {2*(l*w + l*h + w*h):.2f}")

        # b. Sphere
        elif shape_3d == "b":
            calc_type = input("Enter 'i' for volume or 'ii' for surface area: ")
            r = float(input("Enter Radius: "))
            if r > 0:
                if calc_type == "i":
                    print(f">> i. Volume: {(4/3) * PI_VALUE * (r**3):.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Surface Area: {4 * PI_VALUE * (r**2):.2f}")

        # c. Cylinder
        elif shape_3d == "c":
            calc_type = input("Enter 'i' for volume or 'ii' for surface area: ")
            r = float(input("Enter Radius: "))
            h = float(input("Enter Height: "))
            if r > 0 and h > 0:
                if calc_type == "i":
                    print(f">> i. Volume: {PI_VALUE * (r**2) * h:.2f}")
                elif calc_type == "ii":
                    print(f">> ii. Surface Area: {2 * PI_VALUE * r * (r + h):.2f}")

        # d. Cone
        elif shape_3d == "d":
            calc_type = input("Enter 'i' for volume or 'ii' for surface area: ")
            r = float(input("Enter Radius: "))
            h = float(input("Enter Height: "))
            if r > 0 and h > 0:
                if calc_type == "i":
                    print(f">> i. Volume: {(1/3) * PI_VALUE * (r**2) * h:.2f}")
                elif calc_type == "ii":
                    slant = (r**2 + h**2)**0.5
                    print(f">> ii. Surface Area: {PI_VALUE * r * (r + slant):.2f}")

    elif menu_choice == "3":
        print("Ending session... Goodbye!")
        is_active = False
    
    else:
        print("Invalid option. Please choose 1, 2, or 3.")