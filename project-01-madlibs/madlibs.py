# Madlibs Project 01
# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.

# Declaring variables 
verbs=['ate','walked','slept']
nouns=['dog','hammer','cat','car','frog']
# print=('Sam '+verbs[0]+" the "+nouns[0]+" and then "+verbs[1]+" the "+nouns[1]+' later.')
import random
print=('Sam '+random.choice(verbs)+" the "+random.choice(nouns)+" and then "+random.choice(verbs)+" the "+random.choice(nouns)+' later.')



