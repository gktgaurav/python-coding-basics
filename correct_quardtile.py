def quantiles(arr):

    '''   *******   Case for Quantile2 *****88  '''

    if len(arr)%2==0:
        q2= ((arr[len(arr)//2-1] + arr[len(arr)])/2)
        # return q2
    else:
        q2=arr[len(arr)//2]
        # return q2

    '''   *******   Case for Quantile1   ******  '''


    mid1= len(arr)//2
    if mid1%2==0:
        q1= ((arr[mid1//2-1] + arr[mid1//2])/2)
        # return q1
    else:
        q1=arr[mid1//2]
        # return q1

    '''  *****  Case for quantile 3  *******  '''
    mid2= mid1 + mid1//2
    if mid2%2==0:
        q3= ((arr[mid2 +1] + arr[mid2])/2)
        # return q3
    
    else:
        q3= arr[mid2]
        # return q3

    print(q1,q2,q3)
    
   
n=int(input())
array=list(map(int,input().split()))
array.sort()
quantiles(array)
