m1=int(input(" Enter the marks for mathematics out of 100 \n"))
m2=int(input(" Enter the marks for science out of 100 \n"))
m3=int(input(" Enter the marks for history out of 100 \n"))
marks_obtained= m1+m2+m3

total_marks= int(input(" enter the total Marks \n"))
print("marks obtained out of total marks is " + str(marks_obtained))
if(m1>=33 and m2>=33 and m3>=33 and marks_obtained>=120):
    print("PASS")
else:
    print("FAIL")

