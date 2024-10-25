"""""
Task 

"""""

def solution(n):
    romanNum = ""
    if n == 1:
        romanNum = 'I'
        return romanNum
    
    while n != 0:
        if n - 1000 >= 0:
            romanNum += 'M'
            n -= 1000
        elif n - 500 >= 0:
            n -= 500
            if romanNum.count('D') == 3:
                romanNum = romanNum.replace('DDD','DM')
            else:
                romanNum += 'D'
        elif n - 100 >= 0:
            n -= 100
            if romanNum.count('C') == 3:
                romanNum = romanNum.replace('CCC','CD')
            else:
                romanNum += 'C'
        elif n - 50 >= 0:
            n -= 50
            if romanNum.count('L') == 3:
                romanNum = romanNum.replace('LLL','LC')
            else:
                romanNum += 'L'
        elif n - 10 >= 0:
            n -= 10
            if romanNum.count('X') == 3:
                romanNum = romanNum.replace('XXX','XL')
            else:
                romanNum += 'X'
        elif n - 5 >= 0:
            n -= 5
            if romanNum.count('V') == 3:
                romanNum = romanNum.replace('VVV','VX')
            else:
                romanNum += 'V'
        elif n != 0:
            
            if romanNum.count('I') == 3:
                romanNum = romanNum.replace('III','IV')
            else:
                romanNum += 'I'
            n -= 1
        else:
            n = 0
    romanNum = romanNum.replace('VIV','IX')
    romanNum = romanNum.replace('LXL','XC')
    romanNum = romanNum.replace('DCD','CM')
    return romanNum


print(solution(1000))

"""""
 =============================  TOP SOLUTION   =======================================
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string
 =====================================================================================  
"""""
