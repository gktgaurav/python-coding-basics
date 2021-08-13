import math

list_1=list(map(float,input().split()))
x=list_1[0]/100
z=1-x
y=list_1[1]
empty_list_1=[]
for i in range(0,3):
    empty_list_1.append((((math.factorial(y))/((math.factorial(i)*math.factorial(y-i))))*(x**i)*(z**(y-i))))

final_1=sum(empty_list_1)
print("%.3f"%final_1)

empty_list_2=[]
for i in range(2,11):
    empty_list_2.append((((math.factorial(y))/((math.factorial(i)*math.factorial(y-i))))*(x**i)*(z**(y-i))))

final_2=sum(empty_list_2)
print("%.3f"%final_2)

