# 2.8 Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

pi=(3.14)

r= input("What is the radius of your circle?")
r= float(r)

area= pi*r**2
print("The area of your circle is", area,".")