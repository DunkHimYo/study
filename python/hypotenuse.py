import math

class point_lang:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self):
        return abs(self.x-self.y)

class point_hypotenuse:
    
    def hypotenuse(x,y):
        return math.sqrt((x*x)+(y*y))

x=point_lang(1,2).distance()
y=point_lang(3,0).distance()
z=point_hypotenuse.hypotenuse(x,y)
print(y)