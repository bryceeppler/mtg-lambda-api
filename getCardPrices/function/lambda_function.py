from KanatacgScraper import KanatacgScraper
from GauntletScraper import GauntletScraper
from HouseOfCardsScraper import HouseOfCardsScraper

def lambda_handler(event, context):
    name = event['queryStringParameters']['name']
    print("Request received with cardName " + name)

    print('Creating HouseOfCardsScraper')
    houseOfCardsScraper = HouseOfCardsScraper(name)
    print('Creating GauntletScraper')
    gauntletScraper = GauntletScraper(name)
    print('Creating KanatacgScraper')
    kanatacgScraper = KanatacgScraper(name)

    print('Scraping HouseOfCards')
    houseOfCardsScraper.scrape()
    print('Scraping Gauntlet')
    gauntletScraper.scrape()
    print('Scraping Kanatacg')
    kanatacgScraper.scrape()

    print('Retreiving HouseOfCards data')
    houseOfCardsResults = houseOfCardsScraper.getResults()
    print('Retreiving Gauntlet data')
    gauntletResults = gauntletScraper.getResults()
    print('Retreiving Kanatacg data')
    kanatacgResults = kanatacgScraper.getResults()

    print('Merging results')
    results = {
        'houseOfCards': houseOfCardsResults,
        'gauntlet': gauntletResults,
        'kanatacg': kanatacgResults
    }

    return results

