def stdDev(arr):


    meanDiffSqr=[] 

    ''' *****  Mean  *****  '''

    mean= sum(arr)/(len(arr))
    print(mean)

    '''  ****** Mean difference Square  ****** '''

    for i in range(len(arr)):
        meanDiffSqr.append((arr[i]-mean)**2)
    print(meanDiffSqr)
    Sum_meanDiffSqr= sum(meanDiffSqr)

    standard_deviation= (((Sum_meanDiffSqr)/(len(arr)))**0.5)
    print('%.1f'%standard_deviation)

   

n=int(input())
array= list(map(int,input().split()))
stdDev(array)