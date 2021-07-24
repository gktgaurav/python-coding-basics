num=int(input("Enter the number \n"))
count=0
for i in range(2,num):
    if(num%i==0):
        count=count+1

if(count>1):
    print("its not a prime number")
else:
    print("Bingo its a prime")