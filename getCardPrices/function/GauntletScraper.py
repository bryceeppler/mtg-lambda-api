import bs4
import requests
import string

class GauntletScraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = {}
        self.baseUrl = 'https://www.gauntletgamesvictoria.ca/products/search?q='
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.baseUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add +
                url+= '+' 
            else: url+= '&c1'
        return url


    def scrape(self):
        print('Scraping ' + self.url)
