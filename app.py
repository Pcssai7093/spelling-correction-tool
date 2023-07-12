import Indexer as indexer
import searcher as searcher
import relavanceFeedback as rF
import refining as refiner
import assessment as assessor

vocabulary=indexer.getVocabulary

option=-1
def mainMenu():
    print("1. spelling suggester")
    print("2. evaluate spelling suggester")
    print("***[enter the respective number to navigate]")
    global option
    option=int(input("Enter:\n"))

print("--------Welcome to the cli tool for Spell checker--------\n\n")

def spellCheckMenuV1(word):
    n = 2
    index=indexer.creatNIndex(n,vocabulary)
    slist=refiner.generateSuggestedList(word,index,n)
    ranks=refiner.ranking(word,slist)
    print(list(ranks)[0:3])
    return ranks

def spellCheckMenuV2(word):
    n = int(input("Enter the index size:\n"))
    index=indexer.creatNIndex(n,vocabulary)
    slist=refiner.generateSuggestedList(word,index,n)
    ranks=refiner.ranking(word,slist)
    print(list(ranks)[0:3])
    return ranks

def cli():
    global option
    if(option==1):
        word=input("Enter the word:\n")
        if(searcher.checkSpelling(word)==True):
            print("---- Entered word in Correct ----")
            print(" Want To continue to get suggested (y/n) \n")
            cont=input("")
            if(cont!="y"):
                return

        ranks=spellCheckMenuV1(word)
        fb=input("Not satisfied with result? (yes/no)")
        while(fb=="yes"):
            if(fb=="yes"):
                print("Try with other index: Enter 1")
                print("Try filters: Enter 2")
                print("Try pseudo relavance feedback: Enter 3")
                option=int(input("Enter input:"))
                if(option==1):
                    ranks=spellCheckMenuV2(word)
                elif(option==2):
                    print("Are you confident with first letter: Enter 1")
                    print("Are you confident with second letter: Enter 2")
                    filterOption=int(input("Enter input:"))
                    if(filterOption==1):
                        refiner.refine1(word,ranks,20)
                    elif(filterOption==2):
                        refiner.refine2(word,ranks,20)
                elif(option==3):
                    ranks=rF.pseudoRF(word,ranks)
                fb=input("Not satisfied with result? (yes/no)")
        print("Thank you! have a good day")
    elif(option==2):
        n=int(input("Enter index size:\n"))
        file1=input("Enter correct words file:\n")
        file2=input("Enter words words file:\n")
        assessor.printAssessment(file1,file2,n)

        print("Thank you! have a good day")

mainMenu()
cli()
# ['అంకకాండు', 'అరకాండు', 'ఏకకాండ']
    # ['అంకకాండు', 'అంపకాండు', 'ఏకకాండ']
    # ['అంకకాండు', 'అంపకాండు', 'అంకులాండి']
    # ['అంకకాండు', 'ఏకకాండ', 'కినుకకాండు']
    # ['అంకకాండు', 'అంపకాండు', 'అంకులాండి']
    # ['అంకణము', 'అంకనము', 'అంకెము']
    # ['అంకణము', 'అంకనము', 'అంకెము']