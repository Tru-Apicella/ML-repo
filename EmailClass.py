import string
import numpy as np
import itertools as it

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


def create_vocab():
    vocabulary = []
    for x in all_spam:
        vocabulary.append(x)

    for x in all_not_spam:
        vocabulary.append(x)
    return vocabulary

def fill_matrix():
    for x in enumerate(spam):
        for y in enumerate(spam[x[0]]):
            n = -1
            for z in enumerate(spam[x[0]][y[0]]):
                n1 = vocab.index(z[1])
                if n != -1:
                    matrix[n][n1]+=1
                n = vocab.index(z[1])
    for x in enumerate(not_spam):
        for y in enumerate(not_spam[x[0]]):
            n = -1
            for z in enumerate(not_spam[x[0]][y[0]]):
                n1 = vocab.index(z[1])
                if n != -1:
                    matrix[n][n1]+=1
                n = vocab.index(z[1])
    
def corpus():
    for x in enumerate(matrix):
        for y in enumerate(matrix[x[0]]):
            if matrix[x[0]][y[0]]!=0:
                tot = sum(matrix[x[0]])
                i = 0
                while i < len(matrix[x[0]]):
                    tot += matrix[i][x[0]]
                    i+=1
                matrix[x[0]][y[0]] = ((matrix[x[0]][y[0]])/tot)



make_arrays(not_spam, "normal/")
make_arrays(spam, "spam/")
tmp = list(it.chain.from_iterable(spam))
all_spam = list(it.chain.from_iterable(tmp))
tmp = list(it.chain.from_iterable(not_spam))
all_not_spam = list(it.chain.from_iterable(tmp))

vocab = create_vocab()
vocab = list(set(vocab))
#vocab = list(set(vocab))
s = len(vocab)
matrix = [[0 for x in range(s)] for y in range(s)]
fill_matrix()
corpus()
i = 0
tot = 1
while i < len(not_spam[0][1]):
    n = vocab.index(not_spam[0][1][i])
    n1 = vocab.index(not_spam[0][1][i+1])
    tot*=matrix[n][n1]
    print(not_spam[0][1][i+1], matrix[n][n1],tot)
    i+=1
#print(matrix[0])
print("breakpoint")