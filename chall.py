# num=[40,35,82,14,22,66,53]
# num.sort()
# print(num)
# k= 3
# count=0
# for i in range(len(num)-1,0,-1):
#     for j in range(len(num)-2,0,-1):
#         if num[i]>num[j]:
#             count+=1
#             if count==k:
#                 print(num[j+1])
#                 break

# def count_low_high(list_1=list(input())):

# def count_low_high(x):
#     low=0
#     high=0
#     if x==[]:
#         print(None)
#     for i in range(0,len(x)):
#         if x[i]>50 or x[i]%3==0:
#             high+=1
#         else:
#             low+=1
#     print([low,high])
# list_1=input()
# count_low_high(list_1)
# l1=[2,5,9,13,3,8,35,5,90,40]
# a=[]
# for i in reversed(range(1,5)):
#     a.append(l1[i])
# print(a)


def func(prices):
    profit_1=[]
    profit_2=[]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            profit=prices[j]-prices[i]
            if profit>0:
                profit_1.append(profit)
            elif profit<=0:
                profit_1.append(0)
        x=max(profit_1)
        profit_2.append(x)
    max_profit=max(profit_2)
    return max_profit
# A=[50,40,30,20,10]
A=[310,315,275,295,260,270,290,230,255,250]
print(func(A))