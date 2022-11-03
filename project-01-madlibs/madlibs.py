# Madlibs Project 01

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.

# Basic Assignment

# Declaring variables 
verbs=['ate','walked','slept']
nouns=['dog','hammer','cat','car','frog']
adjectives=['adorable', 'bright', 'clean', 'fantastic']
# print=('Sam '+verbs[0]+" the "+nouns[0]+" and then "+verbs[1]+" the "+nouns[1]+' later.')

# Creating the madlibs sentences by choosing random items from the lists
import random
sentence1=('Sam '+random.choice(verbs)+" the "+random.choice(nouns)+" and then "+random.choice(verbs)+" the "+random.choice(nouns)+' later.')
# sentence2=('Today I went to the zoo. I saw a ' + random.choice(adjectives) +' '+random.choice(nouns)+ ' jumping up and down in its tree. He ' + random.choice(verbs) + ' through the large tunnel that led to its ' + random.choice(nouns)+'.')

print(sentence1)
#print(sentence2)

# Extra: Pay attention to letter case.
# That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase.
# This is except in the case of proper nouns which should always be capitalized.



# Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
names=['Samantha','David','Arthur','Vanessa']

name = random.choice(names)
verb1 = random.choice(verbs)
noun1 = random.choice(nouns)
noun2 = random.choice(nouns)

sentence2=('Today ' + name + ' went to the zoo. ' + name + ' saw a ' + random.choice(adjectives) +' '+noun1+ ' jumping up and down in its tree. He ' + verb1 + ' through the large tunnel that led to its ' + noun2+'.')
print(sentence2)

