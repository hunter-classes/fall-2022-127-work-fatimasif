# chapter 10 exercise 4
# Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
def average(numlist):

    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)

grades = [90,95,100,90]
print("grades:",grades)
average=average(grades)
print("Average:",average)

# chapter 10 exercise 6
# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:

def sum_of_squares(xs):
  total = 0 
  for num in numlist:
    total = num * num + total

  return total
  