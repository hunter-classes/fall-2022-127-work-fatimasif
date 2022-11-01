# Madlibs Project 01

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.

# Declaring variables 
verbs=['ate','walked','slept']
nouns=['dog','hammer','cat','car','frog']
adjectives=['adorable', 'bright', 'clean', 'fantastic']
# print=('Sam '+verbs[0]+" the "+nouns[0]+" and then "+verbs[1]+" the "+nouns[1]+' later.')

# Creating the madlibs sentences by choosing random items from the lists
import random
sentence1=('Sam '+random.choice(verbs)+" the "+random.choice(nouns)+" and then "+random.choice(verbs)+" the "+random.choice(nouns)+' later.')
sentence2=('Today I went to the zoo. I saw a ' + random.choice(adjectives) +' '+random.choice(nouns)+ ' jumping up and down in its tree. He ' + random.choice(verbs) + ' through the large tunnel that led to its ' + random.choice(nouns)+'.')

random

