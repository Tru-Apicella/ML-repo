import string
import itertools as it

from sympy import true
#format for spam and not spam arrays will be as following spam[testing/training[each email[words in email]]]
testing = []
training = []
stesting = []
straining = []
not_spam = [training,testing]
spam = [straining,stesting]

def make_arrays(array, type):
    i = 1
    j = 0
    while i <= 25:
        try:
            s1,s2,s3,s4 = 'C:/Users/zoetr/Desktop/email/email/',type, str(i) , '.txt'
            s = ''.join([s1,s2,s3,s4])
            f = open(s, 'r')
        except:
            i+=1
            continue
        i+=1
        tmp = []
        if (j < 5):
            for line in f:
                for word in line.split():
                    tmp.append(word.translate(str.maketrans('','',string.punctuation)))
            tmp = list(filter(None,tmp))
            array[0].append(tmp)

            j+=1
        else:
            for line in f:
                for word in line.split():
                    tmp.append(word.translate(str.maketrans('','',string.punctuation)))
            tmp = list(filter(None,tmp)) 
            array[1].append(tmp)

make_arrays(not_spam, "normal/")
make_arrays(spam, "spam/")
tmp = list(it.chain.from_iterable(spam))
all_spam = list(it.chain.from_iterable(tmp))
tmp = list(it.chain.from_iterable(not_spam))
all_not_spam = list(it.chain.from_iterable(tmp))
vocabulary = []

for x in all_spam:
    check = 0
    for y in all_not_spam:
        if x == y:
            check = 1
            break
    if check == 0:
        vocabulary.append(x)

for x in all_not_spam:
    check = 0
    for y in all_spam:
        if x == y:
            check = 1
            break
    if check == 0:
        vocabulary.append(x)

i = 0
while i < len(vocabulary):
    if i % 25 == 0:
        print (vocabulary[i])
    i+=1
