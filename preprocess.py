import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
#preprocessing
text = open('text.txt','r')
text = text.read()
text = word_tokenize(text)
text = nltk.pos_tag(text,tagset = 'universal')
print(text[0])
#bts = "And this is a sentence that we could use for testing. So yeah, thank-you, Sentence"
x = {",","``","''",")","--","(",":",";","-","&"}
f = open("pos_tagged_words.txt","w")
s = []
for i in text:
    a = i[0].lower()
    if a not in x:
        if a not in stopwords.words('english'):
            if a == '.':
                f.write(a+" ")
            else:
                f.write(a+"/"+i[1]+" ")
f.close()



"""
for brown tagged dataset
for i in bts:
    for j in i:
        if j[0] not in x:
            a = j[0].lower()
            if a not in stopwords.words('english'):
                if a == ".":
                    f.write(a+" ")
                else: 
                    f.write(j[0]+"/"+j[1]+" ")
f.close()
"""