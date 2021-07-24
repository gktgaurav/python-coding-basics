num=int(input(" Enter the number whose factorial you want \n"))
x=1
for i in range(num,1,-1):
    x=x*i

print(f" The factorial of {num} is {x}")