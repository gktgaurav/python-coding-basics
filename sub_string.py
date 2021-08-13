def count_substring(string, sub_string):
    count=0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            count+=1
        
    print(count)

main_str= 'adadfsfsdasasfdsfsdvaffsafasfcfa'
sub_str= 'as'
count_substring(main_str,sub_str)