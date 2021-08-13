class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print(self.x**2+self.y**2+self.z**2)
s_1=Point(1,3,5)
s_1.sqSum()