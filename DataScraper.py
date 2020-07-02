# Scrape data of CSGO matches
import pandas as pd
from bs4 import BeautifulSoup as bs
import codecs

class Scrape():
    def __init__(self):
        super().__init__()

    # function to scrape data from HLTV.com
    def scrapeFromHLTV(self):

        html_doc = codecs.open("hltv.html", "r", "utf-8")

        root = bs(html_doc.read(), "html.parser")
        root.prettify()
        table = (str)(root.find("table",class_='stats-table no-sort'))
        data = pd.read_html(table)[0]
        data = data.drop(data.columns[[2]], axis=1)
        # Give columns proper names
        data.columns = ['Date', 'Event', 'Opponent', 'Map', 'result', 'Outcome']

        # Clean win/loss data and turn to numeric format for compatibilty with machine learning classifier
        data.loc[data.Outcome == 'W', 'Outcome'] = 1
        data.loc[data.Outcome == 'L', 'Outcome'] = 0
        data.loc[data.Outcome == 'T', 'Outcome'] = 0

        # Misc sanitation (datetime conversion, typecasting)
        data['Outcome'] = data['Outcome'].astype(str).astype(int)
        data['Event'] = data['Event'].astype(str)
        data['Date'] = pd.to_datetime(data['Date'])

        print(data)
        # Print resultant dataframe of all merged together top 10 team historic match results
        return data


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrapeFromHLTV()

