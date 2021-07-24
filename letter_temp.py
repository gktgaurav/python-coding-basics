# x where is name of the candidate
# zz where is either selected or not selcted
# z where is the date of the result
letter_template= ''' Good afternoon, x. \n I am happy to announce that you z1 selected. \n Thank You.\n Dated: z '''
# print(letter_template)
name=input("Enter the name of candidate \n")
selected = input("Enter either 'are' or 'aren't' \n ")
date= input(" enter the date of result \n")
letter_template = letter_template.replace("x", name)
letter_template = letter_template.replace("z1", selected)
letter_template = letter_template.replace("z", date)
print(letter_template)