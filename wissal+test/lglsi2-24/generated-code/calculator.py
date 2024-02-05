import math

def calculate_ln():
    num = float(input("Enter the number for ln calculation: "))
    result = math.log(num)
    print(f"The ln of {num} is: {result}")

def calculate_solid_area(shape):
    if shape == 'cube':
        side = float(input("Enter the side length of the cube: "))
        area = 6 * side**2
    elif shape == 'sphere':
        radius = float(input("Enter the radius of the sphere: "))
        area = 4 * math.pi * radius**2
    elif shape == 'cylinder':
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        area = 2 * math.pi * radius * height
    else:
        print("Error: Unrecognized shape!")
        return None

    print(f"The area of the solid {shape} is: {area}")
    return area

def calculator():
    operation = input("Enter the type of operation (+, -, *, /, ln, area): ")

    if operation == 'ln':
        calculate_ln()
        return
    elif operation == 'area':
        calculation_type = input("Enter the calculation type (simple, area): ")

        if calculation_type == 'simple':
            num1 = float(input("Enter the first operand: "))
            num2 = float(input("Enter the second operand: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    return
                result = num1 / num2
            else:
                print("Error: Unrecognized operation!")
                return

            print(f"Result of {operation}: {result}")

        elif calculation_type == 'area':
            shape = input("Enter the shape of the solid (cube, sphere, cylinder): ")
            area_result = calculate_solid_area(shape)
            if area_result is not None:
                print(f"Result of area calculation: {area_result}")
        else:
            print("Error: Unrecognized calculation type!")
        return

    num1 = float(input("Enter the first operand: "))
    num2 = float(input("Enter the second operand: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Error: Unrecognized operation!")
        return

    print(f"Result of {operation}: {result}")

calculator()
