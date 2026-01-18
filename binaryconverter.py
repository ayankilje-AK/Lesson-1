def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num % 2, end='') 


dec_num = int(input("Enter a number: "))
print(f"The binary representation of {dec_num} is: ", end="")
DecimalToBinary(dec_num)
print() 
