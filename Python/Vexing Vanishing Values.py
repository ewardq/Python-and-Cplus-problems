"""""
Confusion, perplexity, a mild headache. These are just a sample of the things you have experienced in the last few minutes while trying to figure out what is going on in your code.

The task is very simple: accept a list of values, and another value n, then return a new list with every value multiplied by n. 
For example, [1, 2, 3] and 4 should result in [4, 8, 12].

While writing the function, you even added some debugging lines to make sure that you didn't mess anything up, and everything looked good! But for some reason when you run the function 
it always seems to return an empty list, even though you can clearly see, that the list should have the right values in it! Somehow, the values are simply disappearing! 
Is this a bug in the programming language itself...?


ORIGINAL CODE
def mul_by_n(lst, n):
    print("Inputs: ", lst, n) # Check our inputs
    result = (x * n for x in lst)
    print("Result: ", list(result)) # Check our result
    return result

"""""

def mul_by_n(lst, n):
    result = []
    print("Inputs: ", lst, n) # Check our inputs
    for x in lst:
        result.append(x*n)
    print("Result: ", result) # Check our result
    return result

print(mul_by_n([1, 2, 3], 4))
"""""
 =============================  TOP SOLUTION   =======================================
 # The solution was to replace paranthesis by brackets. Before it was creating a touple instead of a list.
 
def mul_by_n(lst, n):
    print("Inputs: ", lst, n) # Check our inputs
    result = [ x * n for x in lst ]
    print("Result: ", result) # Check our result
    return result
    

 =====================================================================================  
"""""
