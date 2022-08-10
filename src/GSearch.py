def ner(tkns):
    import spacy
    nlp = spacy.load("en_core_web_sm")

    text = ''
    for i in tkns:
        text += str(i)
        text += ' '
    doc = nlp(text)

    if(doc[0].tag_ == 'NNP'):
        print(text)
        return 1, text
    return 0, 'nothing'


def gSearch(tkns):
    import requests
    from extraction import extractImage

    url = "https://en.wikipedia.org/wiki/"+tkns.replace(' ', '_')
    get = requests.get(url)
    if get.status_code == 200:
        print('Found '+tkns+' on Wikipedia')
        URL = extractImage(url)
        return URL
    else:
        return "Error Code 200"


def peopleAskFor(name):
    import people_also_ask
    # for a person
    req = people_also_ask.get_related_questions(name, 5)

    res = []
    for i in range(len(req)):
        req[i] = req[i].replace('Search for: ', '')
        x = req[i].split('?')
        res.append(x[0])
    print(res)

    # for questions and answers
    '''
    query = "Why is coffee bad for you?"
    req = people_also_ask.get_simple_answer(query)'''

    return(res)
