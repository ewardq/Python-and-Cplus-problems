"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def sum_digits(number):
    temp_number = number
    sum = 0
    while True:
        for digit in str(temp_number):  
            sum += int(digit) 
        if sum < 10:
            break
        temp_number = sum
        sum = 0
    return(sum)

#   if sum == 0 or sum == 3 or sum == 6 or sum == 9:
#       total_sum += number

def is_divisible_by(number, dividend):
    if number % dividend == 0:
        return True
    else: return False
        
        
def solution(number):
    if number <= 3:
        return 0

    total_sum = 0
    temp_number = number - 1
    
    while temp_number >= 3:
        
        if is_divisible_by(temp_number, 3) == True:
            total_sum += temp_number
        elif is_divisible_by(temp_number, 5) == True:
            total_sum += temp_number
            
        print("n > ", temp_number, "| total_sum > ", total_sum)

        temp_number -= 1
        
    return(total_sum)

print(solution(6))


"""""
 =============================  TOP SOLUTION   =======================================

 def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

 =====================================================================================  
"""""