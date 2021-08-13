# import math

# x=float(input())
# y=float(input())
# p=x/(x+y)
# q= y/(x+y)
# m=6
# res=[]
# for i in range(3,7):
#     res.append(((math.factorial(m))/((math.factorial(i)*math.factorial(m-i))))*(p**i)*(q**(m-i)))

# final=sum(res)
# print("%.3f"%final)

# # import math

# # def bi_dist(x, n, p):
# #     b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
# #     return(b)

# # b, p, n = 0, 1.09/2.09, 6
# # for i in range(3,7):
# #     b += bi_dist(i, n, p)   
# # print("%.3f" %b)

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = l / r
print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))