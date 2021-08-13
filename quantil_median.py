from statistics import median
def quantiles(arr):

    q1= median(arr[0:len(arr)//2])
    q2= median(arr)
    q3= median(arr[len(arr)//2:len(arr)])
    print(q1,q2,q3)


n=int(input())
arr_1=list(map(int, input().split()))
arr_1.sort()
quantiles(arr_1)