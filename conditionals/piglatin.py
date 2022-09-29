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
    return result2

# Test Bondify
result2 = bondify("james bond")
print("james bond --> ",result2)

def piglatin(word):
    """
    input: a string representing a word
    returns: a new string with the word converted to piglatin

    Rules:
    if the first letter is a consonent, move it from the start to the end and add "ay"
    so "hello" becomes "ellohay"

    If the first letter is a vowel, just add "yay" to the end
    try to also handle upper case words
    
    """
    result = ''
    #creating variables
    consonent = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    vowel = ('a','e','i','o','u','y')
    ay = 'ay'
    yay = 'yay'
    
    #first letter
    first = word[0]
    if first in consonent:
        wordLength = len(word)
        removeFirstLetter = word[2:wordLength]
        result = word[1].capitalize() + removeFirstLetter + first + ay
     
        
        return result
    else:
        wordLength = len(word)
        result = word[0].capitalize() + word[1:wordLength] + yay
        return result
# Test piglatin

result = piglatin("hello")
print("hello --> ",result)
  
