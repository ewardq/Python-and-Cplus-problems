"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is
non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""
def count_bits(n):
    count = 0
    binary_str = ''
    
    while n > 0:
        quotient = n % 2
        
        count += quotient
        binary_str = str(quotient) + binary_str
        
        n = (n // 2)
    
    count = count + n
    return count

print(count_bits(4)) # 10

"""""
 =============================  TOP SOLUTION   =======================================

def countBits(n):
    return bin(n).count("1")
    
 =====================================================================================  
"""""
