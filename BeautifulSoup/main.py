import requests
from bs4 import BeautifulSoup

response=requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
article_tag=soup.find(name="a",class_="storylink")
article_text=article_tag.getText()
article_link=article_tag.get("href")
article_link.append(article_link)
article_upvote=[int(score.getText().split()[0] for score in soup.find(name="span",class_="score").getText())]

print(article_text)
print(article_link)
print(int(article_upvote[0]))