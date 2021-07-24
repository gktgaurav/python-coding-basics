num=int(input("Please provide the number \n"))

if num%3 == 0 and num%5 == 0:
    print("number is divisible by 3 and 5")
elif(num%3==0):
    print(" number is divisble by 3")
elif(num%5==0):
    print(" number is divisble by 5")
else:
    print(num)