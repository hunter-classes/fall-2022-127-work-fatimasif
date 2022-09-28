# this is a foreach loop

# range is a function that gives a list of items
# starts at 2, goes up to 20 by 3s
for counter in range(2,20,3):
    print(counter)

# these operate the same way
for counter in range (5):
    print(counter)

for counter in [0,1,2,3,4]:
    print(counter)

# this will print each letter
for letter in "this is a sentence":
    print(letter)
    
# while loop
# if while True the loop will continue, if while False it won't
loop_counter = 0
while random.randrange(0,100) < 80:
    print("hello", loop_counter)
    loop_counter = loop_counter + 1
    print("The above loop ran this many times:", loop_counter)
    
# while loop as a counting loop
# first set up a variable to hold the count
i = 0
# then use the boolean to indication when to stop
while i < 5:
    print(i)
    i = i + 1 # don't forget to change the variable so you eventually stop
    
# or count down
i = 5
while i > 0:
    print(i)
    i = i - 1

# you can also traverse over a string
s = 'hello world'
i = 0
while i < len(s):
    print(s[i])
    i = i + 1