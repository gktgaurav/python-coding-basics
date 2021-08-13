def rangoli(num):


    if num%2==1:
        for i in range(0,2*(num//2)):
            print("-"*((4*(num//2))-(2*i))+ str(i) + "-"*((4*(num//2))-(2*i)))













number=int(input())
rangoli(number)