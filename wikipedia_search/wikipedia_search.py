import wikipedia

def article_search(search):
    results = wikipedia.summary(search)
    print(results)
    return results

# article_search()