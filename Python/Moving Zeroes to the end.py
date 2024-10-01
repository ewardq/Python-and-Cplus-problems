"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def move_zeros(lst):
    # Check if there are any zeros in array. If not, exit function.
    if 0 in lst == 0:
        return False

    # Bubble sort. Only swap if there are zeros 
    for out_index in range(len(lst)-1):
        for index in range(len(lst) - out_index - 1):
            if (lst[index] == 0):
                lst[index] = lst[index+1]
                lst[index+1] = 0
    return lst

Test1 = [1, 0, 1, 2, 0, 1, 3]

print(move_zeros(Test1))
"""""
 =============================  TOP SOLUTION   =======================================

 =====================================================================================  
"""""
