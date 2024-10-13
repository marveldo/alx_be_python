
class Shape:

    def area(self):
        raise NotImplementedError('Method needs to be overwritten')
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f'{3.14 * self.radius * self.radius : .14f}'
    