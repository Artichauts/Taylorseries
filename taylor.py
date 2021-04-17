#imports
from sympy import *

#Variables
x = var("x")
n = 1

#user_input
f_input = str(input("""
enter valid function here
                
"""))
a = int(input("""
enter valid number as your a

""" ))


#function definition
f = sympify(f_input)
print(f(a))

#loop
while n < 100 :
    if n == 1 :
        f = diff(f(x), x)
        f = sympify(f)
        print((f.subs(x, a) * (x - a) ** n) / factorial(n))

    elif 100 > n > 1 :
        f = diff(f, x)
        f = sympify(f)
        print( (f.subs(x, a) * (x - a)**n)/factorial(n))

    elif n == 100 :
        break

    n += 1
