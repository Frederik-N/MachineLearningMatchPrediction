# Scrape data of CSGO matches
import math
import re as re
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import learning_curve

class Scrape():
    def __init__(self):
        super().__init__()

    # function to scrape data from HLTV.com
    def scrapeFromHLTV(self):

        # Top team URLS (for scraping match data)
        team = ['https://www.hltv.org/stats/teams/matches/6665/astralis']
        # Pull/scrape/parse data
        r = requests.get(team)
        root = bs(r.content, "html.parser")
        root.prettify()
        table = (str)(root.find("table"))
        data = pd.read_html(table, header=0)[0]

        # Give columns proper names
        data.columns = ['Date', 'Event', 'Opponent', 'Map', 'Rating', 'W/L', 'Outcome']

        # Clean win/loss data and turn to numeric format for compatibilty with machine learning classifier
        data.loc[data.Outcome == 'W', 'Outcome'] = 1
        data.loc[data.Outcome == 'L', 'Outcome'] = 0
        data.loc[data.Outcome == 'T', 'Outcome'] = 0

        # Misc sanitation (datetime conversion, typecasting)
        #data['Outcome'] = data['Outcome'].astype(str).astype(int)
        #data['Event'] = data['Event'].astype(str)
        #data['Date'] = pd.to_datetime(data['Date'])
        #data['Year'] = data['Date'].dt.year
        #data['Team'] = topTeams[i]

        # Print resultant dataframe of all merged together top 10 team historic match results
        return data


if __name__ == '__main__':
    scrape = Scrape()
    print(scrape.scrapeFromHLTV())

