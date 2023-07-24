class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self,width,height):
        s = width * height
        print(s)


    def get_perimetr(self,width,height):
        p = 2 * (width + height)
        print(p)







treul = Rectangle(22,22)
treul.get_area(22,22)
treul.get_perimetr(22,22)
