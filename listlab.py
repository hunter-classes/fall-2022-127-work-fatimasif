# Write a function to find the smallest value in a listKfind smallest in a list of items
    
l=[1,2,3,4,5]
 
# Assign first element as a minimum.
min1 = l[0]

for i in range(len(l)):
 
# If the other element is min than first element
    if l[i] < min1:
        min1 = l[i] #It will change
 
print("The smallest element in the list is ",min1)

# Write a function that returns a new list that contains
# all the odd items in the original list

def odds(num):
    if not num:
        return []
    head = [ num[0] ] if num[0]%2==1 else []
    if len(num)>1:
        return head + odds (num[1:])
    else:
        return head
    
print([0,1,2,3,4,5,6,7,8,9,10])

#Write a function that takes a string and returns a new string where
#all the words are capitalized.
string = ''
def capitalizeWords(string):
    string=string.upper()
    return string
print(capitalizeWords("hello"))

# Write a function that takes a string and returns a new string with
# every word that's longer than 5 character turned into upper case

# Write a function that takes a list of numbers and returns a new list
# with each item squared
def square(list):
    return [i ** 2 for i in list]
print(square([2,3,4]))

# Write a function that takes two lists of numbers and returns a new
# list where each item is the corresponding values of the original
# lists added together. Ex [1,2,3] and [10,20,30] would return the
# list [11,22,33]

# chapter 10
# 10 Count how many words in a list have length 5

# 11 Sum all the elements in a list up to but not including the first even number.
import random

def sum(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum = sum + lst[index]
        index = index + 1
    return sum

lst = []
for i in range(100):
    lst.append(random.randint(0,1000))

print(sum(lst))

# 12 Count how many words occur in a list up to and including the
# first occurrence of the word “sam”.
lst = ["hello","bye","fatima","sam","coding"]
def countSam(samlist):
    returnCount = 0 
    for element in samlist: 
        if element == "sam":
            break
        returnCount = returnCount+1
        return returnCount
print(countSam(lst))
