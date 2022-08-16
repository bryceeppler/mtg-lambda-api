import bs4
import requests
import string

class KanatacgScraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = {}
        self.baseUrl = 'https://www.kanatacg.com/products/search?query='
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.baseUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url +=word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+'
            else: pass
        return url


    def scrape(self):
        print('Scraping ' + self.url)
