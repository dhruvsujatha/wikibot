import wikipedia

def wikiSuggest(keyword):
    suggestResult = wikipedia.suggest(keyword)
    return suggestResult

def wikiSummary(keyword):
    summaryResult = wikipedia.summary(keyword)
    return summaryResult

def wikiImage(keyword):
    imageResult = wikipedia.page(keyword)
    return imageResult.images[0]

def wikiSearch(keyword, noOfResults = 5):
    searchResult = wikipedia.search(keyword, results = noOfResults)
    if searchResult == []:
        suggestResult = wikiSuggest(keyword)
        return {"search": False, "suggest": True, "summary": False, "image": False, "result": [suggestResult]}
    else: 
        loweredCase = list(map(lambda x: x.lower(), searchResult))
        if keyword.lower() in loweredCase:
            summaryResult = wikiSummary(keyword)
            try: 
                imageResult = wikiImage(keyword)
                return {"search": False, "suggest": False, "summary": True, "image": True, "result": [summaryResult, imageResult]}
            except:
                return {"search": False, "suggest": False, "summary": True, "image": False, "result": [summaryResult]}
        else: 
            return {"search": True, "suggest": False, "summary": False, "image": False, "result": [searchResult]}