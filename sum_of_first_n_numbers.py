num=int(input(" Enter the number whose sum of first n natural numbers you want \n"))
i=1
sum=0
while i<= num:
    sum= sum + i
    i=i+1

print("The sum of first n natural numbers is " + str(sum))

