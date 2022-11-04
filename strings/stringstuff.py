s1 = "Hello World"
s2 = 'another string'

s3 = """
This is a multiline string
we use the triple quotes
for those
"""

s4 = 'another\nstring'

print(s1)
print(s2)
print(s3)
print(s4)

#if you need a " in your string use ' to write th string and vice versa
print("john's book")
print('john\'s book')

s5 = s1+s2 #string catenation
print(s5)
print(s1*3)

#gives the length/number
print(len(s1))
print(len("abcde"))

#function that makes the letters uppercase
print(s1.upper())

print(s1[1])
print(s1[0:5])

#isolate the world from s1
#first find the space
space_location = s1.find(" ")
print(space_location)
#pull out from 6 (one after the space) until the end
s6 = s1[space_location+1:] # nothing after the : means go to the end
print(s6)
