import requests
from bs4 import BeautifulSoup




URL = "https://issamichuzi.blogspot.com/2023/08/majaliwa-asema-utalii-ukishamiri-sekta.html"
page = requests.get(URL)
print(page)
soup = BeautifulSoup(page.content, "html.parser")
chance = soup.find("div", itemprop="articleBody")
body = chance.find('span')
text = body.get_text()
print(text)

# scrap = BeautifulSoup(page.content, "html.parser")
# # results = soup.find(id="blog1")
# article = scrap.find("div", class_="post-body entry-content")
# chance = scrap.find("div", itemprop="articleBody")
# body = chance.find('span')
# text = remove_tags(body)
# print(text.prettify())
#https://www.edureka.co/blog/web-scraping-with-python/
#https://flask.palletsprojects.com/en/2.3.x/tutorial/blog/
