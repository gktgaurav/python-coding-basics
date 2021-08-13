# # from collections import Counter
# # x=[1,3, 2, 3, 4, 5, 6, 7, 5, 2, 6, 3, 4, 8, 9, 0, 12, 3, 4, 7, 8, 2, 4, 5, 0, 8, 7]
# # y=Counter(x)
# # print(y.most_common())

# # x=[12 ,23, 43,56,52,12,67,53,23,13,67,89,43,26,72]
# # y= sorted(x,key=abs,reverse=True)
# # print(y)

# x=[25,100,225,400,625,900]
# print(sum(x))

s='sgfhghsgfgsh2te23'
count_alnum=0
count_alpha=0
count_digit=0
count_lower=0
count_upper=0
for i in range(0,len(s)):
    if s[i].isalnum() == True:
        count_alnum+=1
    if s[i].isalpha()== True:
        count_alpha+=1
    if s[i].isdigit() == True:
        count_digit+=1
    if s[i].islower()==True:
        count_lower+=1
    if s[i].isupper()==True:
        count_upper+=1

if count_alnum>0:
    print(True)
else:
    print(False)
if count_alpha>0:
    print(True)
else:
    print(False)
if count_digit>0:
    print(True)
else:
    print(False)
if count_lower>0:
    print(True)
else:
    print(False)
if count_upper>0:
    print(True)
else:
    print(False)
