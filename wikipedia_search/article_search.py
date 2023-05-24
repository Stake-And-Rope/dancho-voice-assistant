import wikipedia

def article_search(search):
    question = str(search)
    results = wikipedia.summary(question, sentences = 3)
    print(results)
    return results

# article_search()