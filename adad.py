# # x= "Welcome to the Python course!"
# # y= "Python programming is used in the course!"
# # x_ls= x.split(' ')
# # print(x_ls)
# # y_ls= y.split(' ')

# # red=[x1 for x1 in x_ls for y1 in y_ls if x1==y1]
# # print(red)

# final=''
# x= "Mathematics is essential in many fields"
# x_upd=x.split()
# x_upd=[elem[::-1] for elem in x_upd]
# for elem in x_upd:
#     final+=elem + ' '
# print(final)

# s="Lists are mutable sequences, typically used to store collections of homogeneous items."
# x=list(s.lower())
# print(x)
# print({char: x.count(char) for char in x if char.isalpha()})

x={2,3,5,6}
y={10,9,4,1}
x.append(y)
print(x)