def generateSuggestedList(word,Bindex,n):
    size=len(word)
    i=0
    slist=[]
    while((i+n-1)<size):
        bg=word[i:i+n]
        poslist=Bindex.get(bg)
        if(poslist!=None):
            poslist=list(set(poslist))
            slist.append(poslist)
        i+=1
    return slist


def lengthCof(word1,word2):
    len1=len(word1)
    len2=len(word2)
    if(len1>len2):
        k=((len2/len1))
        return k
    else:
        k=((len1/len2))
        return k


def editDistance(str1, str2, m, n):
    if m == 0:
        return n
   
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )


def editDistanceScore(word1,word2):
    # print("edit distance")
    if(lengthCof(word1,word2)<=0.7):
        return 0
    value=editDistance(word1,word2,len(word1),len(word2))
    if(value==1 or value==0):
        return 1
    else: 
        return (1/(2**(value-1)))


def ranking(word,slist):
    # print("ranking")
    lCoefficient=len(word)
    ranks=dict()
    for list in slist:
        for str in list:
            freq=ranks.get(str)
            if(freq==None):
                ranks[str]=1
            else:
                ranks[str]=freq+1
    sortRanks=sorted(ranks.items(), key=lambda x:x[1],reverse=True)
    sortRanks=dict(sortRanks[0:20])
    for key in sortRanks.keys():
        freq = sortRanks.get(key)
        lengthCofScore=lengthCof(word,key)
        # editScore=editDistanceScore(word,key)
        # score = freq + editScore
        score=freq+lengthCofScore
        sortRanks[key]=score
    sortRanks=sorted(sortRanks.items(), key=lambda x:x[1],reverse=True)   
    sortRanks=dict(sortRanks)
    return sortRanks



# * refining ranks when first letter is confident
def refine1(word,ranks,i):
    for key in ranks.keys():
        freq=0
        if(word[0]==key[0]):
            freq=i
            score = freq + ranks.get(key)
            ranks[key]=score
    sortedRanks=sorted(ranks.items(), key=lambda x:x[1],reverse=True)
    print(list(dict(sortedRanks))[0:3])
    return sortedRanks


# * refining ranks when last letter is confident
def refine2(word,ranks,i):
    len1=len(word)
    for key in ranks.keys():
        len2=len(key)
        freq=0
        if(word[len1-1]==key[len2-1]):
            freq=i
            score = freq + ranks.get(key)
            ranks[key]=score
    sortedRanks=sorted(ranks.items(), key=lambda x:x[1],reverse=True)
    print(list(dict(sortedRanks))[0:3])
    return sortedRanks
