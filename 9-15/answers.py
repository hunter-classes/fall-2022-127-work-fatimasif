# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

from test import testEqual

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

testEqual(is_even(10), True)
testEqual(is_even(5), False)
testEqual(is_even(1), False)
testEqual(is_even(0), True)

#Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

testEqual(is_even(10), False)
testEqual(is_even(5), True)
testEqual(is_even(1), True)
testEqual(is_even(0), False)

# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled(a,b,c):
  if abs(c**2 - (a**2 + b**2) < 0.001):
        return True
    else:
        return False

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))
print(is_rightangled(a,b,c))

# Extend the above program so that the sides can be given to the function in any order.