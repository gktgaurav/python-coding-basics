def is_balance(my_str):
    count_open=0
    count_close=0
    for i in range(len(my_str)):
        if my_str[i]=='[' or my_str[i]=='{' or my_str[i]=='(':
            count_open+=1
        elif my_str[i]==']' or my_str[i]=='}' or my_str[i]==')':
            count_close+=1
    if count_open==count_close:
        return True
    else:
        return False

given_str='[[]])[{)'
print(is_balance(given_str))
