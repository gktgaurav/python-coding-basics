arr=[]
n=int(input("Number of Elements: \n"))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
print(arr)
# for i in range(0,len(arr)):
z=min(arr)
print(z)
for i in range(0,len(arr)):
    if arr[i]==z:
        print(i)