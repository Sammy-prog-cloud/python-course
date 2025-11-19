class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")
        return self. __height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter only numbers for height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only numbers for width")

    def get_area(self):
        return int(self.__height) * int(self.__width)


def main():
    square = Square()
    height = input("Enter height : ")
    width = input("Enter width : ")
    square.height = height
    square.width = width
    print("Height : ", square.height)
    print("Width : ", square.width)
    print("The area is : ", square.get_area())


main()
