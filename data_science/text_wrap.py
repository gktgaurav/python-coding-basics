
def wrap(string, max_width):
    for i in range(0, (len(string)//max_width)+1):
        z=' '.join(string[4*i:4*i + max_width].split())
    
res= wrap('abcdefghijklmnopqrstuvwxyz', 4)
print(res)


# def wrap(string, max_width):

#     for i in range(0, (len(string)//max_width)+1):
#         print(' '.join(string[4*i:4*i + max_width].split()))
