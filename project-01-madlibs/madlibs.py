# Madlibs Project 01

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.
with open('story.txt', 'w') as f:
    f.write('It was <FOOD> day at school, and <NAME> was super <ADJECTIVE> for lunch. <NAME> went outside to eat, a <NOUN> stole her <FOOD>! <NAME> chased the <NOUN> all over school. She <VERB>, <VERB>, and <VERB> through the playground. Then she tripped on her <NOUN> and the <NOUN> escaped!')
    
import random

# declaring variables
foods = ['pizza', 'taco', 'burrito', 'pasta', 'burger']
names = ['samantha','paulina','catherine','fatima']
adjectives = ['dirty', 'amazing', 'smelly', 'beautiful', 'tasty', 'happy', 'excited', 'upset']
nouns = ['dog', 'book', 'wallet', 'mouse', 'paint', 'chicken', 'chair']
verbs = ['ate','walked','slept', 'dance', 'run', 'jump']

# keep the same name throughout the story 
name = random.choice(names)

# capitalizing the names in the story and at the beginning of the sentence 
f = open('story.txt', 'rt')
for word in f:
  word = word.split()
  for i in word:
    if i == "<NAME>":
      if word.index("<NAME>") != 0:
        name = name.capitalize()

word = ' '.join(word)
word = word.replace('<NAME>',name)
word = word.replace('<FOOD>',random.choice(foods))
word = word.replace('<ADJECTIVE>',random.choice(adjectives))
word = word.replace('<NOUN>',random.choice(nouns))
word = word.replace('<VERB>',random.choice(verbs))
print(word)

# Old Code
# Declaring variables 
# verbs=['ate','walked','slept']
# nouns=['dog','hammer','cat','car','frog']
# adjectives=['adorable', 'bright', 'clean', 'fantastic']
# print=('Sam '+verbs[0]+" the "+nouns[0]+" and then "+verbs[1]+" the "+nouns[1]+' later.')

# Creating the madlibs sentences by choosing random items from the lists
# import random
# sentence1=('Sam '+random.choice(verbs)+" the "+random.choice(nouns)+" and then "+random.choice(verbs)+" the "+random.choice(nouns)+' later.')
# sentence2=('Today I went to the zoo. I saw a ' + random.choice(adjectives) +' '+random.choice(nouns)+ ' jumping up and down in its tree. He ' + random.choice(verbs) + ' through the large tunnel that led to its ' + random.choice(nouns)+'.')
