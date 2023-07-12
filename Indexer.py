vocabulary=[]

f=open("./corpus1.txt",encoding='utf8')
data=f.read().split("\n")
# print(len(data))
f.close()

f2=open("./corpus2.txt",encoding='utf8')
data2=f2.read().split("\n")
# print(len(data2))
data=data+data2
# print(len(data))
data=list(set(data))
# print(len(data))
f2.close()

def getVocabulary():
    return data

vocabulary=data

def generateNGrams(n,word):
    nGrams=[]
    i = 0
    size = len(word)
    while((i+n-1)<size):
        nGrams.append(word[i:i+n])
        i+=1
    return nGrams

def creatNIndex(n,vocabulary):
    nIndex = dict()
    for word in data:
        Ngrams=generateNGrams(n,word)
        for gram in Ngrams:
            if(nIndex.get(gram)==None):
                nIndex[gram]=[word]
            else:
                tlist=nIndex[gram]
                tlist.append(word)
                nIndex[gram]=tlist
    return nIndex