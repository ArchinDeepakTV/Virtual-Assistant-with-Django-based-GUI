from bs4 import *


def aboutInfo(name):
    import re
    import requests
    from htmlhelpers import htmlstring

    url = "https://en.wikipedia.org/wiki/"+name.replace(' ', '_')
    # Fetch URL Content
    r = requests.get(url)

    # Get body content
    soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]
    # print(soup)

    req = ''
    # <div class="Z0LcW">Spanish</div>

    a = soup.findAll('div', class_="Z0LcW")
    print(a)


url = 'https://en.wikipedia.org/wiki/Usain_Bolt'
name = 'Usain Bolt'
aboutInfo(name)
