z= list(map(int,input().split("x")))
n= z[0]
m= z[1]
i=0
while i<(n//2):
    print("-"*(((n//2)*3)-3*i) + ".|."*(2*i+1) + "-"*(((n//2)*3)-3*i))
    i+=1

print("-"*(3*((n//2)-1)+1) + "WELCOME" + "-"*(3*((n//2)-1)+1))

j=((n//2)-1)
while j>=0 and j<=(n//2):
    print("-"*(((n//2)*3)-3*j) + ".|."*(2*j+1) + "-"*(((n//2)*3)-3*j))
    j-=1
    