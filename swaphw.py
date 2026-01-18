def swap_three_numbers(a, b, c):
  a, b, c = c, a, b
  return a, b, c
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"Original numbers: num1={num1}, num2={num2}, num3={num3}")

swapped_num1, swapped_num2, swapped_num3 = swap_three_numbers(num1, num2, num3)

print(f"Swapped numbers: num1 = {swapped_num1}, num2={swapped_num2}, num3={swapped_num3}")