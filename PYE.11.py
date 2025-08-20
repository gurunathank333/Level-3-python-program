print("Takshashila University")
print (" ongur, tindivanam")
print("....................")
print(" student mark list")
print("....................")
m1=int(input("Enter the python mark:"))
m2=int(input("Enter the dbms mark:"))
m3=int (input("Enter the industry mark:"))
total=m1+m2+m3
print("total mark:",total)
avg=total/3/100
print("average total")
if m1>=40 and m2>=40 and m3>=40:
     print("result:pass")
else:
     print("result:fail")
if (total>=250):
     print("grade:0 grade")
elif (total>=200):
     print("grade:A+grade")
elif (total>=150):
     print("grade:A grade")
else:
     print("grade: B grade")   
