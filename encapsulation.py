class Student:
    def __init__(self,name,rollNumber):
        self.__name=name
        self.__rollNumber=rollNumber
    
    def setName(self,n):
        self.__name=n

    def getName(self):
        return (self.__name)

    def setRollNumber(self,r):
        self.__rollNumber=r

    def getRollNumber(self):
        return (self.__rollNumber)

s_1=Student('Adil', 49)
print(s_1.getName(),s_1.getRollNumber())
s_1.setName('Kauaa Biryani')
s_1.setRollNumber(69)
print(s_1.getName(),s_1.getRollNumber())

    