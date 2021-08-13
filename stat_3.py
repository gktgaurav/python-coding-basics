def quantiles(arr):

    res=[]

    ''' *******   Quantiles number 1   ******   '''
    quant1=(arr[0]+arr[1])/2
    res.append(quant1)

    ''' *****    Quantiles number 2  *******  '''

    if len(arr)%2==1:
        res.append(arr[len(arr)//2])
    
    elif len(arr)%2==0:
        res.append((arr[len(arr)-1]+ arr[len(arr)]))


    '''  ******   Quantiles number 3   ******* '''
    quant3 =(arr[-1]+arr[-2])/2
    res.append(quant3)

    print(res)

n=int(input())
arr_1=list(map(int, input().split()))
arr_1.sort()
quantiles(arr_1)

'''#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

    '''
