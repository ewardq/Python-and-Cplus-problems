"""""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""""


#operator_dict = {'+', ,
#                 '-', operator.minus,
#                 '%', operator.divided_by,
#                 '*', operator.times}

def zero(argument='0'):
    if argument != '0':
        operation = '0' + argument
        return eval(operation)
    else: return '0'

def one(argument='1'): 
    if argument != '1':
        operation = '1' + argument
        return eval(operation)
    else: return '1'

def two(argument='2'):
    if argument != '2':
        operation = '2' + argument
        return eval(operation)
    else: return '2'
    
def three(argument='3'):
    if argument != '3':
        operation = '3' + argument
        return eval(operation)
    else: return '3'
    
def four(argument='4'):
    if argument != '4':
        operation = '4' + argument
        return eval(operation)
    else: return '4'
    
def five(argument='5'):
    if argument != '5':
        operation = '5' + argument
        return eval(operation)
    else: return '5'

def six(argument='6'):
    if argument != '6':
        operation = '6' + argument
        return eval(operation)
    else: return '6'
    
def seven(argument='7'):
    if argument != '7':
        operation = '7' + argument
        return eval(operation)
    else: return '7'

def eight(argument='8'):
    if argument != '8':
        operation = '8' + argument
        return eval(operation)
    else: return '8'

def nine(argument='9'):
    if argument != '9':
        operation = '9' + argument
        return eval(operation)
    else: return '9'
    

def plus(number): return '+' + number
def minus(number): return '-' + number
def times(number):  return '*' + number
def divided_by(number):  return '//' + number


print(two(minus(two())))  # Must return 2

"""""
 =============================  TOP SOLUTION   =======================================
def identity(a): return a

def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b




USING EVAL
def zero(arg=""):  return eval("0" + arg)
def one(arg=""):   return eval("1" + arg)
def two(arg=""):   return eval("2" + arg)
def three(arg=""): return eval("3" + arg)
def four(arg=""):  return eval("4" + arg)
def five(arg=""):  return eval("5" + arg)
def six(arg=""):   return eval("6" + arg)
def seven(arg=""): return eval("7" + arg)
def eight(arg=""): return eval("8" + arg)
def nine(arg=""):  return eval("9" + arg)

def plus(n):       return '+' + str(n)
def minus(n):      return '-' + str(n)
def times(n):      return '*' + str(n)
def divided_by(n): return '//' + str(n)
 =====================================================================================  
"""""
