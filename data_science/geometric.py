list_1=list(map(int,input().split()))
n=int(input())
p=list_1[0]/list_1[1]
q=1-p
res=(q**(n-1))*(p)
print("%.3f"%res)
