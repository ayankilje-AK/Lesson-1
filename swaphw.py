def swap_three_numbers(a, b, c):
  """
  Swaps three numbers in a cyclic manner: a becomes c, b becomes a, c becomes b.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    A tuple containing the swapped numbers (new_a, new_b, new_c).
  """
  a, b, c = c, a, b
  return a, b, c

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"Original numbers: num1={num1}, num2={num2}, num3={num3}")

# Swap the numbers
swapped_num1, swapped_num2, swapped_num3 = swap_three_numbers(num1, num2, num3)

print(f"Swapped numbers: num1={swapped_num1}, num2={swapped_num2}, num3={swapped_num3}")