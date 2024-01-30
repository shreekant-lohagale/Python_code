a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=int(input("Enter the 3rd number"))

if a<b and a<c :
    print(" 1st number is less than 2nd and 3rd value",a)
elif b<a and b<c :
    print(" 2nd number is less than 1st and 3rd value",b)
else:
    print(" 3rd number is less than 1st and 2nd value",c)

