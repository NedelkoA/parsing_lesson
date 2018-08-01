# import lxml.html as html
# from urllib.request import urlopen
# import requests
# main_domain_stat = 'https://habr.com/'
# req = requests.get(main_domain_stat)
# page = html.fromstring(req.content)
# page = html.parse(
#     urlopen(main_domain_stat)
# ).getroot()
# article_links = page.xpath(
#     '//li/article[contains(@class,"post")]/h2[@class="post__title"]/a[@class="post__title_link"]/@href'
# )
# article_links = page.xpath(
#     '//li/article[contains(@class,"post")]/div[contains(@class,"post__body")]'
# )
# print(article_links)
# for text in article_links:
#     print(text.xpath('.//text()'))
from bs4 import BeautifulSoup
import requests
url = 'https://habr.com/'
req = requests.get(url)
soup = BeautifulSoup(
    req.content,
    'html.parser',
)
article_list = soup.select(
    'li article.post h2 a'
)
for article in article_list:
    print(article['href'])
