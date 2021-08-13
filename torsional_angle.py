import math

class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        print("x: {}, y: {}, z: {}".format(x,y,x))


class TorsionalAngle:
    def __init__(self,points):
        self.points=points
    
    #### dot product
    def subtraction(self):
        res = []
        res.append(Point(self.points[1].x - self.points[0].x,
                        self.points[1].y - self.points[0].y,
                        self.points[1].z - self.points[0].z))
        return res


point = []
for i in range(0,4):
    x = int(input())
    y = int(input())
    z = int(input())
    point.append(Point(x,y,z))

for obj in point:
    print( obj.x, obj.y, obj.z, sep =' ' )

ta = TorsionalAngle(point)
sub = ta.subtraction()

print("len of input: ",len(point))
print("len: ",len(sub))
for obj in sub:
    print( obj.x, obj.y, obj.z, sep =' ' )
    
for i in range(0,len(point)):
    print(i.__str__)



        
