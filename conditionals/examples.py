def is_even(n):
    if n%2 == 0:
        return True
    #print(True) is wrong.You should return in a function.
    else:
        return False
    
#shorter and easier way to write the is_even function
def is_even_short_version(n):
    return n%2 == 0
    
def is_odd(n):
    return not(is_even(n))

result = is_even(10)
print("Result for 10 is:" ,result)
result = is_even(11)
print("Result for 11 is:" ,result)
#use print when you want something to show on the screen. The user will see.

print("Direct call short version:" ,is_even_short_version(12))

print("Odd tests")
result = is_odd(10)
print("Result for 10 is:" ,result)
