"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def array_plus_array(arr1,arr2):
    total_sum = 0
    for i in arr1:
        total_sum += i
    for i in arr2:
        total_sum += i
    return total_sum

print(array_plus_array([5,5,5],[1,2,3]))


"""""
 =============================  TOP SOLUTION   =======================================
 
 def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

 =====================================================================================  
"""""
