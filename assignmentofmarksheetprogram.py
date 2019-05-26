# mark sheet of 5 subjects
sub1=int(input("english marks:"))
sub2=int(input("urdu marks:"))
sub3=int(input("maths marks:"))
sub4=int(input("physics marks:"))
sub5=int(input("islamiat marks:"))
sum = sub1+sub2+sub3+sub4+sub5
avg= sum/425*100
print(avg)
if avg >= 100:
    print("error in entering the marks,please try again")
elif avg >= 80 and avg < 100:
    print("Grade: A+")
elif avg >= 70 and avg < 80:
    print("Grade: A")
elif avg >= 60 and avg < 70:
    print("Grade: B")
elif avg >= 50 and avg < 60:
    print("Grade: C")
elif avg >= 40 and avg < 50:
    print("Grade: D")
else:
    print("FAIL")
