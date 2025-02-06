
def count_set_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1  # Increment count if the least significant bit is 1
        n >>= 1  # Right shift the number by 1 to check the next bit
    return count

# Example
n = 7  # Binary representation: 101
print(count_set_bits(n))  # Output: 2
