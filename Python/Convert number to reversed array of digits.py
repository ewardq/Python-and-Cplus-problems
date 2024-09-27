"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def digitize(n):
    original_num_list = [int(i) for i in str(n)]            # Create a list so we can iterate though the digits
    reversed_list = [original_num_list[len(original_num_list) - i] for i in range(1, len(original_num_list)+1)]         # Create a list begining with last digit
    return reversed_list

print(digitize(1234))



"""""
 =============================  TOP SOLUTION   =======================================
 
 # This solution makes use of list comprehension and string slicing to reverse the list
 
def digitize(n):
    return [int(x) for x in str(n)[::-1]]
    
 =====================================================================================  
"""""
