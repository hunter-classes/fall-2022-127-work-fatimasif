# Madlibs Project 01

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.

# Completed two extras: (1) wrote story in a text file, (2) reused a replacement
# Attempted to capitalize the names as an extra 

# Used inspiration and help with syntax from W3 Schools Python

# Creating and writing a seperate text file (extra)
with open('story.txt', 'w') as f:
    f.write('It was <FOOD> day at school, and <NAME> was super <ADJECTIVE> for lunch. <NAME> went outside to eat, a <NOUN> stole her food! <NAME> chased the <NOUN> all over school. She <VERB> through the playground. Then she tripped on her <NOUN> and the <NOUN> escaped!')
    
import random

# Declaring variables
foods = ['pizza', 'taco', 'burrito', 'pasta', 'burger']
names = ['samantha','paulina','catherine','fatima']
adjectives = ['dirty', 'amazing', 'smelly', 'beautiful', 'tasty', 'happy', 'excited', 'upset']
nouns = ['dog', 'book', 'wallet', 'mouse', 'paint', 'chicken', 'chair']
verbs = ['ate','walked','slept', 'dance', 'run', 'jump']

# Opening the story file and reading it
f = open('story.txt', 'rt')  
story = f.read()
  
# Creating a function to have the madlibs game work. Substituting the placeholders for a input from the lists.
def madlibs():
  word = story.split() # Splitting the string into a list 
  sentence = '' # Used inspiration from Derek's code to create an empty string. Used this to add to my original code which only used if statements that would not work because they made a variable == to a replace and random function
  name = random.choice(names) # Keeping the same name throughout the story (extra)
  for i in word:
      # Each if statement will check for where there is a needed input in the story
    if i == "<NAME>":
      sentence += (" "+name.capitalize()) # Capitalizing the names (attempted extra) and keeping the same name throughout (extra)
      # Using random.choice function to randomly select item from a list and be inputted into the story
      # += operator lets you add two values together and assign the resultant value to a variable
    elif i == "<VERB>":
      sentence += (" "+random.choice(verbs)) 
    elif i == "<NOUN>":
      sentence += (" "+random.choice(nouns)) 
    elif i == "<ADJECTIVE>":
      sentence += (" "+random.choice(adjectives))    
    elif i == "<FOOD>":
      sentence += (" "+random.choice(foods))  
    else:
        sentence += (' '+i)
  return(sentence)
 
# Running and printing the function
print(madlibs())




# Previous old code that is just here to look back on

# keep the same name throughout the story 
#name = random.choice(names)

# capitalizing the names in the story and at the beginning of the sentence 
#f = open('story.txt', 'rt')
#for word in f:
#  word = word.split()
#  for i in word:
#    if i == "<NAME>":
#      if word.index("<NAME>") != 0:
#        name = name.capitalize()

#word = ' '.join(word)
#word = word.replace('<NAME>',name)
#word = word.replace('<FOOD>',random.choice(foods))
#word = word.replace('<ADJECTIVE>',random.choice(adjectives))
#word = word.replace('<NOUN>',random.choice(nouns))
#word = word.replace('<VERB>',random.choice(verbs))
#print(word)



# Another previous old code that is just here to look back to

# Declaring variables 
# verbs=['ate','walked','slept']
# nouns=['dog','hammer','cat','car','frog']
# adjectives=['adorable', 'bright', 'clean', 'fantastic']
# print=('Sam '+verbs[0]+" the "+nouns[0]+" and then "+verbs[1]+" the "+nouns[1]+' later.')

# Creating the madlibs sentences by choosing random items from the lists
# import random
# sentence1=('Sam '+random.choice(verbs)+" the "+random.choice(nouns)+" and then "+random.choice(verbs)+" the "+random.choice(nouns)+' later.')
# sentence2=('Today I went to the zoo. I saw a ' + random.choice(adjectives) +' '+random.choice(nouns)+ ' jumping up and down in its tree. He ' + random.choice(verbs) + ' through the large tunnel that led to its ' + random.choice(nouns)+'.')
