# findLargest(l) which takes in a list of numbers and returns the value of the smallest number
def findSmallest(l):
    small_so_far = l[0]
    for item in l[1:]:
        if item < small_so_far:
            small_so_far = item
    return small_so_far

def findLargest(l):
    large_so_far = l[0]
    for item in l[1:]:
        if item > large_so_far:
            large_so_far = item
    return large_so_far
#test
print(findLargest([3,4,5,1,2,6]))

# freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency
# of v, that is, the number of times that v appears in l.  
def freq(l,v):
    frequency = 0
    for item in l:
        if item == v:
            frequency = frequency + 1
    return frequency
#test
l=[1,2,3,4,5,5,5,6,7,8,9]
result=freq(l,5)
print(result)