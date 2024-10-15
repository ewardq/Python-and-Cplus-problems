"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
John is a typist. He has a habit of typing: he never use the Shift key to switch case, just using only Caps Lock.

Given a string s. Your task is to count how many times the keyboard has been tapped by John.

You can assume that, at the beginning the Caps Lock light is not lit.

Input/Output
[input] string s

A non-empty string. It contains only English letters(uppercase or lowercase).

1 ≤ s.length ≤ 10000

[output] an integer

The number of times John tapped the keyboard.

Example
For s = "a", the output should be 1.

John hit button a.

For s = "aa", the output should be 2.

John hit button a, a.

For s = "A", the output should be 2.

John hit button Caps Lock, A.

For s = "Aa", the output should be 4.

John hit button Caps Lock, A, Caps Lock, a.
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""

def typist(s):
    upper_flag = False
    count = 0
    for c in s:
        count += 1
        if ((upper_flag == False) and (c.isupper() == True)) or ((upper_flag == True) and (c.isupper() == False)):
            count += 1
        if c.isupper() == True:
            upper_flag = True
        else: upper_flag = False
    return count

print(typist("aA"))



"""""
 =============================  TOP SOLUTION   =======================================
 
def typist(s):
    up=False
    t=len(s)
    for c in s:
        if c.isupper() and not up:
            up=True
            t+=1
        elif c.islower() and up:
            up=False
            t+=1
    return t

 =====================================================================================  
"""""