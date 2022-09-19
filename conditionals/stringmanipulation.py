def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
    # isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper()
    result = result + first + "."

    # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result2

def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    result2 = ""
    #find the last name and put it first
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result2 = result2 + last + ","
    
    #put the full name following the last name
    first = name[0:location].capitalize()
    result2 = result2 + ' ' + first + ' ' + last
    return result
    
    
# Test initialize
# Test Bondify
result = initialize("james bond")
result2 = bondify("james bond")
print("james bond --> ",result)
print("james bond --> ",result2)

