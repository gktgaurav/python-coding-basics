def print_formatted(number):

    binary_arr=[]
    octa_arr=[]
    hex_arr=[]

    '''  *****   Decimal to Binary   ****** '''
    while number >0:
        binary_arr.append(number%2)
        number=number//2
        print(binary_arr)
    

    




print_formatted(17)