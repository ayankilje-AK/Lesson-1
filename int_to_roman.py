def int_to_roman(num):
    # Mapping of values to symbols, including subtractive combinations (4, 9, etc.)
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_numeral = ""
    for value, symbol in roman_map:
        # count is how many times the current value fits into num
        # num becomes the remainder
        count, num = divmod(num, value)
        roman_numeral += symbol * count
        
    return roman_numeral

# Example Usage
print(int_to_roman(2))  # Output: MCMXCIV
