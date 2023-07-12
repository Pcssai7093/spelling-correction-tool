import Indexer as ind

def checkSpelling(word):
    Vdata=ind.getVocabulary()
    if word not in Vdata:
        return False
    return True