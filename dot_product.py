import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    
    ###   ''' **** Function for Vector Subtraction  *****  '''
    def sub(self, on):
        return Points(self.x-on.x,self.y-on.y,self.z-on.z)
    

    ##  '''  ****  Function for Dot Product of Vectors  ******  '''
    def dot(self,on):
        return (Points(on.x*self.x, on.y*self.y, on.z*self.z)

    ###   ''' ***** Function for Cross Product of Vectors  ****** '''

    def cross(self, on):
        return (Points((self.y*on.z-(self.z*on.y)), -(self.x*on.z-(self.z*on.x)),  (self.x*on.y-(self.y*on.x))))

    ###   ''' ****** Function for Absolute ******* '''
        
    def absolute(self):
        print(pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5))

A=Points(0,4,5)
B=Points(1,7,6)
C=Points(0,5,9)
D=Points(1,7,2)
AB=B.sub(A)
BC=C.sub(B)
CD=D.sub(C)
X=AB.cross(BC)
Y=BC.cross(CD)
dotXY= X.dot(Y)
m= dotXY.x + dotXY.y + dotXY.z
print(m)
modX= X.absolute()
modY= Y.absolute()
COS=((dotXY)/(modY*modX))
print((COS*3.14)/180)