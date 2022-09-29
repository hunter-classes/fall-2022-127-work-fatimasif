# count from 1 to 100
for i in range (1,101):
    print(i)
# if the number is divisible by 3, print "fizz"
# if it's divisible by 5 print "buzz"
# and if it's divisible by 3 and 5, print "fizzbuzz"
# if it's not divisible by 3 or 5, print the number
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    if i % 3 == 0:
        print('fizz')
    if i % 5 == 0:
        print('buzz')