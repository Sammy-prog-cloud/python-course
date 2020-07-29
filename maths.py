class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.breadth * self.length


length_ = int(input('Enter length of the rectangle >>> '))
breadth_ = int(input('Enter breadth of the rectangle >>> '))
obj = rectangle(length_, breadth_)
print('Area of the rectangle >>> ', obj.area())

length = int(input('What is the length of rectangle >>> '))
breadth = int(input('What is the breadth of rectangle >>> '))
area = length * breadth
print('The area of the rectangle >>> ', area)
