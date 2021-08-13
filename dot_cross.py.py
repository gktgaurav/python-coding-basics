import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    ###   ''' **** Function for Vector Subtraction  *****  '''
    def __sub__(self, on):
        return Points(self.x-on.x,self.y-on.y,self.z-on.z)

    
    ###   ''' ***** Function for Cross Product of Vectors  ****** '''
    def cross(self, on):
        return (Points((self.y*on.z-(self.z*on.y)), -(self.x*on.z-(self.z*on.x)),  (self.x*on.y-(self.y*on.x))))

   

    ##  '''  ****  Function for Dot Product of Vectors  ******  '''
    def dot(self,on):
        return on.x*self.x + on.y*self.y + on.z*self.z
    
    
    def absolute(self):
        return (pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5))

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
    print(points)
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    ### AB x BC
    ### BC x CD
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    print(type(x))
    print(type(y))
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print(type(angle))
    print("%.2f" % math.degrees(angle))
    



'''

A=Points(0,4,5)
B=Points(1,7,6)
C=Points(0,5,9)
D=Points(1,7,2)
AB=(B-A)
print(AB.x, AB.y, AB.z)
BC=(C-B)
print(BC.x,BC.y,BC.z)
CD=(D-C)
print(CD.x,CD.y,CD.z)
X=AB.cross(BC)
print(X.x,X.y,X.z)
Y=BC.cross(CD)
print(Y.x,Y.y,Y.z)
dotXY= X.dot(Y)
print(dotXY.x,dotXY.y,dotXY.z)
m= dotXY.x + dotXY.y + dotXY.z
print(m)
modX= X.absolute()
print(modX)
modY= Y.absolute()
print(modY)
COS=((m)/(modY*modX))
print(COS)
print((COS*3.14)/180)

'''