from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


# html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())

# bsObj = BeautifulSoup(html.read())
# print(bsObj.h1)


def get_title(url):
    try:
        html = urlopen(url)
        # continue
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html.read())
        title = bs_obj.body.h1
        return title
    except AttributeError as er:
        print(er)
        return None


title = get_title("http://pythonscraping.com/pages/page1.html")


if title == None:
    print("there is no title to show")
else:
    print(title)
