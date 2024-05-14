#Tkai DeVore
#14Apr24
#P2LAB1
#Variables and Expressions

import math

def main():
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle: "))

    # Calculate diameter, circumference, and area
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    # Format the results
    formatted_diameter = "{:.1f}".format(diameter)
    formatted_circumference = "{:.2f}".format(circumference)
    formatted_area = "{:.3f}".format(area)

    # Display the results
    print("Diameter:", formatted_diameter)
    print("Circumference:", formatted_circumference)
    print("Area:", formatted_area)

if __name__ == "__main__":
    main()

