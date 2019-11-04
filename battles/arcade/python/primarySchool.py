class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        # self.area = width * height
        
    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)



def primarySchool(height, width):
    return str(Rectangle(height, width))

def test():
    testeql(primarySchool(7, 4), "7 x 4 = 28")
