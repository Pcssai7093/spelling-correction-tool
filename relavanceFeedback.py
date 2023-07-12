import refining as refiner
def pseudoRF(word,ranks):
    # print(ranks)
    tempranks=list(ranks.keys())
    tempranks=tempranks[0:5]
    size=len(word)
    firstMatches=0
    endMatches=0
    firstLetter=word[0]
    endLetter=word[size-1]
    for i in tempranks:
        size2=len(i)
        if(i[0]==firstLetter):
            firstMatches+=1
        elif(i[size2-1]==endLetter):
            endMatches+=1
    # print(firstMatches,endMatches)
    if(firstMatches>=endMatches):
        return dict(refiner.refine1(word,ranks,firstMatches)[0:20])
    else:
        return dict(refiner.refine2(word,ranks,endMatches)[0:20])