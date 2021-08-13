
def convertd2b(dec_num):
    if(dec_num == 0):
        print(dec_num)
        return
    empty_stack=[]
    while dec_num>0:
        if dec_num%2==0:
            empty_stack.append(0)
        elif dec_num%2==1:
            empty_stack.append(1)
        dec_num=dec_num//2
    reverse_stack=empty_stack[::-1]
    res = ""
    for i in range(len(reverse_stack)):
         res = res + str(reverse_stack[i])
    print(res)
    print(''.join(map(str, reverse_stack)))

x2=242
convertd2b(x2)    
