# Dictionary Practice 11/7/22

d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list']=[2,3,4,5,6]
d[ (1,2) ] = 55
print(d)
d['list']  = 55.3
print(d)

person = {'fist' : "John",
          'last' : "Smith",
          'age' : 50,
          'height' : 60}
person['age'] = person['age'] + 1

print(person)

k = person.keys()
print(k)
for item in k:
    print('person[',item,'] = ',person[item])

# convert the dict_keys thing into a list:
klist = [x for x in person.keys()]
print(klist)

# pull out the values and convert to list
vlist = [x for x in person.values()]


xl = [3,5]
xt = (3,5)
yt = ('hello',44,34.5)
a,b,c = yt

for k,v in person.items():
    print(k,v)

for k in person.keys():
    print(k,person[k])

s1 = {'gender':'m', 'name':'barney','id':1,'scores':[100,99,85]}
s2 = {'gender':'f', 'name':'jen','id':2,'scores':[95,85]}
s3 = {'gender':'m', 'name':'marcel','id':3,'scores':[99,76,88,82]}
s4 = {'gender':'f', 'name':'sookie','id':4,'scores':[98]}

student_list = [s1,s2,s3,s4]
student_dict = {}
for item in student_list:
    student_dict[item['id']] = item
    
s="""this is a string with a bunch of lower case letters. There's nothing too
interesting about it other than the fact that there are a bunch of words
over multiple lines and we're going to do some processing on them
"""

def count_letters(s):
    '''
    count the number of times each letter
    appears in s
    '''
    # ord('a')
    # chr(97)
    counts ={}
    for letter in s:
        if letter in counts.keys():
            counts[letter]=counts[letter]+1
        else:
            counts[letter]=1
    return counts

result = count_letters(s)
print(result)
