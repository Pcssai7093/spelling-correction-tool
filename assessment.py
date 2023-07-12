import re
import Indexer as indexer
import searcher as searcher
import relavanceFeedback as rF
import refining as refiner

vocabulary=indexer.getVocabulary()

# f1 = open("wrongWords.txt",encoding="utf8")
# data1=f1.read()
# data1=re.sub(" ","",data1)
# data1=re.sub("'","",data1)
# data1=data1.split(",")
# f1.close()


# f2 = open("correctWords.txt",encoding="utf8")
# data2=f2.read()
# data2=re.sub(" ","",data2)
# data2=re.sub("'","",data2)
# data2=data2.split(",")
# f2.close()
# print(len(data1))
# print(len(data2))

# print(data1)


def printAssessment(cwFile,wwFile,n=2):
    f1 = open(wwFile,encoding="utf8")
    data1=f1.read()
    data1=re.sub(" ","",data1)
    data1=re.sub("'","",data1)
    data1=data1.split(",")
    f1.close()


    f2 = open(cwFile,encoding="utf8")
    data2=f2.read()
    data2=re.sub(" ","",data2)
    data2=re.sub("'","",data2)
    data2=data2.split(",")
    f2.close()

    # * index length 2
    Index_2=indexer.creatNIndex(n,vocabulary)
    matches=0
    totalWords=len(data1)
    i=0
    for word in data1:
       
        slist=refiner.generateSuggestedList(word,Index_2,2)
        ranks=refiner.ranking(word,slist)
        # print(ranks)
        # print(data1[0]," ",list(ranks.items())[0][0])
        # print(data1[0]==list(ranks.items())[0][0])
        outputWord=list(ranks.items())[0][0]
        # print(word,outputWord)
        # print(word,"   ",outputWord,"   ",data2[i])
        if(outputWord==data2[i]):
            matches+=1
        i+=1
    # print(matches)
    print("Precision is: ",matches/totalWords)


    # word=data1[3]
    # print(word)
    # slist=refiner.generateSuggestedList(word,Index_2,2)
    # ranks=refiner.ranking(word,slist)
    # outputWord=list(ranks.items())[0][0]
    # print(outputWord)



# printAssessment("correctWords.txt","wrongWords.txt",2)