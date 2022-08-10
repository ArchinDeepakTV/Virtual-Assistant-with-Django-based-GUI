def nltkProcessing(article):
    from nltk.tokenize import sent_tokenize
    import nltk
    from GSearch import gSearch, ner

    # nltk.download()
    # nltk.download('punkt')
    # nltk.download('wordnet')
    # nltk.download('stopwords')

    nltk_stopwords = nltk.corpus.stopwords.words('english')
    wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()

    inputs = ''
    doc = sent_tokenize(article)
    for i, token in enumerate(doc):
        inputs = inputs + token

        tkns = nltk.tokenize.word_tokenize(inputs)
        tkns = [tkn for tkn in tkns if not tkn in nltk_stopwords]
        # print(tkns)
        # print()

        # LEMMATIZER
        for tkn in tkns:
            lemmatized_tkn = wordnet_lemmatizer.lemmatize(tkn)

            if tkn != lemmatized_tkn:
                # print(tkn, ' ', lemmatized_tkn)
                for i in range(len(tkns)):
                    if tkns[i] == tkn:
                        tkns[i] = lemmatized_tkn

        print(tkns)
        x, name = ner(tkns)
        if x == 1:
            imageURL = gSearch(name)
            if imageURL == "Error Code 200":
                a = 1
            else:
                return(imageURL)
        else:
            '''google page'''


# articles = 'Lionel Messi'
# nltkProcessing(articles)
