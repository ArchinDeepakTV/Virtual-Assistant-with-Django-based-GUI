from bs4 import *


def extractImage(url):
    import re
    import requests

    # Fetch URL Content
    r = requests.get(url)

    # Get body content
    soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]

    # Initialize variable

    images = []
    req = ''

    # Iterate throught all tags
    for tag in soup.find_all():
        if tag.name == "img":
            # Add url and Image source URL
            images.append(url+tag['src'])

    # for i in range(10):
    #     print(images[i])

    # print()
    for i in range(len(images)):
        if images[i].endswith('jpg'):
            # print(images[i])
            req = images[i]
            break

    req = req.replace('220px', '940px')
    req = 'https:'+req.replace(url, '')
    print(req)
    return req


def aboutInfo(name):
    import re
    import requests

    url = "https://en.wikipedia.org/wiki/"+name.replace(' ', '_')
    r = requests.get(url)

    if r.status_code == 200:
        print('Found '+name+' on Wikipedia')

        # Get body content
        soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]
        # print(soup)

        req = ''

        # Iterate throught all tags
        for tag in soup.find_all():
            if tag.name == "p":
                # Add url and Image source URL
                print(tag.text)
                req = req+tag.text
                if len(req) > 2000:
                    req = req.replace(';', '')
                    break

    # res = re.search('[(.*)]', req)
    return req
