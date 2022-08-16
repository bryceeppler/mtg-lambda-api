import bs4
import requests
import string

class HouseOfCardsScraper():
    def __init__(self, cardName):
        self.cardName = cardName
        self.results = {}
        self.baseUrl = 'https://houseofcards.ca/search?page=1&q=%2A'
        self.url = self.createUrl()

    def getResults(self):
        return self.results

    def createUrl(self):
        url = self.baseUrl
        nameArr = self.cardName.split()
        for word in nameArr:
            url += word
            if word != nameArr[len(nameArr)-1]: # then we don't have last item, add %20
                url+= '%20' 
            else: url+= '%2A'
        return url

    def scrape(self):
        print('Scraping ' + self.url)

