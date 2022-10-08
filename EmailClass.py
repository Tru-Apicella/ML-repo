import string
import numpy as np
import itertools as it
import matplotlib.pyplot as plt

#format for spam and not spam arrays will be as following spam[testing/training[each email[words in email]]]
testing = []
training = []
stesting = []
straining = []
not_spam = [training,testing]
spam = [straining,stesting]
totspam = 0
totnspam = 0
TP = 0
TN = 0
FP = 0
FN = 0
theta = 1
thetarr = []
iterarr = []

def make_arrays(array, type):
    i = 1
    j = 0
    global totnspam
    global totspam
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
            if type == 'normal/':
                totnspam+=1
            elif type == 'spam/':
                totspam+=1
            array[0].append(tmp)

            j+=1
        else:
            for line in f:
                for word in line.split():
                    tmp.append(word.translate(str.maketrans('','',string.punctuation)))
            tmp = list(filter(None,tmp)) 
            if type == 'normal/':
                totnspam+=1
            elif type == 'spam/':
                totspam+=1
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
                matrix[x[0]][y[0]] = ((matrix[x[0]][y[0]])/tot)

def getSentence(sentence):
    index = -1
    index1 = 0
    total = 1
    for x in enumerate(sentence):
        index1 = vocab.index(x[1])
        if index != -1:
            total*=matrix[index][index1]
        index = vocab.index(x[1])
    return total

def W2V(sentence, type):
    total = 1
    if type == 1:
        for x in enumerate(sentence):
            numword = all_spam.count(x[1])
            total*=numword/len(all_spam)
    elif type == 0:
        for x in enumerate(sentence):
            numword = all_not_spam.count(x[1])
            total+=numword/len(all_not_spam)
    return total

def BOW(sentence, type):
    total = 1
    uword = len(list(set(sentence)))
    if type == 1:
        for x in enumerate(sentence):
            numword = all_spam.count(x[1])+1
            total+=numword/(len(all_spam)+uword)
    elif type == 0:
        for x in enumerate(sentence):
            numword = all_not_spam.count(x[1])+1
            total+=numword/(len(all_not_spam)+uword)
    return total

def bayes():
    #putting probability that word is spam in matrix
    i = 0
    global totnspam
    global totspam
    for x in enumerate(spam):
        for y in enumerate(spam[x[0]]):
            n = -1
            for z in spam[x[0]][y[0]]:
                n1 = vocab.index(z)
                if n != -1:
                    nspam = all_spam.count(z)
                    nall = unfiltered_vocab.count(z)
                    bayesprob =((nspam/(totspam+totnspam))/(nall/(totspam+totnspam)))
                    matrix[n][n1]= bayesprob
                n = vocab.index(z)
    for x in enumerate(not_spam):
        for y in enumerate(not_spam[x[0]]):
            n = -1
            for z in not_spam[x[0]][y[0]]:
                n1 = vocab.index(z)
                if n != -1:
                    nspam = all_spam.count(z)
                    nall = unfiltered_vocab.count(z)
                    bayesprob =((nspam/(totspam+totnspam))/(nall/(totspam+totnspam)))
                    matrix[n][n1]= bayesprob
                n = vocab.index(z)
    btest()

def hyp(x,theta):
    return theta*x

def SGD():
    theta = 1
    thetarr = []
    iterarr = []    
    alpha = 0.01
    iter = 0
    num = 0
    while num < 50:
        for i in not_spam[1]:
            x = W2V(i,0)
            #x = BOW(i,0)
            theta = theta - alpha*(hyp(x,theta)-0)*x
            iter+=1
            thetarr.append(theta)
            iterarr.append(iter)
        for i in spam[1]:
            x = W2V(i,1)
            #x = BOW(i,0)
            theta = theta - alpha*(hyp(x,theta)-1)*x
            iter+=1
            thetarr.append(theta)
            iterarr.append(iter)
        num+=1
    test(theta,iterarr,thetarr)

def ngram(sentence, i):
    index = -1
    index1 = 0
    total = 0
    for x in sentence:
        index1 = vocab.index(x)
        if index != -1:
            total+=matrix[index][index1]
        index = vocab.index(x)
    prob = total/len(sentence)
    if prob >= 0.5:
        return 1
    else:
        return 0

def test(theta,iterarr,thetarr):
    i = 0
    while i < 5:
        hypo = hyp(W2V(spam[1][i],1),theta)
        print("the spam hyp is: ", hypo)
        if hypo > 1:
            hypo = 1
            result(1,1)
        else:
            hypo = 0
            result(1,0)
        print("the spam hyp is: ", hypo)
        i+=1
    i = 0
    while i < 5:
        hypo = hyp(W2V(not_spam[1][i],0),theta)
        print("the not spam hyp is: ", hypo)
        if hypo > 1:
            hypo = 1
            result(0,1)
        else:
            hypo = 0
            result(0,0)
        print("the not spam hyp is: ", hypo)
        i+=1
    #report()
    print(theta)
    plt.plot(iterarr, thetarr)
    plt.show()

def btest():
    i = 0
    while i < 5:
        hypo =ngram(spam[1][i],1)
        print("the spam hyp is: ", hypo)
        result(1,hypo)
        i+=1
    i = 0
    while i < 5:
        hypo =ngram(not_spam[1][i],1)
        print("the not spam hyp is: ", hypo)
        result(0,hypo)
        i+=1
    #report()

def result(real, calc):
    if real ==0 and calc == 0:
        global TN
        TN +=1
    if real ==0 and calc == 1:
        global FP
        FP+=1
    if real ==1 and calc == 0:
        global FN
        FN+=1
    if real ==1 and calc == 1:
        global TP
        TP+=1
def report():
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    fscore = 2*(recall*precision)/(recall+precision)
    print("true positive: ",TP," true negative: ",TN," false positive: ",FP," false negative: ",FN," Precision: ",precision," recall: ",recall," fscore: ",fscore)



make_arrays(not_spam, "normal/")
make_arrays(spam, "spam/")
tmp = list(it.chain.from_iterable(spam))
all_spam = list(it.chain.from_iterable(tmp))
tmp = list(it.chain.from_iterable(not_spam))
all_not_spam = list(it.chain.from_iterable(tmp))

unfiltered_vocab = create_vocab()
vocab = list(set(unfiltered_vocab))
s = len(vocab)
matrix = [[0 for x in range(s)] for y in range(s)]
#fill_matrix()
bayes()
#SGD()
print("breakpoint")