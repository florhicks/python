from bs4 import BeautifulSoup
import requests

# User-Agent: *
# Crawl-delay: 30
# Disallow: /context?
# Disallow: /flag?
# Disallow: /from?
# Disallow: /logout
# Disallow: /newcomments
# Disallow: /r?
# Disallow: /reply?
# Disallow: /submit
# Disallow: /submitlink?
# Disallow: /submitted?
# Disallow: /threads?
# Disallow: /vote?
# Disallow: /x?


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.select(selector=".titleline > a:first-child ")
titles_text = [tag.getText() for tag in titles]
# print(titles_text)
titles_link = [tag.get("href") for tag in titles]
# print(titles_link)

titles_upvote = soup.select(selector=".score ")
titles_score = [int(tag.getText().split()[0]) for tag in titles_upvote]
# print(titles_score)

max_score = titles_score.index(max(titles_score))

news = [{title: {"link": link, "score": score}} for title, link, score in zip(titles_text, titles_link, titles_score)]
print(news)

high_score_new = news[max_score]
print(high_score_new)
