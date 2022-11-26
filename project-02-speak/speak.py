# Project 2 Pirate.org - working solo 

# Your program will take an text file named input.txt and read it in and use the dictionary (described below) to translate the contents of input.txt to pirate-speak. Your program should print out the results.
# Your program should contain a dictionary of substitutions to convert the input file into pirate-speak.
# Extra: Handle upper and lower case and/or punctuation

# Creating and writing a seperate text file 
with open('input.txt', 'w') as f:
    f.write('my friends and I are going to travel to find money. before we get in our car and hit the road, we will get food. we won’t be around our children for a while, it is only us guys.')
    
# Opening the story file and reading it
f = open('input.txt', 'rt')  
story = f.read()

# Creating the dictionary with the Pirate translations
pirateWords = {
    "my":"me",
    "friends":"maties",
    "are":"be",
    "travel":"sail",
    "money":"treasure",
    "before":"afore",
    "car":"boat",
    "the":"th’",
    "road":"sea",
    "food":"chow",
    "around":"aroun'",
    "children":"little sandcrabs",
    "guys":"scurvey dogs"
}


# Function to translate sentence from English to Pirate Speak
def translate(english):
    # Splitting the string into a list 
    import re
    words = re.findall(r"[\w']+|[.,!?;]", story) # Splitting a string into words and punctuation 
    # Substitute the English words with the Pirate translations.
    result = [pirateWords.get(word, word) for word in words]
    # Capitalize words that begin a sentence (EXTRA)
    capitalize = True
    for i, word in enumerate(result):
        if capitalize:
            result[i] = word.capitalize()
            capitalize = False
        if word.endswith((".", "!", "?", ":",)):
            capitalize = True
    return " ".join(result)

print(translate(story))