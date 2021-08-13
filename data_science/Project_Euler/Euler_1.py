
# import sys


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     i=1
#     sum=0
#     while i<n:
#         if i%3==0 or i%5==0:
#             sum+=i
#         i+=1
#     print(sum)


import sys
t = int(input().strip())
for a0 in range(t):
    empty=[]
    n = int(input().strip())
    for i in range(1,n):
        if i%3==0 or i%5==0:
            empty.append(i)
    print(sum(empty))
    empty.clear()



    # i,sum=1,0
    # while i<n:
    #     if i%3==0 or i%5==0:
    #         sum+=i
    #     i+=1
    # print(sum)    
                       