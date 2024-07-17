from itertools import product
def max_xor_string(y,bits):
    Strings=generate_binary_strings(bits)
    max_xor=0
    max_xor_string=''
    for i in Strings:
        current=int(y,2)^int(i,2)
        if current>max_xor:
            max_xor=current
            max_xor_string=i
    return max_xor_string
def generate_binary_strings(x):
    binary_strings = [''.join(p) for p in product('01', repeat=x)]
    return binary_strings
# Example usage:
bits=3
y = "101"
result = max_xor_string(y, bits)
print("Binary string with maximum XOR:", result)