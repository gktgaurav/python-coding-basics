# ******  Providing Number of Elements in the array   ******
N=int(input())

# ***** Creating an Array of size same as number of elements defined above *******
# arr=[]
# for i in range(0,N):
#     arr.append(int(input())) 
arr = list(map(int, input().split(N)))

#****** Calculating the  Mean  *******

print(sum(arr)/N)

#*****  Calculating the  Median   ********
arr.sort()
arr_1= arr
print(arr_1)
if len(arr_1)%2==1:
    median= arr_1[(N//2)]
    print(median)
elif len(arr_1)%2==0:
    median= ( arr_1[(N//2)-1] + arr_1[(N//2)] )/2
    print(median)

# ******   Calculating the Mode ********

# Step1: Create dictionary
dictionary = {}

# Step2: iterate the array
for i in range(0,len(arr)):

    if arr[i] in dictionary:
        dictionary[arr[i]] += 1
    else:
        dictionary[arr[i]] = 1
    

# Step3: define the variables

mini = 100001
maxi = -1

# Step4: now find the min key
for key, value in dictionary.items():

    if maxi < value:
        maxi = value
        mini = key
    
    if maxi == value and mini > key:
        mini = key

mode=mini
print(mode)




##### Another way of getting Mode ######
arr_2=[]
i=0
while i <len(arr):
    arr_2.append(arr.count(arr[i]))
    i+=1
print(arr_2)
dict1=dict(zip(arr,arr_2))
print(dict1)

mini1 = 100001
maxi1 = -1

# Step4: now find the min key
for key, value in dict1.items():

    if maxi1 < value:
        maxi1 = value
        mini1 = key
    
    if maxi1 == value and mini1 > key:
        mini1 = key

print(mini1)


