from math import pi, pow


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please choose between circle or rectangle")


def rectangle_area():
    length = float(input("Enter Length >>> "))
    width = float(input("Enter Width  >>> "))
    area = length * width
    print("The area of the rectangle >>> ", area)


def circle_area():
    radius = float(input('Enter in Radius >>> '))
    c_area = pi * (pow(radius, 2))
    print("Area of the Circle >>> {:.2f}".format(c_area))


def main():
    get_shape = input('Enter in the shape >>> ')
    get_area(get_shape)


main()
