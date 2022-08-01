''' SET Bit

We want to take a string of binary digits and want to set one of them to true'''


def set_bit(x, pos):
    mask = 1 << pos  # construct a 1, then left shift to the positions
    return x | mask  # return mask or input string


input_bits = 0b00000110  # 6
position = 0b00000101  # 5
mask = 1
# answer = 00100110 # 2+4+32=38


print(set_bit(x=input_bits, pos=position))
