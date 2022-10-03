import string
not_spam = []
spam = []

def make_arrays(array, type):
    i = 1
    while i <= 25:
        try:
            s1,s2,s3,s4 = 'C:/Users/zoetr/Desktop/email/email/',type, str(i) , '.txt'
            s = ''.join([s1,s2,s3,s4])
            f = open(s, 'r')
        except:
            i+=1
            continue
        i+=1
        for line in f:
            for word in line.split():
                array.append(word)
    i = 0
    for count in enumerate(array):
        x = count[0]
        array[x] = array[x].translate(str.maketrans('','',string.punctuation))
    

make_arrays(not_spam, "normal/")
make_arrays(spam, "spam/")
spam = list(filter(None,spam))
not_spam = list(filter(None,not_spam))
