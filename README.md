```
from bs4 import BeautifulSoup
def remove(soup):
    for tag in soup():
        tag.attrs = None
    return soup
doc = '<p class="whatever">junk</p><div style="background: yellow;" id="foo" class="blah">blah</div>'
print(doc)
soup = BeautifulSoup(doc,'html.parser')
remove(soup)
print(soup)
```
