#  Using the find_all method for bs objects we can get a list of tags, not just the first occurence
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://www.linkedin.com')

bs = BeautifulSoup(html.read(), 'html.parser')

name_list = bs.findAll('span', {'class': 'green'})
for name in name_list:
    print(name.get_text())
