print("Enter number (numerator:)")
numn = int(input("Enter the numerator number"))
print("Enter a number (denominator)")
numd = int(input("Enter the denominator number"))
if numn%numd==0:
    print("\n" + str(numn) + "is divisible by" + str(numd))
else:
    print("\n" + str(numn) + "is not divisible by" + str(numd))