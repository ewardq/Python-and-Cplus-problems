"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
Task 
You work for a company that analyzes traffic count at a particular intersection during the
peak hours of 4:00 PM to 8:00 PM. Each day, you are given a list that contains the number
of vehicles that pass through the intersection every 10 minutes from 4:00 to 8:00 PM.

You are expected to return a list of tuples that each contain the hour and the maximum 
amount of traffic for each hour.

For example:

a1 = [23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]

traffic_count(a1) ==> [('4:00pm', 45), ('5:00pm', 65), ('6:00pm', 89), ('7:00pm', 93)]
All values in the given list are integers.
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def traffic_count(array):
    four_pm = array[:6]
    five_pm = array[6:12]
    six_pm = array[12:18]
    seven_pm = array[18:24]

    four_pm.sort()
    five_pm.sort()
    six_pm.sort()
    seven_pm.sort()

    peak_four = ('4:00pm', four_pm[-1])
    peak_five = ('5:00pm', five_pm[-1])
    peak_six = ('6:00pm', six_pm[-1])
    peak_seven = ('7:00pm', seven_pm[-1])
    return ([peak_four, peak_five, peak_six, peak_seven])


a1 = [23,24,34,45,43,23,       57,34,65,12,19,45,    54,65,54,43,89,48,        42,55,22,69,23,93]
print(traffic_count(a1))

"""""
 =============================  TOP SOLUTION   =======================================

def traffic_count(array):
    return [('4:00pm', max(array[:6])), ('5:00pm', max(array[6:12])), ('6:00pm', max(array[12:18])), ('7:00pm', max(array[18:]))]

 =====================================================================================  
"""""
