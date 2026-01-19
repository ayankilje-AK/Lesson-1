num = int(input("Enter a number: "))
t = num
NumLen = 0

while t>0:
    NumLen += 1
    t = int(t/10)

if NumLen >= 4:
    NumLen = int(NumLen/2)
    chk = 0
    while num>0:
        rem = (num%10)
        if chk == NumLen:
           midOne = rem
        elif chk == (NumLen - 1):
            midTwo = rem
        num = int(num/10)
        chk = chk + 1
    product = (midOne*midTwo)
    print("The product of", midOne, "*", midTwo,"=",product)
else:
    print("The number is less than 4 digits. Enter a number that is 4 digits or more")