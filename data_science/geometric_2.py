list_1=list(map(int,input().split()))
n=int(input())
p=list_1[0]/list_1[1]
q=1-p
empty=[]
for n in range(1,n+1):
    empty.append((q**(n-1))*(p))
res=sum(empty)
print("%.3f"%res)
