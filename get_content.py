import requests
from bs4 import BeautifulSoup


class GetText:
    def __init__(self, url):
        self.url = url
        self.name = None

    def retrieve(self):
        # Making a GET request
        r = requests.get(self.url, verify=False)

        # check status code for response received
        # success code - 200
        # print(r)

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        # Gets all the links in the website
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))

        # Opens new link, which is the first news article in the website
        r2 = requests.get(links[3], verify=False)

        soup2 = BeautifulSoup(r2.content, 'html.parser')

        self.name = soup2.find('h1', class_='article__title').text
        article_text = soup2.find('div', class_='article-content').text

        return article_text

    def get_title(self):
        return self.name
