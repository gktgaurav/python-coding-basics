def print_formatted(number):

    m=number
    n=number
    o=number

    binary_arr=[]
    octa_arr=[]
    hex_arr=[]

    for a in range(1,number):
        print(a,end=" ")        # Printing Decimal

        binary_arr=[]

        m=a
        n=a
        o=a
        while m>0:
            binary_arr.append(m%2)    # Converting decimal to binary
            m=m//2
        print(str(binary_arr[::-1]))
        binary_arr.clear()
        # while n>0:
        #     print(reversed(n%8) , end="")     # Converting decimal to octane
        #     n=n//8
        
        print('\n')
        

    # for i in range(1,m+1):
        
    #     '''  *****   Decimal to Binary   ****** '''
    #     while m>0:
    #         binary_arr.append(i%2)
    #         m=m//2
    
    # for i in range(1,n+1):
    #     '''  *******   Decimal to Binary   ******   '''
    #     while n>0:
    #         octa_arr.append(n%8)
    #         n=n//8

    # for i in range(1,o+1):
    #     '''   *******  Decimal to Hexadecimal   ******   '''
        
    #     while o>0:
    #         if o%16<=9:
    #             hex_arr.append(o%16)
    #             o=o//16
    #         elif o%16==10:
    #             hex_arr.append('A')
    #             o=o//16
    #         elif o%16==11:
    #             hex_arr.append('B')
    #             o=o//16
    #         elif o%16==12:
    #             hex_arr.append('C')
    #             o=o//16
    #         elif o%16==13:
    #             hex_arr.append('D')
    #             o=o//16
    #         elif o%16==14:
    #             hex_arr.append('E')
    #             o=o//16
    #         elif o%16==15:
    #             hex_arr.append('F')
    #             o=o//16

    # return (number,binary_arr,octa_arr,hex_arr)

n=int(input())        
print_formatted(n)




# binary_arr=[]
# number=50
# while number >0:
#     binary_arr.append(number%2)
#     number=number//2
#     print(binary_arr)
