import wikipedia
import webbrowser

url = ''

def article_search(search):
    question = search
    """GET THE URL"""
    result = wikipedia.page(search)
    global url
    url = result.url
    
    """GET THE FIRST THREE SENTENCES"""
    content = wikipedia.summary(question, sentences = 1)
    
    print(content, url)
    return content

def open_in_browser():
    webbrowser.open(url)

    

# article_search("Jupiter")
# open_in_browser()