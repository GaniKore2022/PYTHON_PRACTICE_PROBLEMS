def invert_integer(number):
    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)
    
    inverted = 0
    while number > 0:
        inverted = (inverted * 10) + (number % 10)
        number //= 10
    
    return -inverted if is_negative else inverted


# Example usage
number1 = 12345
print(invert_integer(number1))  # Output: 54321

number2 = -9876
print(invert_integer(number2))  # Output: -6789

number3 = 0
print(invert_integer(number3))  # Output: 0
