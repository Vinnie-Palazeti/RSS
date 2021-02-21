from datetime import datetime
import requests
from bs4 import BeautifulSoup



foos = {
	'Num': [1,2,3,4],
	'Funcs': [newyorker(),washpost_politics(),washpost_opinions(),washpost_sports()],
	'Alias' : ["New Yorker", "Washington Post Politics", "Washington Post Opinions", "Washington Post Sports"]
}


def newyorker():
  article_list = []

  try:
    page = requests.get('https://www.newyorker.com/feed/news')
    soup = BeautifulSoup(page.content, features='xml')
    articles = soup.findAll('item')

    for a in articles:
      try:
        title = a.find('title').text
      except Exception as e:
        title = "N/A"
      try:
        link = a.find('link').text
      except Exception as e:
        link = "N/A"
      try:
        date = datetime.strptime(a.find('pubDate').text[:-15], "%a, %d %b %Y").strftime('%A, %d %b %Y')
      except Exception as e:
        link = "N/A"
      try:
        author = a.find('dc:creator').text
      except Exception as e:
        author ='N/A'

      article = [
                 date,
                 title,
                 author,
                 link
      ]
      article_list.append(article)

    return article_list 
    

  except Exception as e:
    print('didn\'t work sorry')
    print(e)



def washpost_politics():
  article_list = []

  try:
    page = requests.get('http://feeds.washingtonpost.com/rss/politics?')
    soup = BeautifulSoup(page.content, features='xml')
    articles = soup.findAll('item')

    for a in articles:
      try:
        title = a.find('title').text
      except Exception as e:
        title = "N/A"
      try:
        link = a.find('link').text
      except Exception as e:
        link = "N/A"
      try:
        date = datetime.strptime(a.find('pubDate').text[:-13], "%a, %d %b %Y").strftime('%A, %d %b %Y')
      except Exception as e:
        link = "N/A"
      try:
        author = a.find('dc:creator').text
      except Exception as e:
        author ='N/A'

      article = [
                 date,
                 title,
                 author,
                 link
      ]
      article_list.append(article)

    return article_list 
    

  except Exception as e:
    print('didn\'t work sorry')
    print(e)


def washpost_opinions():
  article_list = []

  try:
    page = requests.get('http://feeds.washingtonpost.com/rss/opinions?')
    soup = BeautifulSoup(page.content, features='xml')
    articles = soup.findAll('item')

    for a in articles:
      try:
        title = a.find('title').text
      except Exception as e:
        title = "N/A"
      try:
        link = a.find('link').text
      except Exception as e:
        link = "N/A"
      try:
        date = datetime.strptime(a.find('pubDate').text[:-13], "%a, %d %b %Y").strftime('%A, %d %b %Y')
      except Exception as e:
        link = "N/A"
      try:
        author = a.find('dc:creator').text
      except Exception as e:
        author ='N/A'

      article = [
                 date,
                 title,
                 author,
                 link
      ]
      article_list.append(article)

    return article_list 
    

  except Exception as e:
    print('didn\'t work sorry')
    print(e)



def washpost_sports():
  article_list = []

  try:
    page = requests.get('http://feeds.washingtonpost.com/rss/sports?')
    soup = BeautifulSoup(page.content, features='xml')
    articles = soup.findAll('item')

    for a in articles:
      try:
        title = a.find('title').text
      except Exception as e:
        title = "N/A"
      try:
        link = a.find('link').text
      except Exception as e:
        link = "N/A"
      try:
        date = datetime.strptime(a.find('pubDate').text[:-13], "%a, %d %b %Y").strftime('%A, %d %b %Y')
      except Exception as e:
        link = "N/A"
      try:
        author = a.find('dc:creator').text
      except Exception as e:
        author ='N/A'

      article = [
                 date,
                 title,
                 author,
                 link
      ]
      article_list.append(article)

    return article_list 
    

  except Exception as e:
    print('didn\'t work sorry')
    print(e)



