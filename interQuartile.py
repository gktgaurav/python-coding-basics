from statistics import median
def interQuartile(values,freqs):
    
    '''  ******   Creating a set of sorted array   ******** '''

    s=[]

    for i in range(len(values)):
        count=1
        while count<=freqs[i]:
            s.append(values[i])
            count+=1
    s.sort()

    '''   ********   Creating quantile 1  ********* '''

    q1= median(s[0:len(s)//2])
    
    '''  *******    Creating quantile 2   ********* '''

    q3= median(s[(len(s)+1)//2:len(s)])

    print('%.1f'%(q3-q1))



n=int(input())
val_arr=list(map(int,input().split()))
freq_arr=list(map(int,input().split()))
interQuartile(val_arr, freq_arr)