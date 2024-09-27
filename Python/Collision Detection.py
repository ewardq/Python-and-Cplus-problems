"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:

def collision(x1, y1, radius1, x2, y2, radius2):  
  # collision?
If a collision is detected, return true. If not, return false.

Here's a geometric diagram of what the circles passed in represent:
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def collision(x1, y1, radius1, x2, y2, radius2): 
    dist_betwn = pow(  pow((x2-x1),2) + pow((y2-y1),2)  , (0.5)) 

    if (dist_betwn < radius1) or (dist_betwn < radius2):
        return True
    else:
        return False

# This solution works but with one important bug for an edge case.

"""""
 =============================  TOP SOLUTION   =======================================

from math import dist
def collision(x1, y1, radius1, x2, y2, radius2): 
    return radius1+radius2 >= dist((x1,y1),(x2,y2)) 

 =====================================================================================  
"""""
