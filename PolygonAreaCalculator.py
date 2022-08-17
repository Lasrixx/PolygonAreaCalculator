import math

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        output=""
        for i in range(self.height):
            output+="*"*self.width+"\n"
        return output
    def get_amount_inside(self,shape):
        amountInWidth = math.floor(self.width/shape.width)
        amountInHeight = math.floor(self.height/shape.height)
        print(amountInWidth,amountInHeight)
        return amountInWidth*amountInHeight
    def __str__(self):
        return("Rectangle(width=%d, height=%d)"%(self.width,self.height))

class Square(Rectangle):
    def __init__(self,side):
        self.width = side
        self.height = side
    def set_side(self,side):
        self.width = side
        self.height = side
    def set_width(self,side):
        self.width = side
        self.height = side
    def set_height(self,side):
        self.width = side
        self.height = side
    def __str__(self):
        return("Square(side=%d)"%(self.width))

rect=Rectangle(15,10)
sq = Square(5)
sq.set_side(2)
sq.set_width(4)
sq.set_side(2)
print(rect.get_amount_inside(sq))

