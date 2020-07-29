class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


length_ = int(input("Enter the length of the rectangle >>> "))
breadth_ = int(input("Enter the breadth of the rectangle >>> "))
rectangle = Rectangle(length_, breadth_)
print("The area of the rectangle is ", rectangle.calculate_area())