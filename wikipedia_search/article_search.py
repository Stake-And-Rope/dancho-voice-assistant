import wikipedia

def article_search(search):
    results = wikipedia.summary(search, sentences = 3)
    print(results)
    return results

# article_search()